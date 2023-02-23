import scapy.contrib.http2 as h2
import json

# 后续补充其他类型帧
def extract_type(frame_name):
    if frame_name.startswith('<headers-frame'):
        frame_type = 'headers'
    elif frame_name.startswith('<continuation-frame'):
        frame_type = 'continuation'
    elif frame_name.startswith('<data-frame'):
        frame_type = 'data'
    elif frame_name.startswith('<padded-headers-frame'):
        frame_type = 'padded-headers'
    # elif frame_name.startswith('<continuation-frame'):
    #     frame_type = 'continuation'
    return frame_type

# "<padded-headers-frame-pool-1:1>": {
# ":method": "POST\u0011",
# ":scheme": "https",
# ":path": "/reqid=203",
# ":authority": "47.96.175.128",
# "content-length": "10",
# "flags": [
# "P",
# "ES",
# "EH"
# ],
#"padding": "5\r\nBBBBB\r\n0\r\n\r\n"
#},
def extract_headers(fileds_dict):
    headers_lst = []
    for key, value in fileds_dict.items():
        header_name = key
        header_value = value
        headers_lst.append(h2.HPackLitHdrFldWithoutIndexing(
            hdr_name=h2.HPackHdrString(data=h2.HPackLiteralString(header_name)),
            hdr_value=h2.HPackHdrString(data=h2.HPackLiteralString(header_value))
        ))
    return headers_lst


def build_frame(fileds_dict, frame_type):

    if frame_type == 'headers' or frame_type == 'padded-headers' or frame_type == 'priority-headers' or frame_type == 'continuation' or frame_type == 'push-promise':
        flag_values = set(fileds_dict['flags'])
        id_value = 1
        fileds_dict.pop('flags')
        if frame_type == 'headers':
            headers_lst = extract_headers(fileds_dict)
            return h2.H2Frame(flags=flag_values, stream_id=id_value) / h2.H2HeadersFrame(hdrs=headers_lst)
        elif frame_type == 'continuation':
            headers_lst = extract_headers(fileds_dict)
            return h2.H2Frame(flags=flag_values, stream_id=id_value) / h2.H2ContinuationFrame(hdrs=headers_lst)
        elif frame_type == 'padded-headers':
            padding_payload = fileds_dict['padding']
            fileds_dict.pop('padding')
            headers_lst = extract_headers(fileds_dict)
            return h2.H2Frame(flags=flag_values, stream_id=id_value) / h2.H2PaddedHeadersFrame(hdrs=headers_lst,
                                                                                           padding=padding_payload.encode())
    elif frame_type == 'data' or frame_type == 'padded-data':
        flag_values = set(fileds_dict['flags'])
        id_value = 1
        payload = fileds_dict['data']
        if frame_type == 'data':
            return h2.H2Frame(flags=flag_values, stream_id=id_value) / h2.H2DataFrame(data=payload)
        else:
            padding_payload = fileds_dict['padding']
            return h2.H2Frame(flags=flag_values, stream_id=id_value) / h2.H2PaddedDataFrame(data=payload,
                                                                                            padding=padding_payload.encode())

def load_data(file_name):
    with open(file_name,'r') as load_f:
        load_dict = json.load(load_f)

    return load_dict

if __name__ == "__main__":

    frames_dict = load_data(file_name="./caddy_attack_data.json")
    frames = []
    for anomaly_name, frame_dict in frames_dict.items():
        for frame_name, frame_fileds in frame_dict.items():
            frame_type = extract_type(frame_name=frame_name)
            frame = build_frame(fileds_dict=frame_fileds, frame_type=frame_type)
            frame.show()
            frames.append(frame)



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
    elif frame_name.startswith('<goaway-frame'):
        frame_type = 'goaway'
    elif frame_name.startswith('<priority-headers-frame'):
        frame_type = 'priority-headers'
    return frame_type



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
        elif frame_type == 'priority-headers':
            exclusive_value = fileds_dict['exclusive']
            dependency_value = fileds_dict['dependency']
            weight_value = fileds_dict['weight']
            fileds_dict.pop('exclusive')
            fileds_dict.pop('dependency')
            fileds_dict.pop( 'weight')
            headers_lst = extract_headers(fileds_dict)
            return h2.H2Frame(flags = flag_values, stream_id = id_value)/h2.H2PriorityHeadersFrame(exclusive=int(exclusive_value), stream_dependency = int(dependency_value), weight = int(weight_value), hdrs=headers_lst)
    
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

    elif frame_type == 'goaway':
        flag_values = set(fileds_dict['flags'])
        id_value = 1
        fileds_dict.pop('flags')
        last_stream_id_value = fileds_dict['last_stream_id']
        # 这个位置取出error还有点问题
        error = fileds_dict['error']
        # print(error)

        error_value = h2.H2ErrorCodes.SETTINGS_TIMEOUT
        print(error_value)
        additional_data_value = fileds_dict['additional_data']
        return h2.H2Frame(flags = flag_values, stream_id = id_value)/h2.H2GoAwayFrame(last_stream_id = int(last_stream_id_value), error = int(error_value), additional_data=additional_data_value.encode())


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
            # frame.show()
            frames.append(frame)



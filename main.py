from h2client import H2Client
from  frm2json import save_attack_data, save_get_request
import time
if __name__ == '__main__':
    # 将生成异常帧的json
    # save_attack_data('caddy')
    save_attack_data('caddy')
    # 生成正常get请求的json
    save_get_request()
    #
    dn = '127.0.0.1'
    port = 443
    attack_data = 'caddy_attack_data.json'
    get_request = 'normal_get_data.json'
    caddy_anomaly_req_id = ["req_256", "req_392", "req_854", "req_150",  "req_637", "req_887", "req_963", "req_61", "req_144", "req_537", "req_554","req_755", "req_924", "req_982"]
    for id in caddy_anomaly_req_id:

        h2client = H2Client(verbose=True)
        print(f'req_id:{id}')
        h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type=id)
        # 去掉注释 同一个py文件发送两个请求
        # h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')
        print(f'time sleep:  5s')
        time.sleep(5)



   
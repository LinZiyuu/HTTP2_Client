from h2client import H2Client
from  frm2json import save_attack_data, save_get_request
import time
if __name__ == '__main__':

    # 生成正常get请求的json
    save_get_request()
    dn = '127.0.0.1'
    port = 443

    get_request = 'normal_get_data.json'
    
    h2client = H2Client(verbose=True)
    h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')




   
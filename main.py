from h2client import H2Client
from  frm2json import save_attack_data, save_get_request

if __name__ == '__main__':
    # 将生成异常帧的json
    save_attack_data()
    # 生成正常get请求的json
    save_get_request()
    #
    dn = '172.17.168.200'
    port = 443
    attack_data = 'caddy_attack_data.json'
    get_request = 'normal_get_data.json'
    h2client = H2Client(verbose=True)
    h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type='no_missmatch_check_frm1')
    h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')

    h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type='header_after_end_header_frm1')
    h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')

    h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type='header_after_end_header_frm2')
    h2client.send(dn='172.17.168.200', port=port, file_name=get_request, anomaly_type='get_frm')

    h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type='header_after_end_header_frm3')
    h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')

    h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type='header_after_end_header_frm4')
    h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')

    h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type='miss_end_stream_frm1')
    h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')

    h2client.send(dn=dn, port=port, file_name=attack_data,
                  anomaly_type='miss_end_stream_frm2')
    h2client.send(dn=dn, port=port, file_name=get_request, anomaly_type='get_frm')
import json
# with open("./caddy_attack_data.json",'r') as load_f:
#     load_dict = json.load(load_f)
#     print(load_dict.keys())
# load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
# print(load_dict)

# with open("../config/record.json","w") as dump_f:
#     json.dump(load_dict,dump_f)
def load_data(file_name):
    with open(file_name,'r') as load_f:
        load_dict = json.load(load_f)

    return load_dict
frames_dict = load_data(file_name="./caddy_attack_data.json")
print(frames_dict.keys())
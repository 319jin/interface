import json
import os,sys
pwd = os.getcwd()
base_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)


def get_json(path=None):
    "读取json文件中的数据,如果path为空获取mock文件中的数据，如果不为空获取其他文件中的数据"
    if path == None:
        with open(base_path+"/Config/mock.json",'r',encoding='utf-8') as f:
            data = json.load(f)
    else:
        with open(base_path + path, 'r',encoding='utf-8') as f:
            data = json.load(f)
    return data

def get_value(key,path=None):
    "根据字段的key获取value的值"
    data = get_json(path)
    return data.get(key)


def write_value(key,value,path=None):
    "根据字典的key写入value"
    data = get_json(path)
    data[key]=value
    data = json.dumps(data)
    if path == None:
        path = base_path+"/Config/mock.json"
    else:
        path = base_path + path
    with open(path,'w',encoding='utf-8') as f:
        f.write(data)





if __name__ == "__main__":
    # print(get_value("login"))
    # print(get_value("cookie","/Config/cookie.json"))
    print(write_value('/ui/user/add',{"msg": "密码必须为包含字母和数字且长度为8到12位", "status": -1}))
    print(write_value('/ui/user/add/passwd/number',{"msg": "密码必须为包含字母和数字且长度为8到12位", "status": -1}))
    print(write_value('/ui/user/add/passwd/letter',{"msg": "密码必须为包含字母和数字且长度为8到12位", "status": -1}))
    print(write_value('/ui/user/add/passwd/LowerLetter',{"msg": "操作成功", "status": 0}))
    print(write_value('/ui/user/add/passwd/capitalLetter',{"msg": "操作成功", "status": 0}))




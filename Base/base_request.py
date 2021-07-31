#coding=utf-8

import json,requests
from Base.read_db import oracle

class BaseRequest():

    def send_post(self,url,data,headers=None):
        """post请求"""
        res = requests.post(url=url,data=data,headers=headers).text
        return res

    def sen_get(self,url,data =None,headers=None):
        """get请求"""
        res = requests.get(url,params =data,headers=headers).text
        return res
    def send_put(self,url,data =None,headers=None):
        """put请求"""
        res = requests.put(url=url, data=data, headers=headers).text
        return res
    def send_delete(self,url,data =None,headers=None):
        """delete请求"""
        res = requests.delete(url,data=data,headers=headers).text
        return res

    def run_man(self,method,url,data=None,headers=None):
        """执行方法，传递method、URL、data参数"""
        if method == "post":
            res = self.send_post(url,data,headers)
        elif method == "put":
            res = self.send_put(url,data,headers)
        elif method == "delete":
            res = self.send_delete(url,data,headers)
        else:
            res = self.sen_get(url,data,headers)
        try:
            res=json.loads(res)
        except:
            print('解析失败')
        return res

    def smsCode(self):
        '''通过数据库获取验证码'''
        url = "http://172.18.12.61:8901//ui/user/sendSmsCode"
        data = {"password": "123456qQ","username": "jzj319"}
        headers = {"content-type": "application/json", "charset": "UTF-8"}
        res=self.run_man('post',url,json.dumps(data),headers)
        sql = "SELECT * FROM RECEIVE_202107 WHERE USER_ID = '168' ORDER BY RECEIVE_TIME DESC"
        sql_res_data = oracle.read_oracle(sql)[0]['CONTENT']
        print(sql_res_data)
        sql_res_data = sql_res_data.split("：")[1][:6]
        # sql_res_data = {'data': sql_res_data}
        return sql_res_data

    def token(self):
        url = "http://172.18.12.61:8901/ui/user/token"
        data = {"password": "123456qQ","username": "jzj319",'smsCode':self.smsCode()}
        headers = {"content-type": "application/json", "charset": "UTF-8"}
        res = self.run_man('post',url,json.dumps(data),headers)
        print(res)
        token = res['data']
        return token




request = BaseRequest()

if __name__ == "__main__":

    # url = "http://172.18.12.61:8901/ui/user"
    #
    # data = ""
    # headers = {"content-type": "application/json", "charset": "UTF-8","Authorization":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxNjgiLCJ1c2VySWQiOjE2OCwib3JnSWQiOi0xLCJuYW1lIjoiIiwiZXhwIjoxNjI2ODc2OTI3fQ.tpVmRY-ngCp_1aqvbvWJm6ZRfy9N_OWRrOf3osk-QcsWMCdm7aRyMvRLLPJIzysCqObXlnhvgDu8Kx0KcGhiFTE5b4MWIk6we3H6-Xbn0BZknvzhOuvFX-onKOIKmZoGsIfqJ62RVFn6OnOW2-ysvkroB4OKuQUQ8EAP5VPNesQ"}
    #
    # print(request.run_man('get',url,data,headers))
    print(request.smsCode())
    print(request.token())
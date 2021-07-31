# -*- coding: utf-8 -*-
import json
import unittest,os,sys

import mock
from ddt import ddt,data
pwd = os.getcwd()
base_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)

from Base.read_excel import readExcel
from Base.read_ini import config_data
from Base.base_request import request
from Base.read_db import oracle
from Base.depend_date import get_data
from Base.read_json import get_value
from Base.log import logger

excel_data = readExcel.get_excel_data()
token = request.token()
config_url = config_data.get_value('host')
@ddt
class Test_case01(unittest.TestCase):

    @data(*excel_data)
    def test_user(self,excel_data):
        print(excel_data)
        case_id = excel_data[0]
        """获取测试用例的行号i"""
        i = readExcel.get_rows_number(case_id)
        depend = excel_data[3]
        is_run = excel_data[2]
        base_url = excel_data[5]
        url = config_url + base_url
        para_data = json.loads(excel_data[7])
        if is_run == "yes":
            """该用例是否进行执行"""
            if depend:
                """使用获取依赖的方法获取依赖数据，把数据添加到url或data中"""
                depend_data = get_data(depend)
                if excel_data[14] == "url":
                    url = url+'/'+str(depend_data)
                elif excel_data[14] == "data":
                    para_data['id']=depend_data
            headers = json.loads(excel_data[8])
            """把token添加到headers中"""
            headers['Authorization'] = token
            method = excel_data[6]
            """使用mock数据"""
            # request.run_man = mock.Mock(return_value=get_value(base_url))
            """使用run_man方法进行get/post/put/delete请求"""
            if method == "get" or method == "delete":
                res = request.run_man(method, url, para_data, headers)
            else:
                res = request.run_man(method, url, json.dumps(para_data), headers)
            print(res)
            """把接口返回的结果写入Excel中"""
            readExcel.excel_write_data(i, 13, json.dumps(res, ensure_ascii=False).encode('utf-8'))
            assert_ = excel_data[10]
            expect_msg = excel_data[9]
            """根据预期结果方式msg/code/sql结果进行断言"""
            if assert_ == "msg":
                try:
                    self.assertEqual(expect_msg,res['msg'])
                    readExcel.excel_write_data(i, 12, '成功')
                except Exception as msg:
                    logger.info(msg)
                    readExcel.excel_write_data(i, 12, '失败')
            elif assert_ == "code":
                try:
                    self.assertEqual(expect_msg,res['status'])
                    readExcel.excel_write_data(i, 12, '成功')
                except Exception as msg:
                    logger.info(msg)
                    readExcel.excel_write_data(i, 12, '失败')
            elif assert_ == "sql":
                sql_data = excel_data[4]
                try:
                    result_data = oracle.read_mysqldb(sql_data,'hsp_user')
                    self.assertEqual(para_data['username'], result_data[0]['username'])
                    """把自己后面测试用例使用到的数据可以添加到字典中，写入Excel"""
                    excel_sql_data = {"id":result_data[0]['id'],'name':result_data[0]['username']}
                    readExcel.excel_write_data(i, 12, '成功')
                    readExcel.excel_write_data(i, 14, json.dumps(excel_sql_data))
                except Exception as msg:
                    logger.info(msg)
                    readExcel.excel_write_data(i, 12, '失败')


if __name__ == "__main__":
    unittest.main()




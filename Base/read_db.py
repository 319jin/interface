import pymysql.cursors
import os,pymysql
import cx_Oracle
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'
class ReadDB():

    def read_oracle(self,sql):
        '''查询oracel的数据库'''
        conn = cx_Oracle.connect('hsp', 'hjhz123456', '172.18.0.10:1521/ORCL')
        cursor = cx_Oracle.Cursor(conn)
        cursor.execute(sql)
        result = cursor.fetchall()
        cols = [d[0] for d in cursor.description]
        a = []
        for row in result:
            b = dict(zip(cols, row))
            a.append(b)
        cursor.close()
        conn.close()
        return a

    def del_mysqldb(self,sql,name):
        '''删除MySQL数据库'''
        db = pymysql.connect(host='172.18.1.101', port=3306, user='hsp', passwd='hsp123456', db=name, charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print(cursor.rowcount,'记录删除条数')

    def read_mysqldb(self,sql,name):
        '''读取MySQL数据库'''
        db = pymysql.connect(host='172.18.1.101', port=3306, user='hsp', passwd='hsp123456', db=name, charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data



oracle = ReadDB()

if __name__ == "__main__":

    # sql = "SELECT * FROM RECEIVE_202107 WHERE USER_ID = '168' ORDER BY RECEIVE_TIME DESC"
    # print(oracle.read_oracle(sql)[0]["CONTENT"])

    sql = "SELECT * FROM hsp_user.`user` WHERE username = 'jin12345678901234567'"

    print(oracle.read_mysqldb(sql,'hsp_user'))



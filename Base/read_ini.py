import configparser
import os,sys
pwd=os.getcwd()
base_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class GitIni:

    def get_ini(self):
        "获取所有配置文件中的数据"
        file_path = base_path+'/Config/server.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8-sig")
        return cf

    def get_value(self,key,node=None):
        if node==None:
            node = 'server'
        cf = self.get_ini()
        try:
            data = cf.get(node,key)
        except Exception as e:
            print("没有获取到值")
            data = None
        return data
config_data = GitIni()

if __name__ == "__main__":

    print(GitIni().get_value("host"))
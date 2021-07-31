import os

class GetPath(object):

    def get_params_path(self, file_name):
        """
        读取参数化文件位置
        :param file_name: 参数化文件名称
        :return: 返回参数化文件的路径
        """
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        file_path = os.path.join(os.path.join(path, 'testFile'), file_name)
        return file_path

    def get_conf_path(self, file_name):
        """
        读取配置文件位置
        :param file_name: 配置文件的名称
        :return: 配置文件的路径
        """
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        file_path = os.path.join(os.path.join(path, 'config'), file_name)
        return file_path
import sys,os,json
from Base.read_excel import readExcel
from jsonpath_rw import parse

pwd = os.getcwd()
base_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)


def split_data(data):
    '''拆分单元格数据'''
    list_data = data.split(">")
    case_id = list_data[0]
    row_num = list_data[1]
    rule_data = list_data[2]
    return case_id,row_num,rule_data


def depend_data(data):
    '''获取依赖结果集'''
    case_id = split_data(data)[0]
    num = split_data(data)[1]
    row_number = readExcel.get_rows_number(case_id)
    rul_data = readExcel.get_cell_value(row_number,int(num))
    print(type(rul_data))
    return rul_data


def get_depend_data(res_data,key):
    '''获取依赖字段'''
    res_data = json.loads(res_data)
    json_exe = parse(key)
    madle = json_exe.find(res_data)
    return [math.value for math in madle][0]

def get_data(data):
    '''获取依赖数据'''
    res_data = depend_data(data)
    # print(res_data)
    rule_data = split_data(data)[2]
    return get_depend_data(res_data,rule_data)




if __name__ == "__main__":
    data = 'case_001>14>id'
    print(depend_data(data))

    # print(get_data(data))


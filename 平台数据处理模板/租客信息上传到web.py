import time
import json
import requests
import xlwings as xw
from tqdm import tqdm

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDAzMCIsImF1dGhBY2NvdW50IjoiT2liQ1BwNzNadTQ3MEtGbVg5ZFcwYWU5dHlwTDQ1SWdWMGwzQmtjR1B4eVlDNWpTSTN3aTVFejRJdHk2di9ab09ZaTJpS0s2NWZQNUZoZUxFbkZZcWlDc2VEZzFPUHUrR21xTmNsZkxuL01GWXZtK0Zvb2F0UVk4TVpYZHpTdGN5UFlBVTFSVFRTMTVkcndQZXhnVjlEamE2eEpuU0lBbFNaZENpMXB6SEFWNXJkdzBPT28vT0hScWQxSW5mS1dSIiwidHlwZSI6MSwiZXhwIjoxNjUxMjE5MjY1fQ.KolVLSmWO3nxIx6FrvJrR8ta2Yc1gwqYQbpGbvczqGc',
    'Content-Type': 'application/json',
}


# 空间编号和空间名称转换，变成{空间名称:空间编号字典}
def id_convert():
    app = xw.App(visible=True, add_book=False)
    wb = xw.Book('xxxx.xlsx')  # 租户信息或者家属信息excelb表
    sht = wb.sheets[0]
    cell = sht.used_range.last_cell
    rows = cell.row  # 获取excel总行数
    colums = cell.column  # 获取excel总列数
    total_dict = {}

    for i in range(1, rows):
        temp_list = sht.range('a{}:b{}'.format(i, i)).value  # a是空间编号，b是空间名称
        total_dict[temp_list[1]] = str(int(temp_list[0]))

    wb.close()
    app.quit()
    return total_dict

# 将【空间编码，业主手机号，业主名称】添加到列表，此函数将空间编码和空间名称转换完保存为列表
def excel_final(id_dic):
    app = xw.App(visible=True, add_book=False)
    wb = xw.Book('xxxx.xlsx')  # 租户信息或者家属信息excelb表
    sht = wb.sheets[0]
    cell = sht.used_range.last_cell
    rows = cell.row  # 获取excel总行数
    colums = cell.column  # 获取excel总列数
    total_list = []
    for i in range(1, rows+1):
        """以下代码根据项目可以调整，最后格式是【空间编码，业主手机号，业主名称】即可"""
        temp_list = sht.range('a{}:e{}'.format(i, i)).value
        temp_list[0] = "YSHY"+temp_list[0]  # 将excel默认的小数转换成字符串
        idConvert = id_dic[temp_list[0]]
        temp_list[4] = str(int(temp_list[4]))  # 将excel默认的小数转换成字符串
        total_list.append([idConvert, temp_list[4], temp_list[2]])  # 【空间编码，业主手机号，业主名称】

    wb.close()
    app.quit()
    return total_list

# 存放错误的数据的excel
def error_log(data):
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False  # 关闭一些提示信息，可以加快运行速度。 默认为 True。
    app.screen_updating = True  # 更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。
    wb = app.books.add()
    sht1 = wb.sheets.add()  # 新建工作表，默认新建的放在最前面

    sht1.range('a1').value = data

    wb.save('errorLog.xlsx')
    wb.close()
    app.quit()


if __name__ == '__main__':
    id_dic = id_convert()
    final_data = excel_final(id_dic)

    error_data = []
    for i in final_data:  # 循环家属或者租户信息
        try:
            """data是从web上查看请求获取的，根据实际情况有变动"""
            data = {"name": i[2], "contactInfo": i[1], "tags": [],
                    "list": [{"id": i[0], "roomAbb": "null", "userType": 4}],
                    "projectId": 80009}
            response = requests.post('http://group.hjt.link/hlink-saas-community/api/manage/userInfo/addUser',
                                     headers=headers,
                                     data=json.dumps(data))
            """逐个模拟请求发送请求"""
            print("成功")
        except Exception as e:
            # 如果出现错误，则
            print(e, "i", "失败")
            error_data.append(i)
        time.sleep(0.5)
    error_log(error_data)
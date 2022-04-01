import xlwings as xw


# 先读取房间和业主信息
def read_first_excel():  # 需要【楼栋，单元，房间，面积，业主，电话】信息保存到excel表里
    app = xw.App(visible=True, add_book=False)
    wb = xw.Book('xxxx.xlsx')  # 保存表的名字，根据实景情况更改
    sht = wb.sheets[0]
    cell = sht.used_range.last_cell
    rows = cell.row
    colums = cell.column
    # print(rows)
    total_list = []
    for i in range(1, rows):
        total_list.append(sht.range('a{}:f{}'.format(i, i)).value)  # 楼栋，单元，房间，面积，业主，电话
        """楼栋，单元，房间，面积，业主，电话
            每个表顺序不同，下一步再处理"""
    wb.close()
    app.quit()
    return total_list


# 获取房间编码和房间的对应关系
def get_correspondence(data):
    data_ = {}
    num = 1
    for i in data:
        if i[1].count("0") > 1:
            ceng = "{}0".format(i[1].split("00")[0])
        else:
            ceng = "{}".format(i[1].split("0")[0])
        ljmc = "{}层>".format(ceng)
        kjmc = "{}-{}".format(ceng, i[1])
        name = "xxx"
        phone = "xxx"
        data_[kjmc] = [name, phone]  # 空间编码为key，[业主名称，电话]为value 保存到字典中
        num += 1
        # print(num)
    return data_  # 返回对应的字典


# 将数据处理成能够房产信息中需要的数据格式
def excel_final(data_):
    app = xw.App(visible=True, add_book=False)
    wb = xw.Book('房产信息.xlsx')
    sht = wb.sheets[0]
    cell = sht.used_range.last_cell
    rows = cell.row
    colums = cell.column
    total_list = []
    for i in range(2, rows):
        try:
            temp_list = sht.range('a{}:e{}'.format(i, i)).value  # 获取房产信息中的 【项目,位置，房间编码，房间】信息
            temp_list.append("xxxx")  # 这里需要填写企业编号，在房产信息－＞企业信息中查找企业编号，然后添加到列表中

            nameAndphone_data = data_["xxx"]  # xxx 填写房间号码，找到对应的value【业主名称，电话】
            temp_list.extend(nameAndphone_data)  # 将业主名称，电话继续添加到列表
            # total_list.append(temp_list)
            total_list.append(temp_list)  # 将完整的信息逐条保存到最终列表
        except:  # 如果有错误就单独处理
            pass
    wb.close()
    app.quit()
    return total_list  # 此处是最终要写入excel的列表


# 将最终列表信息写入到excel里
def writeToFinal(data):
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False  # 关闭一些提示信息，可以加快运行速度。 默认为 True。
    app.screen_updating = True  # 更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。
    wb = app.books.add()
    sht1 = wb.sheets.add()  # 新建工作表，默认新建的放在最前面

    sht1.range('a1').value = data

    wb.save('房产信息数据.xlsx')  # 将房产信息数据这个excel复制到房产信息中，在web中上传即可
    wb.close()
    app.quit()


if __name__ == '__main__':
    data1 = read_first_excel()  # 先读取房间和业主信息
    data_dict = get_correspondence(data1)  # 获取房间编码和房间的对应关系
    final_data = excel_final(data_dict)  # 将数据处理成能够房产信息中需要的数据格式
    writeToFinal(final_data)  # 将最终信息写入excel
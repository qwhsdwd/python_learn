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


# 读取空间导入模板中的路径编码信息
def read_second_excel():  # 需要将空间导入模板的路径编码单独保存导excel文件中
    app = xw.App(visible=True, add_book=False)
    wb = xw.Book('工作簿2.xlsx')  # 存有路径编码的excel文件
    sht = wb.sheets[0]
    cell = sht.used_range.last_cell
    rows = cell.row
    colums = cell.column
    # print(rows)
    total_dict = {}
    for i in range(1, rows):
        a = sht.range('a{}'.format(i)).value
        b = sht.range('b{}'.format(i)).value
        total_dict[a] = b
        # a, b =
    wb.close()
    app.quit()
    return total_dict


# 最终写入空间导入模板
def writeToExcel(data1, data2):  # data1 是未处理的数据，data2是路径编码字典
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False  # 关闭一些提示信息，可以加快运行速度。 默认为 True。
    app.screen_updating = True  # 更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。
    wb = app.books.add()
    sht1 = wb.sheets.add()  # 新建工作表，默认新建的放在最前面
    num = 1
    for i in data1:
        ljmc = "xxx"  # 路径名称
        ljbm = "xxx"  # 路径编码
        kjmc = "xxx"  # 空间名称
        jzmj = "xxx"  # 建筑面积
        """根据实际数据进行处理后写入即可"""
        sht1.range('a{}'.format(num)).value = [ljmc, ljbm, "FJ", kjmc, kjmc, jzmj, "", "0", "1"]
        num += 1
        # print(num)
        print([ljmc, ljbm, "FJ", kjmc, kjmc, jzmj, "", "0"])
        # print(num)

    wb.save('空间导入模板数据.xlsx')
    wb.close()
    app.quit()


if __name__ == '__main__':
    data1 = read_first_excel()  # 获取【楼栋，单元，房间，面积，业主，电话】信息列表
    data_dict = read_second_excel()  # 获取路径编码字典
    writeToExcel(data1, data_dict)  # data1数据处理成空间导入模板要求的数据后写入空间导入模板
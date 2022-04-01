import xlwings as xw


# 读取excel文件，把数据写入到python的列表对象里
def read_excel():
    app = xw.App(visible=True, add_book=False)  # 启动xlwings模块
    wb = xw.Book('2小时假期邀请函.xlsx')  # 打开excel文件
    sht = wb.sheets['信息1']  # 按表名获取工作表

    cell = sht.used_range.last_cell  # 获取表的行和列的对象
    rows = cell.row  # 获取行数
    colums = cell.column  # 获取列数
    # print(rows)

    total_list = []
    # 从第二行开始读取（因为第一行是标题）
    for i in range(2, rows + 1):
        total_list.append(sht.range('a{}:j{}'.format(i, i)).value)
        # 每读一行都加入列表total_list
    # 关闭wb对象
    wb.close()
    # 关闭excel
    app.quit()
    # 函数返回读取的数据列表
    return total_list


# 处理数据函数
def data_processing(excel_list):
    # 创建一个新的列表对象
    new_list = []
    # 遍历列表
    for i in excel_list:
        # 如果第8个元素为None（没有数据）就忽略，如果不为None（有数据）就运行下列代码
        if i[7] is not None:
            # *关键代码，以“/n"分割字符串，为新列表
            license_plate = i[7].split("\n")
            # 举个例子 license_lpate 现在的值为[‘鲁B00000’，‘鲁B00001’，‘鲁B00002’]
            for j in license_plate:
                # 　遍历这个列表[‘鲁B00000’，‘鲁B00001’，‘鲁B00002’]
                new_list.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6], j, i[8], i[9]])
                # 添加到最终的列表
        else:
            new_list.append(i)
            # 如果车牌这个元素为None那么直接添加到最终的列表里

    # 函数返回最终的列表
    return new_list


# 将最终处理完的数据写入新的excel表里
def write_to_excel(final_list):
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False  # 关闭一些提示信息，可以加快运行速度。 默认为 True。
    app.screen_updating = True  # 更新显示工作表的内容。默认为 True。关闭它也可以提升运行速度。
    wb = app.books.add()
    sht1 = wb.sheets.add()  # 新建工作表，默认新建的放在最前面

    sht1.range('a1').value = final_list

    wb.save('2小时假期邀请函-处理后.xlsx')  # 保存到新excel的名称
    wb.close()
    app.quit()

    # 这个函数直接复制即可


if __name__ == '__main__':
    # excel_list为读取excel后的列表
    excel_list = read_excel()
    # final_list为 将读取的excel数据处理后的列表
    final_list = data_processing(excel_list)
    # 将final_list的数据直接写入新的excel
    write_to_excel(final_list)

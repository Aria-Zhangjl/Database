# 进行数据查询
# -*- coding:utf-8 -*-
import easygui as eg
import pymssql  # 引入pymssql模块

'''
server=r'...'
user=r'..'
psd=r'...'
db=r'...'
'''


def conn():
    connect = pymssql.connect(server, user, psd, db, charset="GBK")  # 服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    else:
        print('连接失败！')
    return connect

def conn2():
    connect = pymssql.connect(server, user, psd, db)  # 服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    else:
        print('连接失败！')
    return connect

# 医生信息的查询
def queryDoctor():
    con = conn()
    cursor = con.cursor()
    query1 = eg.buttonbox(msg="请选择查询功能", title="医生信息查询", choices=['医生个人信息查询', '高级查询'])
    title = query1
    if (query1 == '医生个人信息查询'):
        msg = "请输入医生的工号"
        doctorid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Doctor where dworkid like '""" + doctorid + """'"""
    else:
        msg1 = "请输入想要得到的数据信息"
        msg = "请输入sql语言"
        insertmsg1 = eg.enterbox(msg=msg, title=title)
    insertmsg1 = str(insertmsg1)
    print(insertmsg1)
    cursor.execute(insertmsg1)
    docmes = cursor.fetchall()
    con.commit()
    fieldNames = ["医生编号:      ", "身份证号:      ", "医生姓名:      ", "医生性别:      ", "医生年龄:      ", "工作医院:      ", \
                  "医院编号:      ","负责患者人数:  ", "科室:          ", "职称:          ", "学历:          ", \
                  "电话号码:      ", "家庭住址:      ","社区编号:      ", "工作时间:      "]

    res = "查询结果如下：\n\n"
    if len(docmes) == 0:
        eg.msgbox(msg="未能找到对应的信息", title="查询结果")
    else:
        print(docmes)
        if len(docmes[0])==len(fieldNames):
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] +  playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
        else:
            for i in docmes:
                print(i)
                for j in range(0,len(i)):
                    res += str(i[j]) + '\t'
                res+='\n\n'
            res+='\n\n\n'

        eg.msgbox(msg=res, title="查询结果")
    # print(docmes)


# 医院信息的查询
def queryHospital():
    con = conn()
    cursor = con.cursor()
    query1 = eg.buttonbox(msg="请选择查询功能", title="医院信息查询", choices=['医院信息查询', '高级查询'])
    title = query1
    if (query1 == '医院信息查询'):
        msg = "请输入医院编号"
        hosid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Hospital where hid like '""" + hosid + """'"""
    else:
        msg1 = "请输入想要得到的数据信息"
        msg = "请输入sql语言"
        insertmsg1 = eg.enterbox(msg=msg, title=title)
    insertmsg1 = str(insertmsg1)
    cursor.execute(insertmsg1)
    print(insertmsg1)
    docmes = cursor.fetchall()
    con.commit()
    fieldNames = ["医院编号:      ", "医院名称:      ", "医院等级:      ", "医院地址:      ", "医院工作时间:  ", "病人最大容量:  ", \
                  "医院电话:      ", "接诊人数:      ",'医生人数:      ']

    res = "查询结果如下：\n\n"
    if len(docmes) == 0:
        eg.msgbox(msg="未能找到对应的信息", title="查询结果")
    else:
        if len(docmes[0])!=len(fieldNames):
            for i in docmes:
                print(i)
                for j in range(0, len(i)):
                    res += str(i[j]) + '\t'
                res += '\n\n'
            res += '\n\n\n'
        else:
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + " " + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"

        eg.msgbox(msg=res, title="查询结果")


# 社区信息的查询
def queryComunity():
    con = conn()
    cursor = con.cursor()
    query1 = eg.buttonbox(msg="请选择查询功能", title="社区信息查询", choices=['社区信息查询', '高级查询'])
    title = query1
    if (query1 == '社区信息查询'):
        msg = "请输入社区编号"
        comid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Comunity where cid like '""" + comid + """'"""
    else:
        msg1 = "请输入想要得到的数据信息"
        msg = "请输入sql语言"
        insertmsg1 = eg.enterbox(msg=msg, title=title)
    insertmsg1 = str(insertmsg1)
    print(insertmsg1)
    cursor.execute(insertmsg1)
    docmes = cursor.fetchall()
    con.commit()
    fieldNames = ["社区编号:      ", "社区名称:      ", "居住人数:      ","社区地址:      ", "隔离人数:      ", "医生人数:      ", "社区电话:      ", \
                  "物业工作时间:  ", "居委工作时间:  "]

    res = "查询结果如下：\n\n"
    if len(docmes) == 0:
        eg.msgbox(msg="未能找到对应的信息", title="查询结果")
    else:
        if len(docmes[0])==len(fieldNames):
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k]  + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
        else:
            for i in docmes:
                print(i)
                for j in range(0, len(i)):
                    res += str(i[j]) + '\t'
                res += '\n'
            res += '\n\n\n'

        eg.msgbox(msg=res, title="查询结果")


# 酒店信息的查询
def queryHotel():
    con = conn()
    cursor = con.cursor()
    query1 = eg.buttonbox(msg="请选择查询功能", title="酒店信息查询", choices=['酒店信息查询', '高级查询'])
    title = query1
    if (query1 == '酒店信息查询'):
        msg = "请输入酒店编号"
        hotid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Hotel where hotel_id like '""" + hotid + """'"""
    else:
        msg1 = "请输入想要得到的数据信息"
        msg = "请输入sql语言"
        insertmsg1 = eg.enterbox(msg=msg, title=title)
    insertmsg1 = str(insertmsg1)
    print(insertmsg1)
    cursor.execute(insertmsg1)
    docmes = cursor.fetchall()
    con.commit()
    fieldNames = ["酒店编号:    ", "酒店名称:    ", "酒店星级:    ", "酒店地址:    ", "住房价格:    ", "入住人数:    ", \
                  "隔离人数:    ", "客房总数:    ", "酒店电话:    "]

    res = ""
    if len(docmes) == 0:
        eg.msgbox(msg="未能找到对应的信息", title="查询结果")
    else:
        if len(docmes[0])==len(fieldNames):
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
        else:
            for i in docmes:
                print(i)
                for j in range(0, len(i)):
                    res += str(i[j]) + '\t'
                res += '\n\n'
            res += '\n\n\n'

        eg.msgbox(msg=res, title="查询结果")


# 患者信息的查询
def queryPatient():
    con = conn()
    cursor = con.cursor()
    query1 = eg.buttonbox(msg="请选择查询功能", title="患者信息查询", choices=['患者个人信息查询', '高级查询'])
    title = query1
    if (query1 == '患者个人信息查询'):
        msg = "请输入患者身份证号"
        pid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Patient where pid like '""" + pid + """'"""
    else:
        msg1 = "请输入想要得到的数据信息"
        msg = "请输入sql语言"
        insertmsg1 = eg.enterbox(msg=msg, title=title)
    insertmsg1 = str(insertmsg1)
    print(insertmsg1)
    cursor.execute(insertmsg1)
    docmes = cursor.fetchall()
    con.commit()
    fieldNames = ["身份证号:    ", "患者姓名:    ", "患者性别:    ", "患者年龄:    ", "患者地址:    ", "社区编号:    ","患者症状:    ", "近期日程:    ", \
                  "就诊医院:    ","医院编号:    ", "主治医生:    ", "医生工号:    ","入院时间:    ", "出院时间:    ", "隔离状态:    ", "工作单位:    "]

    res = ""
    if len(docmes) == 0:
        eg.msgbox(msg="未能找到对应的信息", title="查询结果")
    else:
        if len(docmes[0])==len(fieldNames):
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k]+ playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
        else:
            for i in docmes:
                print(i)
                for j in range(0, len(i)):
                    res += str(i[j]) + '\t'
                res += '\n\n'
            res += '\n\n\n'

        eg.msgbox(msg=res, title="查询结果")


# 密集接触者的查询
def queryContact():
    con = conn()
    cursor = con.cursor()
    query1 = eg.buttonbox(msg="请选择查询功能", title="密集接触者信息查询", choices=['密集接触者信息查询', '高级查询'])
    title = query1
    if (query1 == '密集接触者信息查询'):
        msg = "请输入密集接触者身份证号"
        conid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Contact_People where contact_id like '""" + conid + """'"""
    else:
        msg1 = "请输入想要得到的数据信息"
        msg = "请输入sql语言"
        insertmsg1 = eg.enterbox(msg=msg, title=title)
    insertmsg1 = str(insertmsg1)
    print(insertmsg1)
    cursor.execute(insertmsg1)
    docmes = cursor.fetchall()
    con.commit()
    fieldNames = ["身份证号:        ", "姓名:            ", "性别:            ", "年龄:            ", "居住社区:        ","社区编号:        ", \
                  "症状:            ", "隔离地点:        ", "酒店编号:        ","接触源:          ","接触者身份证号:  ", "隔离时长:        ", "工作单位:        "]

    res = "查询结果如下：\n"
    if len(docmes) == 0:
        eg.msgbox(msg="未能找到对应的信息", title="查询结果")
    else:
        if len(docmes[0])==len(fieldNames):
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
        else:
            for i in docmes:
                print(i)
                for j in range(0, len(i)):
                    res += str(i[j]) + '\t'
                res += '\n\n'
            res += '\n\n\n'

        eg.msgbox(msg=res, title="查询结果")


if __name__ == '__main__':
    while 1:
        queryContact()

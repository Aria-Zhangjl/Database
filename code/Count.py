# 进行数据统计
# -*- coding:utf-8 -*-

import easygui as eg
import pymssql #引入pymssql模块
import re
'''
server=r'...'
user=r'..'
psd=r'...'
db=r'...'
'''

def conn():
    connect = pymssql.connect(server,user,psd,db ,charset="GBK")#服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    else:
        print('连接失败！')
    return connect

def conn2():
    connect = pymssql.connect(server,user,psd,db)#服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    else:
        print('连接失败！')
    return connect

#普通统计：患者信息统计
def countpatient():
    con=conn()
    cursor=con.cursor()
    #年龄层
    sql=[]
    sql.append("""select count(*) from Patient where page < 18""")
    sql.append("""select count(*) from Patient where page >= 18 and page <48""")
    sql.append( """select count(*) from Patient where page >= 48 and page < 68""")
    sql.append("""select count(*) from Patient where page >= 68""")
    ages=["18岁以下: ","18-48岁:  ","28-68岁:  ","68岁以上: "]
    res1=""
    for i in range(0,4):
        cursor.execute(sql[i])
        res=cursor.fetchone()
        res=str(res)
        res=re.sub("\D","",res)
        con.commit()
        res1+=ages[i]+res+"人\n"
    eg.buttonbox(msg=res1,title="患者年龄统计",choices=['下一步'])
    #性别
    con=conn2()
    cursor=con.cursor()
    sql2=[]
    sql2.append("""select count(*) from Patient where psex = '女'""")
    sql2.append("""select count(*) from Patient where psex like '男'""")
    sex=["男性：","女性："]
    res2=""
    for i in range(0,2):
        cursor.execute(sql2[i])
        res=cursor.fetchone()
        res=str(res)
        res = re.sub("\D", "", res)
        con.commit()
        res2+=sex[i]+res+"人\n"
    eg.buttonbox(msg=res2,title="患者性别统计",choices=['返回'])




def countcontact():
    con = conn()
    cursor = con.cursor()
    # 年龄层
    sql = []
    sql.append("""select count(*) from Contact_People where contact_age < 18""")
    sql.append("""select count(*) from Contact_People where contact_age >= 18 and contact_age <48""")
    sql.append("""select count(*) from Contact_People where contact_age >= 48 and contact_age < 68""")
    sql.append("""select count(*) from Contact_People where contact_age >= 68""")
    ages = ["18岁以下: ", "18-48岁:  ", "28-68岁:  ", "68岁以上: "]
    res1 = ""
    for i in range(0, 4):
        cursor.execute(sql[i])
        res = cursor.fetchone()
        res = str(res)
        res = re.sub("\D", "", res)
        con.commit()
        res1 += ages[i] + res + "人\n"
    eg.buttonbox(msg=res1, title="密集接触者年龄统计",choices=['下一步'])
    # 性别
    con = conn2()
    cursor = con.cursor()
    sql2 = []
    sql2.append("""select count(*) from Contact_People where contact_sex = '女'""")
    sql2.append("""select count(*) from Contact_People where contact_sex like '男'""")
    sex = ["男性：", "女性："]
    res2 = ""
    for i in range(0, 2):
        cursor.execute(sql2[i])
        res = cursor.fetchone()
        res = str(res)
        res = re.sub("\D", "", res)
        con.commit()
        res2 += sex[i] + res + "人\n"
    eg.buttonbox(msg=res2, title="密集接触者性别统计",choices=['返回'])

def countdoctor():
    con = conn()
    cursor = con.cursor()
    # 年龄层
    sql = []
    sql.append("""select count(*) from Doctor where dage < 18""")
    sql.append("""select count(*) from Doctor where dage >= 18 and dage <48""")
    sql.append("""select count(*) from Doctor where dage >= 48 and dage < 68""")
    sql.append("""select count(*) from Doctor where dage >= 68""")
    ages = ["18岁以下: ", "18-48岁:  ", "28-68岁:  ", "68岁以上: "]
    res1 = ""
    for i in range(0, 4):
        cursor.execute(sql[i])
        res = cursor.fetchone()
        res = str(res)
        res = re.sub("\D", "", res)
        con.commit()
        res1 += ages[i] + res + "人\n"
    eg.buttonbox(msg=res1, title="医生年龄统计",choices=['下一步'])
    # 性别
    con = conn2()
    cursor = con.cursor()
    sql2 = []
    sql2.append("""select count(*) from Doctor where dsex = '女'""")
    sql2.append("""select count(*) from Doctor where dsex like '男'""")
    sex = ["男性：", "女性："]
    res2 = ""
    for i in range(0, 2):
        print(sql2[i])
        cursor.execute(sql2[i])
        res = cursor.fetchone()
        res = str(res)
        res = re.sub("\D", "", res)
        con.commit()
        res2 += sex[i] + res + "人\n"
    eg.buttonbox(msg=res2, title="医生性别统计",choices=['返回'])

#统计非安全小区
def Countsafecom():
    con=conn()
    cursor=con.cursor()
    sql="""select cname from Comunity where cdepartpeople > 0"""
    cursor.execute(sql)
    commes=cursor.fetchall()
    con.commit()
    res=[]
    for i in commes:
        res.append(str(i[0]).rstrip())
    msg="目前已发现有患者的小区有：\n"+res[0]
    for i in range(1,len(res)):
        msg+="、 "+res[i]
    msg+='\n\n'
    sql="""select count(*) from Patient"""
    cursor.execute(sql)
    patsum=cursor.fetchone()
    patsum = str(patsum)
    patsum = re.sub("\D", "", patsum)
    con.commit()
    msg+="目前共有患者"+patsum+"名。\n"
    sql="""select count(*) from Contact_People"""
    cursor.execute(sql)
    consum=cursor.fetchone()
    consum = str(consum)
    consum = re.sub("\D", "", consum)
    con.commit()
    msg+="目前共有正在隔离的密集接触者"+consum+"名。\n\n"
    eg.buttonbox(msg=msg,title="当前数据统计",choices=['下一步'])


def Countbyself():
    con = conn()
    cursor = con.cursor()
    msg="请输入相关语句"
    title="数据统计"
    sql=eg.enterbox(msg=msg,title=title)
    sql=str(sql)
    cursor.execute(sql)
    docmes = cursor.fetchall()
    con.commit()
    res="统计结果如下：\n"
    for i in docmes:
        print(i)
        for j in range(0, len(i)):
            res += str(i[j]) + '\t'
        res += '\n\n'
    res += '\n\n\n'
    eg.msgbox(msg=res,title="查询结果")

if __name__ == '__main__':
    while 1:
        Countbyself()
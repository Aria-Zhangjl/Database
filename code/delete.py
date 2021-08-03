
# -*- coding:utf-8 -*-
import easygui as eg
import pymssql #引入pymssql模块

'''
server=r'...'
user=r'..'
psd=r'...'
db=r'...'
'''

def conn():
    connect = pymssql.connect(server,user,psd,db,charset="GBK" ) #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    else:
        print('连接失败！')
    return connect

def deleteTab():
    con=conn()
    cursor=con.cursor()
    conid = eg.enterbox("请输入要删除密集接触者的身份证号", title="密集接触者数据删除")
    insertmsg1 = """delete from Contact_People where contact_id like '""" + conid + """'"""
    which=eg.buttonbox(msg="确认删除该数据?",choices=['确认','重新输入'])
    while which=='重新输入':
        conid = eg.enterbox("请输入要删除密集接触者的身份证号", title="密集接触者数据删除")
        insertmsg1 = """delete from Contact_People where contact_id like '""" + conid + """'"""
        which = eg.buttonbox(msg="确认删除该数据?", choices=['确认', '重新输入'])
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="删除成功", choices=['返回'])


if __name__ == '__main__':
    while 1:
        deleteTab()


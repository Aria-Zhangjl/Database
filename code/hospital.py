import easygui as eg
import pymssql #引入pymssql模块

'''
server=r'...'
user=r'..'
psd=r'...'
db=r'...'
'''

def conn():
    connect = pymssql.connect(server,user,psd,db ) #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    else:
        print('连接失败！')
    return connect

#医院添加医生信息
def hospitalinsert_doctor():
    con=conn()
    cursor=con.cursor()
    title="医生信息输入"
    msg="请输入医生的信息"
    fieldNames=["医生编号","医生身份证号","医生姓名","医生性别","医生年龄","工作医院","负责患者人数","科室","职称","学历","电话号码","家庭住址","工作时间"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Hotel(hotel_id,hotel_name,hotel_rank,hotel_address,hotel_price,hotel_people,hotel_departpeople,hotel_capacity,hotel_tel) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"','"+fieldValus[2]+"','"+fieldValus[3]+"','"+ \
              fieldValus[4] + "'," +fieldValus[5]+","+fieldValus[6]+",'"+fieldValus[7]+"','"+fieldValus[8]+"')"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])

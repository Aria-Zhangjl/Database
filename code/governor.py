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

#政府添加医院的信息
def ginsert_hos():
    con=conn()
    cursor=con.cursor()
    title="医院信息输入"
    msg="请输入医院的信息"
    fieldNames=["医院编号","医院名称","医院等级","医院地址","医院工作时间","病人最大容量","医院电话","接诊人数"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Hospital(hid,hname,hrank,haddress,hworktime,hcapacity,htel,hpatient) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"','"+fieldValus[2]+"','"+fieldValus[3]+"','"+ \
              fieldValus[4] + "'," +fieldValus[5]+",'"+fieldValus[6]+"',"+fieldValus[7]+")"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    #cursor.execute("INSERT INTO Hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",('2', '中文', '1', '1', '11', '1', '1', '1'))
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])



#政府添加酒店的信息
def ginsert_hotel():
    con=conn()
    cursor=con.cursor()
    title="隔离酒店信息输入"
    msg="请输入酒店的信息"
    fieldNames=["酒店编号","酒店名称","酒店星级","酒店地址","住房价格","入住人数","隔离人数","客房总数","酒店电话"]
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

#添加社区信息
def ginsert_comunity():
    con=conn()
    cursor=con.cursor()
    title="社区信息输入"
    msg="请输入社区的信息"
    fieldNames=["社区编号","社区名称","社区地址","隔离人数","医生人数","社区电话","物业工作时间","居委工作时间"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Comunity (cid,cname,caddress,cdepartpeople,cdoctor,ctel,cestate_worktime,cRC_worktime) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"','"+fieldValus[2]+"',"+fieldValus[3]+","+ \
              fieldValus[4] + ",'" +fieldValus[5]+"','"+fieldValus[6]+"','"+fieldValus[7]+"')"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])


#添加患者信息

#添加密集接触者的信息


#查询患者信息


#查询隔离人的信息

#查询医生的信息
if __name__ == '__main__':
    while 1:
        ginsert_hotel()
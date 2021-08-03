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

#添加医院的信息
def insert_hos():
    con=conn()
    cursor=con.cursor()
    title="医院信息输入"
    msg="请输入医院的信息"
    fieldNames=["医院编号","医院名称","医院等级","医院地址","医院工作时间","病人最大容量","医院电话","接诊人数","医生人数"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Hospital(hid,hname,hrank,haddress,hworktime,hcapacity,htel,hpatient,hdoctor) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"','"+fieldValus[2]+"','"+fieldValus[3]+"','"+ \
              fieldValus[4] + "'," +fieldValus[5]+",'"+fieldValus[6]+"',"+fieldValus[7]+","+fieldValus[8]+")"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    #cursor.execute("INSERT INTO Hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",('2', '中文', '1', '1', '11', '1', '1', '1'))
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])



#政府添加酒店的信息
def insert_hotel():
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
def insert_comunity():
    con=conn()
    cursor=con.cursor()
    title="社区信息输入"
    msg="请输入社区的信息"
    fieldNames=["社区编号","社区名称","居住人数","社区地址","隔离人数","医生人数","社区电话","物业工作时间","居委工作时间"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Comunity (cid,cname,cpeople,caddress,cdepartpeople,cdoctor,ctel,cestate_worktime,cRC_worktime) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"',"+fieldValus[2]+",'"+fieldValus[3]+"',"+fieldValus[4]+","+ \
              fieldValus[5] + ",'" +fieldValus[6]+"','"+fieldValus[7]+"','"+fieldValus[8]+"')"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])


#添加患者信息
def insert_patient():
    con=conn()
    cursor=con.cursor()
    title="患者信息输入"
    msg="请输入患者的信息"
    fieldNames=["患者身份证号","患者姓名","患者性别","患者年龄","患者地址","患者地址编号","患者症状","近期日程","就诊医院",\
                "医院编号","主治医生","医生工号","入院时间","出院时间","隔离状态","工作单位"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Patient (pid,pname,psex,page,pcomunity,pcomunityid,psympton,pdate,phospital,\
    phospitalid,pdoctorname,pdoctorid,pinhos,pouthos,papart,pworkplace) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"','"+fieldValus[2]+"',"+fieldValus[3]+",'"+ \
              fieldValus[4] + "','" +fieldValus[5]+"','"+fieldValus[6]+"','"+fieldValus[7]+"','"+fieldValus[8]\
               +"','"+fieldValus[9]+"','"+fieldValus[10] +"','" + fieldValus[11]+"','"+fieldValus[12]+"','"+fieldValus[13]\
            +"','"+fieldValus[14]+"','"+fieldValus[15]+"')"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])


#添加密集接触者的信息
def insert_contact():
    con=conn()
    cursor=con.cursor()
    title="密集接触者信息输入"
    msg="请输入密集接触者的信息"
    fieldNames=["身份证号","姓名","性别","年龄","居住社区","社区编号","症状","隔离酒店","酒店编号","接触源","接触人身份证号","隔离时长","工作单位"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Contact_People (contact_id,contact_name,contact_sex,contact_age,contact_comunity,contact_comunityid,contact_sympton,contact_depadd,contact_depaddid,contact_people,contact_peopleid,depart_time,contact_workplace) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"','"+fieldValus[2]+"',"+fieldValus[3]+",'"+ \
              fieldValus[4] + "','" +fieldValus[5]+"','"+fieldValus[6]+"','"+fieldValus[7]+"','"+fieldValus[8]\
               +"','"+fieldValus[9]+"','"+fieldValus[10]+"','"+fieldValus[11]+"','"+fieldValus[12]+"')"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])

#添加医生的信息
def insert_doctor():
    con=conn()
    cursor=con.cursor()
    title="医生信息输入"
    msg="请输入医生的信息"
    fieldNames=["医生编号","医生身份证号","医生姓名","医生性别","医生年龄","工作医院","医院编号","负责患者人数","科室","职称","学历","电话号码",\
                "家庭住址","社区编号","工作时间"]
    fieldValus=eg.multenterbox(msg,title,fieldNames)
    fieldValus=tuple(fieldValus)
    insertmsg1= """INSERT INTO Doctor (dworkid,did,dname,dsex,dage,dhospital,dhospitalid,dpatients,ddepartment,dtitle,deducation,dtel,daddress,daddressid,dworktime) values """
    insertmsg2="('"+fieldValus[0]+"','"+fieldValus[1]+"','"+fieldValus[2]+"','"+fieldValus[3]+"',"+ \
              fieldValus[4] + ",'" +fieldValus[5]+"','"+fieldValus[6]+"',"+fieldValus[7]+",'"+fieldValus[8]+"','"+fieldValus[9]\
               +"','"+fieldValus[10]+"','"+fieldValus[11] +"','" + fieldValus[12]+"','"+fieldValus[13]+"','"+fieldValus[14]+"')"
    insertmsg1=insertmsg1+insertmsg2
    print(insertmsg1)
    cursor.execute(insertmsg1)
    con.commit()
    eg.buttonbox(msg="添加成功",choices=['返回'])

if __name__ == '__main__':
    while 1:
        insert_comunity()
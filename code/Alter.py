#修改数据
#-*- coding:utf-8 -*-
import easygui as eg
import pymssql #引入pymssql模块

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

#医生信息修改
def AlterDoctor():
    con = conn()
    cursor = con.cursor()
    which=eg.buttonbox(msg="请选择修改对象",title="医生信息修改",choices=['工号输入修改','自定义修改'])
    if which=='工号输入修改':
        msg = "请输入医生的工号"
        title = "医生信息修改"
        doctorid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Doctor where dworkid like '""" + doctorid + """'"""
        insertmsg1 = str(insertmsg1)
        cursor.execute(insertmsg1)
        docmes = cursor.fetchall()
        con.commit()
        fieldNames = ["医生编号:      ", "身份证号:      ", "医生姓名:      ", "医生性别:      ", "医生年龄:      ", "工作医院:      ", \
                      "医院编号:      ", "负责患者人数:  ", "科室:          ", "职称:          ", "学历:          ", \
                      "电话号码:      ", "家庭住址:      ", "社区编号:      ", "工作时间:      "]

        res = "查询数据如下：\n\n"
        if len(docmes) == 0:
            eg.msgbox(msg="未能找到对应的信息", title="查询结果")
        else:
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    # print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
            con.close()
            con2 = conn2()
            cursor = con2.cursor()
            docNames2 = ["修改项", "数据"]
            fieldValues = eg.multenterbox(msg=res, title="医生信息修改", fields=docNames2)
            Doctordict = {'医生编号': 'dworkid', '医生身份证号': 'did', '医生姓名': 'dname', '医生性别': 'dsex', '医生年龄': 'dage', \
                          '工作医院': 'dhospital', '负责患者人数': 'dpatients', '科室': 'ddepartment', '职称': 'dtitle',
                          '学历': 'deducation', \
                          '电话号码': 'dtel', '家庭住址': 'daddress', '工作时间': 'dworktime'}
            fieldValues = tuple(fieldValues)
            print(fieldValues)
            sql = """update Doctor set """ + Doctordict[fieldValues[0]] + """ = '""" + fieldValues[1] + \
                  """' where dworkid like '""" + str(doctorid) + """'"""
            print(sql)
            cursor.execute(sql)
            con2.commit()
            if Doctordict[fieldValues[0]]=='dhospital':
                sql="""select hid from hospital where hname like '"""+fieldValues[1]+"""'"""
                print(sql)
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                print(res)
                sql="""update Doctor set dhospitalid = '""" + str(res[0]) + """' where dworkid like '""" + str(doctorid) + """'"""
                cursor.execute(sql)
                con2.commit()
            if Doctordict[fieldValues[0]]=='daddress':
                sql = """select cid from Comunity where cname like '""" + fieldValues[1] + """'"""
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                sql = """update Doctor set daddressid = '""" + str(res[0]) + """' where dworkid like '""" + str(
                    doctorid) + """'"""
                cursor.execute(sql)
                con2.commit()
            eg.msgbox(msg="修改成功！")
    else:
        Updatefree()


#医院信息修改
def AlterHospital():
    con=conn()
    cursor=con.cursor()
    which=eg.buttonbox(msg="请选择修改对象",title="医院信息修改",choices=['输入编号修改','自定义修改'])
    if which=='输入编号修改':
        msg = "请输入医院的编号"
        title = "医院信息修改"
        hosid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Hospital where hid like '""" + hosid + """'"""
        insertmsg1 = str(insertmsg1)
        cursor.execute(insertmsg1)
        docmes = cursor.fetchall()
        con.commit()
        fieldNames = ["医院编号", "医院名称", "医院等级", "医院地址", "医院工作时间", "病人最大容量", \
                      "医院电话", "接诊人数", "医生人数"]

        res = ""
        if len(docmes) == 0:
            eg.msgbox(msg="未能找到对应的信息", title="查询结果")
        else:
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + "    " + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
            con.close()
            con2 = conn2()
            cursor = con2.cursor()
            docNames2 = ["修改项", "数据"]
            fieldValues = eg.multenterbox(msg=res, title="医院信息修改", fields=docNames2)
            Doctordict = {'医院编号': 'hid', '医院名称': 'hname', '医院等级': 'hrank', '医院地址': 'haddress', \
                          '医院工作时间': 'hworktime', '病人最大容量': 'hcapacity', '医院电话': 'htel', '接诊人数': 'hpatient',
                          '医院医生': 'hdoctor'}
            fieldValues = tuple(fieldValues)
            print(fieldValues)
            sql = """update Hospital set """ + Doctordict[fieldValues[0]] + """ = '""" + fieldValues[1] + \
                  """' where hid like '""" + str(hosid) + """'"""
            print(sql)
            cursor.execute(sql)
            con2.commit()
            eg.msgbox(msg="修改成功！")
    else:
        Updatefree()

#患者信息修改
def AlterPatient():
    con=conn()
    cursor=con.cursor()
    which=eg.buttonbox(msg="请选择修改对象",title="患者信息修改",choices=['输入身份证修改','自定义修改'])
    if which=='输入身份证修改':
        msg = "请输入患者的身份证号"
        title = "患者信息修改"
        pid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Patient where pid like '""" + pid + """'"""
        insertmsg1 = str(insertmsg1)
        cursor.execute(insertmsg1)
        docmes = cursor.fetchall()
        con.commit()
        fieldNames = ["身份证号:    ", "患者姓名:    ", "患者性别:    ", "患者年龄:    ", "患者地址:    ", "社区编号:    ", "患者症状:    ","近期日程:    ",\
                      "就诊医院:    ", "医院编号:    ", "主治医生:    ", "医生工号:    ", "入院时间:    ", "出院时间:    ", "隔离状态:    ","工作单位:    "]

        res = ""
        if len(docmes) == 0:
            eg.msgbox(msg="未能找到对应的信息", title="查询结果")
        else:
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
            con.close()
            con2 = conn2()
            cursor = con2.cursor()
            docNames2 = ["修改项", "数据"]
            fieldValues = eg.multenterbox(msg=res, title="患者信息修改", fields=docNames2)
            Doctordict = {'患者身份证号': 'pid', '患者姓名': 'pname', '患者性别': 'psex', '患者年龄': 'page', \
                          '患者地址': 'pcomunity', '患者症状': 'psympton', '近期日程': 'pdate', '就诊医院': 'phospital', \
                          '主治医生': 'pdoctorname', '入院时间': 'pinhos', '出院时间': 'pouthos', '隔离状态': 'papart', \
                          '工作单位': 'pworkplace'}
            fieldValues = tuple(fieldValues)
            print(fieldValues)
            sql = """update Patient set """ + Doctordict[fieldValues[0]] + """ = '""" + fieldValues[1] + \
                  """' where pid like '""" + str(pid) + """'"""
            cursor.execute(sql)
            print(sql)
            con2.commit()
            if Doctordict[fieldValues[0]] == 'pcomunity':
                sql = """select cid from Comunity where cname like '""" + fieldValues[1] + """'"""
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                sql = """update Patient set pcomunityid = '""" + str(res[0]) + """' where pid like '""" + str(
                    pid) + """'"""
                cursor.execute(sql)
                con2.commit()
            if Doctordict[fieldValues[0]] == 'phospital':
                sql = """select hid from Hospital where hname like '""" + fieldValues[1] + """'"""
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                sql = """update Patient set phospitalid = '""" + str(res[0]) + """' where pid like '""" + str(
                    pid) + """'"""
                print(sql)
                cursor.execute(sql)
                con2.commit()
            if Doctordict[fieldValues[0]] == 'pdoctorname':
                sql = """select dworkid from Doctor where dname like '""" + fieldValues[1] + """'"""
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                sql = """update Patient set pdoctorid = '""" + str(res[0]) + """' where pid like '""" + str(
                    pid) + """'"""
                cursor.execute(sql)
                con2.commit()
            eg.msgbox(msg="修改成功！")
    else:
        Updatefree()

#密集接触者信息修改
def AlterContact():
    con=conn()
    cursor=con.cursor()
    which=eg.buttonbox(msg="请选择修改对象",title="密集接触者信息修改",choices=['输入身份证修改','自定义修改'])
    if which=='输入身份证修改':
        msg = "请输入密集接触者的身份证号"
        title = "密集接触者信息修改"
        conid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Contact_People where contact_id like '""" + conid + """'"""
        insertmsg1 = str(insertmsg1)
        cursor.execute(insertmsg1)
        docmes = cursor.fetchall()
        con.commit()
        fieldNames = ["身份证号:   ", "姓名:            ", "性别:            ", "年龄:            ", "居住社区:   ","社区编号:   ", \
                      "症状:            ", "隔离地点:   ", "酒店编号:   ", "接触源:       ", "接触者身份证号:  ","隔离时长:    ", "工作单位:   "]

        res = ""
        if len(docmes) == 0:
            eg.msgbox(msg="未能找到对应的信息", title="查询结果")
        else:
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += fieldNames[k] + playmes[fieldNames[k]]
                    res += ("\n")
                res += "\n\n\n"
            con.close()
            con2 = conn2()
            cursor = con2.cursor()
            docNames2 = ["修改项", "数据"]
            fieldValues = eg.multenterbox(msg=res, title="密集接触者信息修改", fields=docNames2)
            Doctordict = {'身份证号': 'contact_id', '姓名': 'contact_name', '性别': 'contact_sex', '年龄': 'contact_age', \
                          '居住社区': 'contact_comunity', '症状': 'contact_sympton', '隔离地点': 'contact_depadd', \
                          '接触源': 'contact_people', '隔离时长': 'depart_time', '工作单位': 'contact_workplace'}
            fieldValues = tuple(fieldValues)

            print(fieldValues)
            sql = """update Contact_People set """ + Doctordict[fieldValues[0]] + """ = '""" + fieldValues[1] + \
                  """' where contact_id like '""" + str(conid) + """'"""
            print(sql)
            cursor.execute(sql)
            con2.commit()
            if Doctordict[fieldValues[0]] == 'contact_comunity':
                sql = """select cid from Comunity where cname like '""" + fieldValues[1] + """'"""
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                sql = """update Contact_People set contact_comunityid = '""" + str(res[0]) + """' where contact_id like '""" + str(
                    conid) + """'"""
                cursor.execute(sql)
                con2.commit()
            if Doctordict[fieldValues[0]] == 'contact_depadd':
                sql = """select hotel_id from Hotel where hotel_name like '""" + fieldValues[1] + """'"""
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                sql = """update Contact_People set contact_depaddid = '""" + str(res[0]) + """' where contact_id like '""" + str(
                    conid) + """'"""
                cursor.execute(sql)
                con2.commit()
            if Doctordict[fieldValues[0]] == 'contact_people':
                sql = """select pid from Patient where pname like '""" + fieldValues[1] + """'"""
                cursor.execute(sql)
                res = cursor.fetchone()
                con2.commit()
                sql = """update Contact_People set contact_peopleid = '""" + str(res[0]) + """' where contact_id like '""" + str(
                    conid) + """'"""
                cursor.execute(sql)
                con2.commit()
            eg.msgbox(msg="修改成功！")

    else:
        Updatefree()


#社区信息修改
def AlterComunity():
    con=conn()
    cursor=con.cursor()
    which=eg.buttonbox(msg="请选择修改对象",title="社区信息修改",choices=['输入社区编号修改','自定义修改'])
    if which=='输入社区编号修改':
        msg = "请输入社区的编号"
        title = "社区信息修改"
        comid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Comunity where cid like '""" + comid + """'"""
        insertmsg1 = str(insertmsg1)
        cursor.execute(insertmsg1)
        docmes = cursor.fetchall()
        con.commit()
        fieldNames = ["社区编号", "社区名称", "居住人数","社区地址", "隔离人数", "医生人数", "社区电话", "物业工作时间", "居委工作时间"]

        res = ""
        if len(docmes) == 0:
            eg.msgbox(msg="未能找到对应的信息", title="查询结果")
        else:
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + "    " + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
            con.close()
            con2 = conn2()
            cursor = con2.cursor()
            docNames2 = ["修改项", "数据"]
            fieldValues = eg.multenterbox(msg=res, title="密集接触者信息修改", fields=docNames2)
            Doctordict = {'社区编号': 'cid', '社区名称': 'cname', '社区地址': 'caddress', '隔离人数': 'cdepartpeople', \
                          '医生人数': 'cdoctor', '社区电话': 'ctel', '物业工作时间': 'cestate_worktime', '居委工作时间': 'cRC_worktime'}
            fieldValues = tuple(fieldValues)

            print(fieldValues)
            sql = """update Comunity set """ + Doctordict[fieldValues[0]] + """ = '""" + fieldValues[1] + \
                  """' where cid like '""" + str(comid) + """'"""
            print(sql)
            cursor.execute(sql)
            con2.commit()
            eg.msgbox(msg="修改成功！")
    else:
        Updatefree()

#酒店信息修改
def AlterHotel():
    con=conn()
    cursor=con.cursor()
    which=eg.buttonbox(msg="请选择修改对象",title="酒店信息修改",choices=['输入酒店编号修改','自定义修改'])
    if which=='输入酒店编号修改':
        msg = "请输入酒店的编号"
        title = "酒店信息修改"
        hotid = eg.enterbox(msg=msg, title=title)
        insertmsg1 = """select * from Hotel where hotel_id like '""" + hotid + """'"""
        insertmsg1 = str(insertmsg1)
        cursor.execute(insertmsg1)
        docmes = cursor.fetchall()
        con.commit()
        fieldNames = ["酒店编号", "酒店名称", "酒店星级", "酒店地址", "住房价格", "入住人数", "隔离人数", "客房总数", "酒店电话"]

        res = ""
        if len(docmes) == 0:
            eg.msgbox(msg="未能找到对应的信息", title="查询结果")
        else:
            for i in docmes:
                playmes = {}
                for j in range(0, len(fieldNames)):
                    playmes[fieldNames[j]] = str(i[j])
                    print(playmes[fieldNames[j]])
                for k in range(0, len(fieldNames)):
                    res += (fieldNames[k] + "    " + playmes[fieldNames[k]])
                    res += ("\n")
                res += "\n\n\n"
            con.close()
            con2 = conn2()
            cursor = con2.cursor()
            docNames2 = ["修改项", "数据"]
            fieldValues = eg.multenterbox(msg=res, title="酒店信息修改", fields=docNames2)
            Doctordict = {'酒店编号': 'hotel_id', '酒店名称': 'hotel_name', '酒店星级': 'hotel_rank', '酒店地址': 'hotel_address', \
                          '住房价格': 'hotel_price', '入住人数': 'hotel_people', '隔离人数': 'hotel_departpeople', \
                          '客房总数': 'hotel_capacity', '酒店电话': 'hotel_tel'}
            fieldValues = tuple(fieldValues)

            print(fieldValues)
            sql = """update Hotel set """ + Doctordict[fieldValues[0]] + """ = '""" + fieldValues[1] + \
                  """' where hotel_id like '""" + str(hotid) + """'"""
            print(sql)
            cursor.execute(sql)
            con2.commit()
            eg.msgbox(msg="修改成功！")
    else:
        Updatefree()

def Updatefree():
    con=conn()
    cursor=con.cursor()
    msg="请输入要修改的sql语言"
    sql=eg.enterbox(msg=msg,title="自定义修改")
    sql=str(sql)
    cursor.execute(sql)
    con.commit()
    eg.msgbox(msg="修改成功！",title="自定义修改")





if __name__ == '__main__':
    while 1:
        AlterContact()
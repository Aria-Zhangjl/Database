#建立表格

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

def creat(connect):
    cursor=connect.cursor()

    #建立医院信息表
    '''
    hid--医院编号
    hname--医院
    hrank--医院等级
    haddress--医院地址
    hworktime--医院工作时间
    hcapacity--病人最大容量
    htel--医院电话
    hpatient--接诊人数
    hdoctor--医院的医生
    hid是主码
    '''
    cursor.execute("""
    IF OBJECT_ID('Hospital', 'U') IS NOT NULL
        DROP TABLE Hospital
    CREATE TABLE Hospital (
        hid CHAR(10),          /*医院编号*/
        hname CHAR(100),       /*医院名称*/
        hrank CHAR(10),        /*医院等级*/      
        haddress CHAR(100),    /*医院地址*/
        hworktime CHAR(30),    /*工作时间*/
        hcapacity INT,         /*最大容量*/
        htel CHAR(10),         /*医院电话*/
        hpatient INT,          /*患者人数*/
        hdoctor INT,           /*医生人数*/
        PRIMARY KEY(hid),      /*医院编号是主码*/
        )
        """)
    #建立酒店信息表
    '''
    hotel_id-酒店编号
    hotel_name--酒店名称
    hotel_rank--酒店星级
    hotel_address--酒店地址
    hotel_price --住房价格
    hotel_people--入住人数
    hotel_departpeople--隔离人数
    hotel_capacity--客房总数
    hotel_tel--酒店电话
    hotel_id是主码
    '''
    cursor.execute("""
    IF OBJECT_ID('Hotel', 'U') IS NOT NULL
        DROP TABLE Hotel
    CREATE TABLE Hotel (
        hotel_id CHAR(10),           /*酒店编号*/
        hotel_name CHAR(100),        /*酒店名称*/
        hotel_rank CHAR(10),         /*酒店星级*/
        hotel_address CHAR(100),     /*酒店地址*/
        hotel_price INT,             /*住房价格*/
        hotel_people INT,            /*入住人数*/
        hotel_departpeople INT,      /*隔离人数*/
        hotel_capacity INT,          /*最大容量*/
        hotel_tel CHAR(10),          /*酒店电话*/
        PRIMARY KEY(hotel_id)        /*酒店编号是主码*/
        )
        """)
    # 建立社区信息表
    '''
    cid-社区编号
    cname--社区名称
    caddress--社区地址
    cdepartpeople--隔离人数
    cdoctor--医生人数
    ctel --社区电话
    cestate_worktime--物业工作时间
    cRC_worktime--居委工作时间
    cid是主码
    '''
    cursor.execute("""
    IF OBJECT_ID('Comunity', 'U') IS NOT NULL
        DROP TABLE Comunity
    CREATE TABLE Comunity (
        cid CHAR(10),             /*社区编号*/
        cname CHAR(100),          /*社区名称*/
        cpeople INT,              /*居住人数*/
        caddress CHAR(100),       /*社区地址*/
        cdepartpeople INT,        /*隔离人数*/
        cdoctor INT,              /*医生人数*/
        ctel CHAR(10),            /*联系电话*/
        cestate_worktime CHAR(20),/*物业工作时间*/
        cRC_worktime CHAR(20),    /*居委工作时间*/
        PRIMARY KEY(cid)          /*社区编号是主码*/
        )
        """)

    #建立医生信息表
    '''
    dworkid--医生编号
    did--医生身份证号
    dname--医生姓名
    dsex--医生性别,
    dage--医生年龄,
    dhospital--工作医院,
    dpatients--负责患者人数
    ddepartment--科室
    dtitle--职称
    deducation--学历
    dtel--电话号码
    daddress--家庭住址
    dworktime--工作时间
    dworkid是主码
    '''

    cursor.execute("""
    IF OBJECT_ID('Doctor', 'U') IS NOT NULL
            DROP TABLE Doctor
    CREATE TABLE Doctor (
        dworkid CHAR(20),       /*医生工号*/
        did CHAR(20) NOT NULL,  /*身份证号*/
        dname CHAR(10),         /*医生姓名*/
        dsex CHAR(4),           /*医生性别*/
        dage INT,               /*医生年龄*/
        dhospital CHAR(100),    /*工作医院*/
        dhospitalid CHAR(10),   /*医院编号*/
        dpatients INT,          /*负责患者人数*/
        ddepartment CHAR(100),  /*所在科室*/
        dtitle CHAR(20),        /*职称*/
        deducation CHAR(20),    /*学历*/
        dtel CHAR(20),          /*联系电话*/
        daddress CHAR(100),     /*家庭住址*/
        daddressid CHAR(10),    /*社区编号*/
        dworktime  CHAR(20),    /*工作时间*/
        PRIMARY KEY(dworkid),   /*医生工号是主码*/
        FOREIGN KEY(dhospitalid) REFERENCES Hospital(hid),  /*医院编号是外码，参考医院信息表的hid*/
        FOREIGN KEY(daddressid) REFERENCES Comunity(cid)    /*社区编号是外码，参考社区信息表的cid*/
        )
        """)


    #建立患者信息表
    '''
    pid--身份证号
    pname--姓名
    psex--性别
    page--年龄
    pcomunity--居住社区
    psympton--症状
    pdate--近期日程
    phospital--就诊医院
    pdoctorid--主治医生
    pinhos--入院时间
    pouthos--出院时间
    papart--隔离状态
    pworkplace--工作单位
    pid是主码
    pcomunity是外码，参照了Comunity中的cid
    phospital是外码，参照了Hospital中的hid
    pdoctor是外码，参照了Doctor中的dworkid
    '''

    cursor.execute("""
    IF OBJECT_ID('Patient', 'U') IS NOT NULL
        DROP TABLE persons
    CREATE TABLE Patient (
        pid CHAR(30),              /*患者身份证号*/
        pname CHAR(10),            /*患者姓名*/
        psex CHAR(4),              /*患者性别*/
        page INT,                  /*患者年龄*/
        pcomunity CHAR(100),       /*居住地址*/
        pcomunityid CHAR(10),      /*社区编号*/
        psympton CHAR(100),        /*症状*/
        pdate CHAR(10),            /*近期日程*/
        phospital CHAR(20),        /*就诊医院*/
        phospitalid CHAR(10),      /*医院编号*/
        pdoctoridname CHAR(20),    /*主治医生*/
        pdoctorid CHAR(20),        /*医生工号*/
        pinhos CHAR(20),           /*入院时间*/
        pouthos CHAR(20),          /*出院时间*/
        papart  CHAR(20),          /*隔离状态*/
        pworkplace CHAR(20),       /*工作单位*/
        PRIMARY KEY(pid),          /*身份证号是主码*/
        FOREIGN KEY(hospitalid) REFERENCES Hospital(hid),  /*医院编号是外码，参考医院信息表的hid*/
        FOREIGN KEY(pcomunityid) REFERENCES Comunity(cid), /*社区编号是外码，参考社区信息表的cid*/
        FOREIGN KEY(pdoctorid) REFERENCES Doctor(did)      /*主治医生工号是外码，参考医生信息表的did*/
    )
    """)

    #建立密集人群信息表
    '''
    contact_id--身份证号
    contact_name--姓名
    contact_sex--性别
    contact_age--年龄
    contact_comunity--居住社区
    contact_sympton--症状
    contact_depadd--隔离地点
    contact_people--接触源
    depart_time--隔离时长
    contact_workplace--工作单位
    contact_id是主码
    '''
    cursor.execute("""
    IF OBJECT_ID('Contact_People', 'U') IS NOT NULL
        DROP TABLE Contact_People
    CREATE TABLE Contact_People (
        contact_id CHAR(20),          /*身份证号*/
        contact_name CHAR(10),        /*密集接触者姓名*/
        contact_sex  CHAR(4),         /*密集接触者性别*/
        contact_age INT,              /*密集接触者年龄*/
        contact_comunity CHAR(100),   /*密集接触者居住地址*/
        contact_comunityid CHAR(10),  /*社区编号*/
        contact_sympton CHAR(100),    /*症状*/
        contact_depadd CHAR(100),     /*隔离酒店名称*/
        contact_depaddid CHAR(10),    /*酒店编号*/
        contact_people CHAR(20),      /*接触的患者姓名*/
        contact_peopleid CHAR(30),    /*接触患者的身份证号*/
        depart_time CHAR(20),         /*隔离时长*/
        contact_workplace CHAR(20),   /*工作单位*/
        PRIMARY KEY(contact_id),      /*身份证号是主码*/
        FOREIGN KEY(contact_comunityid) REFERENCES Comunity(cid), /*社区编号是外码，参考社区信息表的cid*/
        FOREIGN KEY(contact_depaddid) REFERENCES Hotel(hotel_id), /*酒店编号是外码，参考酒店信息表的hotel_id*/
        FOREIGN KEY(contact_peopleid) REFERENCES Patient(pid)     /*接触源身份证号是外码，参考患者信息表的pid*/
    )
        """)
    connect.commit()


if __name__ == '__main__':
    con= conn()
    creat(con)

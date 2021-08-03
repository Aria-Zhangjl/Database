#用户操作界面
#政府管理人员可以修改操作所有表格
#医院操作医生表格
#卫生局可以操作医院、医生表格
#所有的人可以查看社区、医院和酒店的信息

#用户密码
password={'政府人员':'government','卫生局':'health bureau','医院':'hospital'}

import easygui as eg
import InsertData as ID
import Query as qr
import Alter as at
import Count
import delete
#登陆
def upload():
    userid = eg.buttonbox(msg="请选择您的身份", title="用户身份选择", choices=['政府人员', '卫生局', '医院', '普通用户'])
    if userid != '普通用户':
        passw = eg.passwordbox(msg="请输入登陆密码", title="用户身份登陆")
        while passw != password[userid]:
            eg.msgbox(msg="密码错误！请重新选择")
            userid = eg.buttonbox(msg="请选择您的身份", title="用户身份选择", choices=['政府人员', '卫生局', '医院', '普通用户'])
            passw = eg.passwordbox(msg="请输入登陆密码", title="用户身份登陆")
    return userid


#普通用户的权限
def ordi_user(id,func):
    if (func=='添加数据' or func=='修改数据' or func=='删除数据'):
        eg.buttonbox(msg="抱歉，您没有该权限！", title="错误", choices=['返回'])
    elif(func=='查询信息'):
        choice=eg.buttonbox(msg="请选择您想查看的信息", title="信息查询", choices=['医院','社区','酒店'])
        if(choice=='医院'):
            qr.queryHospital()
        elif(choice=='社区'):
            qr.queryComunity()
        else:
            qr.queryHotel()

#医院权限
def hos_user(id,func):
    if (func == '添加数据'):
        ID.insert_doctor()
    elif (func == '查询信息'):
        choice=eg.buttonbox(msg="请选择您想查看的信息", title="信息查询", choices=['医院','社区','酒店','医生','患者'])
        if(choice=='医院'):
            qr.queryHospital()
        elif(choice=='社区'):
            qr.queryComunity()
        elif(choice=='酒店'):
            qr.queryHotel()
        elif(choice=='患者'):
            qr.queryPatient()
        else:
            qr.queryDoctor()
    elif (func=='修改数据'):
        at.AlterDoctor()

#卫生局权限
def health_author(id,fun):
    if (func == '添加数据'):
        table = eg.buttonbox("请选择添加的数据库", choices=['医院信息', '医生信息'])
        if(table=='医院信息'):
            ID.insert_hos()
        if(table=='医生信息'):
            ID.insert_doctor()
        # 跳转到对应的信息
    elif (func == '查询信息'):
        choice = eg.buttonbox(msg="请选择您想查看的信息", title="信息查询", choices=['医院', '社区', '酒店', '医生','患者','密集接触者'])
        if (choice == '医院'):
            qr.queryHospital()
        elif (choice == '社区'):
            qr.queryComunity()
        elif (choice == '酒店'):
            qr.queryHotel()
        elif(choice=='医生'):
            qr.queryDoctor()
        elif(choice=='患者'):
            qr.queryPatient()
        else:
            qr.queryContact()
    elif(func=='修改数据'):
        choice=eg.buttonbox("请选择要修改的数据",title="修改数据",choices=['医生信息','医院信息'])
        if choice=='医生信息':
            at.AlterDoctor()
        else:
            at.AlterHospital()

#政府权限
def gover_user(id,fun):
    if (func == '添加数据'):
        table = eg.buttonbox(msg="请选择添加的数据库", choices=['患者信息', '密集接触者', '医院信息', '医生信息','社区信息', '酒店信息'])
        if(table=='医院信息'):
            ID.insert_hos()
        if(table=='医生信息'):
            ID.insert_doctor()
        if(table=='社区信息'):
            ID.insert_comunity()
        if(table=='酒店信息'):
            ID.insert_hotel()
        if(table=='患者信息'):
            ID.insert_patient()
        if(table=='密集接触者'):
            ID.insert_contact()
    elif (func == '查询信息'):
        choice = eg.buttonbox(msg="请选择您想查看的信息", title="信息查询", choices=['医院', '社区', '酒店', '医生', '患者', '密集接触者'])
        if (choice == '医院'):
            qr.queryHospital()
        elif (choice == '社区'):
            qr.queryComunity()
        elif (choice == '酒店'):
            qr.queryHotel()
        elif (choice == '医生'):
            qr.queryDoctor()
        elif (choice == '患者'):
            qr.queryPatient()
        else:
            qr.queryContact()
    elif(fun=='修改数据'):
        choice=eg.buttonbox(msg="请选择要修改的数据对象",title="修改数据",choices=['医生信息','医院信息','酒店信息',\
            '社区信息','患者信息','密集接触者信息'])
        if choice=='医生信息':
            at.AlterDoctor()
        elif choice=='医院信息':
            at.AlterHospital()
        elif choice=='酒店信息':
            at.AlterHotel()
        elif choice=='社区信息':
            at.AlterComunity()
        elif choice=='患者信息':
            at.AlterPatient()
        else:
            at.AlterContact()
    elif(func=='删除数据'):
        delete.deleteTab()

#根据身份选择不同的数据库功能
def choose_func(id,func):
    if func=='统计数据':
        Count.Countsafecom()
        which=eg.buttonbox(msg="选择想要查询的统计信息",title="数据统计",choices=['医生信息','患者信息','密集接触者信息','自定义统计'])
        if which == '医生信息':
            Count.countdoctor()
        elif which =='患者信息':
            Count.countpatient()
        elif which =='密集接触者信息':
            Count.countcontact()
        else:
            Count.Countbyself()
    else:
        if (id == '普通用户'):
            ordi_user(id, func)
        elif (id == '政府人员'):
            gover_user(id, func)
        elif (id == '卫生局'):
            health_author(id, func)
        elif (id == '医院'):
            hos_user(id, func)






if __name__ == '__main__':
    id=upload()
    func = eg.buttonbox(msg="请选择您的操作", title="功能选择", choices=['查询信息', '统计数据', '添加数据','修改数据','删除数据','退出登陆'])
    while func!='退出登陆':
        choose_func(id, func);
        func = eg.buttonbox(msg="请选择您的操作", title="功能选择", choices=['查询信息', '统计数据', '添加数据', '修改数据', '删除数据','退出登陆'])

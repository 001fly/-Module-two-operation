# Author:HU YUE
import pickle
import os
import sys
import logging
import random

BASE_DIR=os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(BASE_DIR)


def loadd(f_all,name):
    with open("%s.txt"%name, 'wb')as f:
        pickle.dump(f_all, f)

# def nadd(wood):
#     with open("%s.txt"%name, "rb")as t:
#         # stuffs=stuffs
#         t_all = pickle.load(t)
#         print(t_all)
#         # print(type(t_all))
#         t_all.append(wood)
#         # print(t_all)
#         loadd(t_all)
logger = logging.getLogger('TEST_LOG')


def coller1(name): #管理员模块可修改用户信息！
    while True:
        print("____管理员系统1___\n"
              "0.查询用户密码\n"
              "1.创建用户和密码\n"
              "2.修改用户信息\n"
              "3.删除用户\n"
              "4.冻结用户\n"
              "5.退出")
        number=input("输入数字进行操作：")
        if number=="0":
            name=input("输入用户名：")
            if not os.path.exists("%s.txt"%name):
                print("用户不存在！")
            else:
                with open("%s.txt"%name,"rb")as f:
                    f_all=pickle.load(f)
                    print(f_all)
                    logger.info('您查询了%s的用户信息。'%name)
        if number=="1":
            name=input("创建新用户：")
            if os.path.exists("%s.txt"%name):
                print("用户已存在请重新输出入")
            else:
                open("%s.txt"%name, 'w').close()
                password=input("新用户密码：")
                new_user={"card_number":"",
                          "user":name,
                          "password":password,
                          "Credit_line":10000,
                          "balance":0,
                          "repayment":0,
                          }
                for i in range(6):  #随机生成信用卡号！
                    each = random.randrange(0, 9)
                    tmp = chr(random.randint(65, 90))
                    new_user["card_number"]+= str(each) + str(tmp)
                print("用户账号已创建！")
                print(new_user)
                with open("%s.txt"%name,"wb")as f:
                    pickle.dump(new_user,f)
                    logger.info('您创建了%s新用户！。' % name)
        if number=="2":
            name=input("输入需要修改的用户名：")

            if os.path.exists("%s.txt" % name):
                n=0
                while n<3:
                        print("____修改用户信息___\n"
                              "0.修改用户password\n"
                              "1.修改用户Credit_line\n"
                              "2.修改用户balance\n"
                              "3.修改用户repayment\n"
                              "4.返回上层菜单")
                        with open("%s.txt" % name, "rb")as f:  # 输出用户当前信息
                            f_all = pickle.load(f)
                            print(f_all)
                        number1 = input("选择修改：")
                        if number1 == "0":
                            new = input("新密码：")
                            with open("%s.txt" % name, "rb")as f:
                                f_all = pickle.load(f)
                                f_all["password"] = new
                                loadd(f_all, name)
                                logger.info('您对%s的密码进行了修改，新密码为%s！。' % (name,new))
                        if number1 == "1":
                            new = input("新额度：")
                            with open("%s.txt" % name, "rb")as f:
                                f_all = pickle.load(f)
                                f_all["Credit_line"] = new
                                loadd(f_all, name)
                                logger.info('您对%s的额度进行了修改，新额度为%s！。' % (name, new))
                        if number1 == "2":
                            new = input("新余额：")
                            with open("%s.txt" % name, "rb")as f:
                                f_all = pickle.load(f)
                                f_all["balance"] = new
                                loadd(f_all, name)
                                logger.info('您对%s的余额进行了修改，新余额为%s！。' % (name, new))
                        if number1 == "3":
                            new = input("新还款金度：")
                            with open("%s.txt" % name, "rb")as f:
                                f_all = pickle.load(f)
                                f_all["repayment"] = new
                                loadd(f_all, name)
                                logger.info('您对%s的还款金度进行了修改，新还款金额为%s！。' % (name, new))
                        if number1 == "4":
                            n=3
            else:
                    print("要修改的用户不存在！请确认后输入")
        if number=="3":
                name=input("输入用户名：")
                if os.path.exists("%s.txt"%name):
                    os.remove("%s.txt"%name)
                    logger.info('您删除了%s的用户信息！。' % name)
                else:
                    print("要删除的用用户不存在！")
        if number=="4":
            if not os.path.exists("forzen_user.txt"):
                open("forzen_user.txt","w").close()
                forzen=[]
                with open("forzen_user.txt","wb")as f:
                    pickle.dump(forzen,f)
            else:
                with open("forzen_user.txt", "rb")as f:
                    f_all=pickle.load(f)
                    print(f_all) #测试代码
                    dname=input("需冻结账户：")
                    if dname in f_all:
                        print("用户已冻结！")
                        continue
                    else:
                     with open("forzen_user.txt", "wb")as t:
                        f_all.append(dname)
                        pickle.dump(f_all,t)
                        logger.info('您冻结了%s用户！。' % name)
        if number=="5":
            break







# os.path.exists("user_ma.txt")
#
# print(os.path.exists("user_ma.txt"))


# coller1("hy")





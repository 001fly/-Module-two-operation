# Author:HU YUE

import logging
import os
import sys
import pickle
from core import banksys
from core import shop
from core import account1
# import banksys
# import shop
# import account1

base_dir=os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
print(base_dir)
sys.path.append(base_dir)



land_proof={"name":"none",
            "id_poor":False,
            "user_message":"none"
}


# def lock(username):
#     if not os.path("lockuser.txt"):
#         with open("lockuser.txt", "wb")as f:
#             userlist=[]
#             pickle.dump(userlist,f)
#     else:
#         with open("lockuser.txt","rb")as f:
#             f_all=pickle.load(f)
#             f_all.append(name)
#             with open("lockuser.txt", "wb")as t:
#                 pickle.dump(f_all,t)













def acc(food):
    def change():
        n=0
        while n<3 :
            username = input("username:")
            user_acc(username)
            if land_proof["id_poor"]:
                n=3
            else:
                n+=1
                if n==3:
                    print("输入用户名次数过多请重新登录！")
                    break
        food()
    return change



def user_acc(username):
    n=0
    while n<3 and land_proof["id_poor"] is not True:
        if os.path.exists("%s.txt" % username):
            if not   ("forzen_user.txt"):
                open("forzen_user.txt","w").close()
                forzen=[]
                with open("forzen_user.txt","wb")as f:
                    pickle.dump(forzen,f)
            else:
                with open("forzen_user.txt", "rb")as f:
                    f_all = pickle.load(f)
                    if username in f_all:
                        print("用户已冻结！需要本人去银行解除冻结！")
                        break
                    else:
                        with open("%s.txt" % username, "rb")as f:
                            f_all = pickle.load(f)
                            passwo = input("password:")
                            if passwo == f_all["password"]:
                                land_proof["name"] = username
                                land_proof["id_poor"] = True
                                land_proof["user_message"] = f_all
                                return land_proof
                                break
                            else:
                                n += 1
                                print("密码错误重新输入")
        else:
            n=3
            print("用户不存在,请重新输入！")
            break

@acc #
def run():
    if land_proof["id_poor"]:
        logger = logging.getLogger('TEST_LOG')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("%s.log" % land_proof["name"],encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh_formatter = logging.Formatter('%(asctime)s - %(name)s '
                                         '- %(levelname)s'
                                         ' - %(message)s')
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)
        while True:
                print("____atm___\n"
                      "0.个人账户操作\n"
                      "1.atm小超市\n"
                      "2.管理员模块\n"
                      "3.退出")

                choose=input("按选项操作：")
                n=0
                while n<3:
                    if choose=="0":
                        banksys.bank(land_proof["name"])
                        break
                    if choose=="1":
                        shop.shopp(land_proof["name"])
                        break
                    if choose=="2":
                        account1.coller1(land_proof["name"])
                        break
                    if choose == "3":
                        n=3
                else:
                   break

        else:
            print("用户名或密码错误请重新操作！")

#
# run()















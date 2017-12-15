# Author:HU YUE
import pickle
import os
import sys
import logging
BASE_DIR=os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(BASE_DIR)
logger = logging.getLogger('TEST_LOG')
def shopp(name):
    n=0
    while n<3:
        print("____欢迎来到atm购物车____")
        print("-----shopping—cart-----")
        shopping = {"0": ["手机", 3000], "1": ["xx电脑", 4000], "2": ["摩登茶杯", 500], "3": ["手表", 1500]}
        for cart in shopping: #格式化输出
            print(cart,shopping[cart])
        comm=input("选择所需商品(0-3),其他则退出：")
        if comm in shopping:
            with open("%s.txt" % name, "rb")as f:
                f_all = pickle.load(f)
                if int(f_all["Credit_line"])>shopping[comm][1]:
                    f_all["Credit_line"] = int(f_all["Credit_line"]) - shopping[comm][1]
                    f_all["repayment"]+=shopping[comm][1]
                    print("你本次用额度购买了%s,信用卡额度还剩%s" % (shopping[comm][0],f_all["Credit_line"]))
                    with open("%s.txt" % name, "wb")as f:
                        pickle.dump(f_all, f)
                        logger.info("%s用户用额度购买了%s,信用卡额度还剩%s" % (name, shopping[comm][0], f_all["Credit_line"]))
                else:
                    print("信用卡额度不足！是否使用信用卡余额支付？yes/no")
                    cost=input("请选择yes or no?:")
                    if cost=="yes":
                        if f_all["balance"] > shopping[comm][1]:
                            f_all["balance"] = int(f_all["balance"]) - shopping[comm][1]
                            print("你本次用余额购买了%s,信用卡余额还剩%s" % (shopping[comm][0], f_all["balance"]))
                            with open("%s.txt" % name, "wb")as f:
                                pickle.dump(f_all, f)
                                logger.info("%s用户用余额购买了%s,信用卡额度还剩%s" % (name, shopping[comm][0], f_all["balance"]))
                        else:
                            difference=shopping[comm][1]-int(f_all["balance"])
                            print("您要购买%s,信用卡余额为%s,还缺少%s!请充值或提高信用卡额度！"%(shopping[comm][0],f_all["balance"],difference))
                            logger.info("%s用户购买%s,信用卡余额为%s,还缺少%s!请充值或提高信用卡额度！" % (name, shopping[comm][0],f_all["balance"],difference))
                    else:
                        print("您的信用卡额度不足请重新选择或退出去充值！")
                        continue
        else:
            break






# shopp("alex")








# shopp("alex")



# if os.path("user_ma.txt"):
#     print("tt")
# else:
#     print("no")
# with open("user_ma.txt","rb")as f:
#     f_all=pickle.load(f)
#     print(f_all)








#
# info={"0":["手机",3000],
#               "1":["xx电脑",4000],
#               "2":["摩登茶杯",500],
#               "3":["手表",1500]
#         }
# comm=input("ooo:")
# print(info[comm][1])
# print(type(info[comm][1]))
# for i in info:
#     print(type(i))
#
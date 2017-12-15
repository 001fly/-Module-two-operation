# Author:HU YUE
import pickle
import os
import sys
import logging
BASE_DIR=os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(BASE_DIR)
logger = logging.getLogger('TEST_LOG')
def bank(name): #银行模块
    while True:
        print("____银行系统___\n"
              "0.存款\n"
              "1.取款\n"
              "2.取现\n"
              "3.转账\n"
              "4.还款\n"
              "5.退出")
        choise=input("请选择：")
        if choise=="0":
            balance_add=input("存入金额：")
            with open("%s.txt"%name,"rb")as f:
                f_all=pickle.load(f)
                f_all["balance"]=int(f_all["balance"])+int(balance_add)
                with open("%s.txt"%name,"wb")as f:
                    pickle.dump(f_all,f)
                    logger.info('%s进行了存款操作，本次存入金额为%s,卡上余额为%s。' % (name,balance_add,f_all["balance"]))
        if choise=="1":
            balance_cos=input("取款金额：")
            with open("%s.txt"%name,"rb")as f:
                f_all=pickle.load(f)
                f_all["balance"]=int(f_all["balance"])-int(balance_cos)
                with open("%s.txt"%name,"wb")as f:
                    pickle.dump(f_all,f)
                    logger.info('%s进行了取款操作，本次取款金额为%s,卡上余额为%s。' % (name, balance_cos, f_all["balance"]))
        if choise=="2":
            credit_line_add=input("取现金额：")
            with open("%s.txt"%name,"rb")as f:
                f_all=pickle.load(f)
                # remoney=(int(credit_line_add) * 5/100)+int(credit_line_add)
                f_all["repayment"]+=(int(credit_line_add) * 5/100)+int(credit_line_add)
                f_all["Credit_line"]=int(f_all["Credit_line"])-int(f_all["repayment"])
                with open("%s.txt"%name,"wb")as f:
                    pickle.dump(f_all,f)
                    logger.info('%s进行了取现操作，本次取现金额为%s,卡上额度为%s。' % (name, credit_line_add, f_all["Credit_line"]))
                    # print(f_all)
        if choise=="3":
            tacc=input("转账金额：")
            tname=input("收款账户：")
            if os.path.exists("%s.txt" % tname):
                with open("%s.txt" % name, "rb")as f:
                    f_all = pickle.load(f)
                    f_all["balance"] = int(f_all["balance"]) - int(tacc)
                    with open("%s.txt"%name,"wb")as f:
                        pickle.dump(f_all,f)
                        logger.info('%s转账给%s，本次转账金额为%s,卡上余额为%s。' % (name, tname, tacc, f_all["balance"]))
                with open("%s.txt" % tname, "rb")as t:
                    t_all = pickle.load(t)
                    t_all["balance"] = int(t_all["balance"]) + int(tacc)
                    with open("%s.txt"%tname,"wb")as t:
                        pickle.dump(t_all,t)
                        fh = logging.FileHandler("%s.log" % tname, encoding="utf-8")
                        fh.setLevel(logging.INFO)
                        fh_formatter = logging.Formatter('%(asctime)s - %(name)s '
                                                         '- %(levelname)s'
                                                         ' - %(message)s')
                        fh.setFormatter(fh_formatter)
                        logger.addHandler(fh)
                        logger.info('%s收到%s的转账，本次转账金额为%s,卡上余额为%s。' % (tname, name, tacc, f_all["balance"]))
            else:
                print("收款账户不存在！请重新操作！")
        if choise=="4":  #还款操作
            with open("%s.txt"%name,"rb")as f:
                f_all=pickle.load(f)
                print(f_all)
                print("您的账单为%s是否还款？（yes or no）"%f_all["repayment"])
                choo=input("是否还款？")
                if choo=="yes":
                    remom=input("还款金额为%s:"%f_all["repayment"]) #显示需还款的金额
                    if int(remom)==f_all["repayment"]:  #还款必须一次还款！金额必须和需还款金额一致！
                        f_all["repayment"]-=int(remom)
                        f_all["Credit_line"]=f_all["Credit_line"]+int(remom)
                        print(f_all)
                        print("还款成功！")
                        with open("%s.txt" % name, "wb")as t:
                            pickle.dump(f_all, t)
                            logger.info('用户%s还款成功！本次还款金额为%s。' % (name,remom))
                    else:
                        print("请按账单再次还款！")
                else:
                    print("请进行其他操作。")
                    break
        if choise=="5":
            break














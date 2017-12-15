# Author:HU YUE
import os
import sys
print( os.path.abspath(__file__) )
BASE_DIR=os.path.dirname(os.path.dirname( os.path.abspath(__file__) ))
sys.path.append(BASE_DIR)

from core import main
from core import account1


if __name__=='__main__':
  while True:
    n=input("选择登录（atm or admin）退出（q）：")
    if n=="admin123":
        account1.coller1("admin")
    if n=="atm":
        main.run()
    if n=="q":
      break
    else:
      print("输入有误！请重新输入！")

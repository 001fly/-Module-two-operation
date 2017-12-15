# Author:HU YUE
import os
import pickle
def select(cmd,part,showcol,compareg,comparem,comparef,compares):
    with open("user_in1.txt","rb")as f:
        f_list=pickle.load(f)
        print(f_list) #测试代码
    n = 0
    for all_people in f_list:
        if comparef==">":
            if int(all_people[2])>int(compares):
                cols = showcol.split(",")
                name = all_people[1]
                age = all_people[2]
                n = n + 1
                print("| %s : %s |" % (name, age))
        if comparef=="<":
            if comparef == "<":
                if int(all_people[2]) < int(compares):
                    cols = showcol.split(",")
                    name = all_people[1]
                    age = all_people[2]
                    n=n+1
                    print("| %s : %s |" % (name, age))

        if comparef == "like":
            if  compares in all_people[5]:
                n = n + 1
                print("|%s|" %(all_people))
                # print(all_people[4])  测试代码
                # print(compares)

        if comparem == "dept":
            if all_people[4] == compares:
                n = n + 1
                print("|%s|" % (all_people))

    print("符合要求的有%s条数据"%n)



def loadFile(stuffs):
    with open("user_in1.txt", 'wb')as f:
        pickle.dump(stuffs, f)

def nadd(stuffs):
    with open("user_in1.txt", "rb")as t:
        # stuffs=stuffs
        t_all = pickle.load(t)
        # print(type(t_all))
        t_all.append(stuffs)
        # print(t_all)
        loadFile(t_all)

def insert(cmd,part,showcol,compareg,comparem,comparef,compares):
    #判断是否有员工信息表
    if not os.path.exists("user_in1.txt"):
        stuffs=[]
        loadFile(stuffs)
    with open("user_in1.txt", "rb")as t:
        t_all = pickle.load(t)
        # print(t_all)
    if t_all == []:
        id = 0
        name = input("name:")
        age = input("age:")
        phone = compares
        dept = input("dept:")
        enroll_date = input("enroll_date(2015-05-09):")
        stuffs = [id, name, age, phone, dept, enroll_date]
        nadd(stuffs)
    else:
        with open("user_in1.txt", "rb")as t:
            t_all = pickle.load(t)
        non=0
        for people in t_all:
            if int(people[3]) == int(compares):
                non+= 1
                print("员工已存在")
                break
                print(non)
        print(non)
        if non==0:
            for people in t_all:
                last = t_all[-1]
                id = int(last[0]) + 1
                name = input("name:")
                age = input("age:")
                phone = compares
                dept = input("dept:")
                enroll_date = input("enroll_date(2015-05-09):")
                stuffs = [id, name, age, phone, dept, enroll_date]
                nadd(stuffs)
                print("ok")
                break





def delete(cmd,part,showcol,compareg,comparem,comparef,compares):
    # 统一提取
    with open("user_in1.txt","rb")as f:
        f_all=pickle.load(f)
    for all_people in f_all:
        print(all_people[0])
        if int(all_people[0]) == int(compares):
            f_all.remove(all_people)
    stuffs=f_all
    loadFile(stuffs)


            # stuffs=f_all

def update(cmd,part,showcol,compareg,comparem,comparef,compares):
    # 统一提取需要信息！


    with open("user_in1.txt", "rb")as f:
       f_all=pickle.load(f)
    print(f_all)
    # print(compareg)
    # print(compares)
    for all_pp in f_all:
        # print(all_pp[4])
        if all_pp[4] == compareg:
            all_pp[4] = compares
    stuffs = f_all
    loadFile(stuffs)
















def run():
    while True:
        cmd = input("SQL>>")
        part = cmd.split()
        showcol = part[1]
        compareg = part[4].strip('"')
        comparem = part[5]
        comparef = part[6]
        compares = part[7].strip('"')
        if cmd.startswith("select"):
            select(cmd,part,showcol,compareg,comparem,comparef,compares)
        elif cmd.startswith("update"):
            update(cmd,part,showcol,compareg,comparem,comparef,compares)
        elif cmd.startswith("delete"):
            delete(cmd,part,showcol,compareg,comparem,comparef,compares)
        elif cmd.startswith("insert"):
            insert(cmd,part,showcol,compareg,comparem,comparef,compares)
        elif cmd=="pp":
            with open("user_in1.txt", "rb")as t:
                t_all = pickle.load(t)
        elif cmd=="exit":
            exit()
        else:
            print("输入有误，请重新输入")
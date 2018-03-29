#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, pickle, hashlib, time

# 程序主目录 & 数据库文件路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_DIR = BASE_DIR + r'\DB'
# db_school = db_DIR + r'\school'
# db_teacher = db_DIR + r'\teacher'
# db_student = db_DIR + r'\student'
# db_classes = db_DIR + r'\classes'
# db_course = db_DIR + r'\course'
# db_admin = db_DIR + r'\admin'
# db_class_record = db_DIR + r'\class_record'
# db_class_grade = db_DIR + r'\class_grade'

def create_uid():     # 创建uid
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()  # 16进制格式hash

# 基础类
class Baseclass(object):
    def __init__(self):
        pass
    def dump_dict(self,type,dump_dict):     # 将字典经pickle序列化后写入文件
        filename = create_uid()
        dump_dict['uid'] = filename
        file_path = "%s\%s" %(db_DIR,type)
        ab_file = "%s\%s" %(file_path,filename)
        if os.path.isdir(file_path):
            with open(ab_file,"wb") as f:
                pickle.dump(dump_dict,f)
                f.flush()
                if True:
                    print(('Create %s succeed!' % type).center(39, '*'))
                    for key in dump_dict:
                        print("%s: %s" % (key,dump_dict[key]))
    def dump_list(self,type,dump_list):     # 将列表经pickle序列化后写入文件
        file_path = "%s\%s" % (db_DIR, type)
        filename = create_uid()
        ab_file = "%s\%s" % (file_path, filename)
        if os.path.isdir(file_path):
            with open(ab_file, "wb") as f:
                pickle.dump(dump_list, f)
                f.flush()
                if True:
                    print(('Create %s succeed!' % type).center(39, '*'))
                    for i in dump_list:
                        for key in i:
                            print("%s: %s" % (key,i[key]))
                        print("\n")
    def open(self,type):     # 反序列化pickle文件内容
        data = []
        db_path = "%s\%s" %(db_DIR,type)
        for i in os.listdir(db_path):
            if os.path.isfile(os.path.join(db_path,i)):
                db_file = os.path.join(db_path,i)
                with open(db_file,'rb') as f:
                    file_dict = pickle.load(f)
                    data.append(file_dict)
        return data
    def manager_auth(self,username,password):     # 管理员身份验证
        user = 'zff'
        passwd = '333333'
        if username == user and password == passwd:
            print("Welcome manager!")
            return True
        else:
            print("Username and password don't match!")
            return False
    def view_student_info(self):     # 查看学员详细信息
        student_name = input("Student name: ").strip()
        student_school = input("School: ").strip()
        student_class = input("Class: ").strip()
        student_info = Baseclass.open(self, "student")
        student_grade = Baseclass.open(self, "class_grade")
        student_record = Baseclass.open(self, "class_record")
        for i in student_info:
            if i['name'] == student_name and i['school'] == student_school and i['class'] == student_class:
                for key in i:
                    print("%s: %s" % (key, i[key]))
        for j in student_grade:
            for m in j:
                if m['name'] == student_name and m['school'] == student_school and m['class'] == student_class:
                    print("student_grade: %s" % m['student_grade'])
        for k in student_record:
            for n in k:
                if n['name'] == student_name and n['school'] == student_school and n['class'] == student_class:
                    print("class_situation: %s" % n['class_situation'])
                    print("attend_times: %s" % n['attend_times'])
    def view_info(self,type):     # 查看元素信息
        data_info = Baseclass.open(self, type)
        for i in data_info:
            for key in i:
                print("%s: %s" % (key, i[key]))

# 管理员类
class Admin(Baseclass):
    def __init__(self):
        super(Admin,self).__init__()
    def create_school(self):     # 创建学校函数
        school_dict = {}
        school_name = input("School name: ").strip()
        school_address = input("School address: ").strip()
        school_dict['school'] = school_name
        school_dict['address'] = school_address
        Baseclass.dump_dict(self,'school',school_dict)
    def create_teacher(self):     # 创建讲师函数
        teacher_dict = {}
        teacher_name = input("Teacher name: ").strip()
        teacher_salary = input("Teacher salary: ").strip()
        teacher_school = input("School name: ").strip()
        teacher_dict['name'] = teacher_name
        teacher_dict['salary'] = teacher_salary
        teacher_dict['school'] = teacher_school
        Baseclass.dump_dict(self,'teacher',teacher_dict)
    def create_student(self):     # 创建学员函数
        student_dict = {}
        student_name = input("Student name: ").strip()
        student_sex = input("Student sex: ").strip()
        student_school = input("School name: ").strip()
        student_class = input("Class: ").strip()
        student_pay = input("Did %s pay for tuition(Y|N): " % student_name).strip()
        student_dict['name'] = student_name
        student_dict['sex'] = student_sex
        student_dict['school'] = student_school
        student_dict['class'] = student_class
        student_dict['pay_fee'] = student_pay
        Baseclass.dump_dict(self,'student',student_dict)
    def create_course(self):     # 创建课程函数
        course_dict = {}
        course_name = input("Course name: ").strip()
        course_period = input("Course period: ").strip()
        course_price = input("Course price: ").strip()
        course_dict['name'] = course_name
        course_dict['period'] = course_period
        course_dict['price'] = course_price
        Baseclass.dump_dict(self,'course',course_dict)
    def create_classes(self):     # 创建班级函数
        classes_dict = {}
        class_name = input("Class name: ").strip()
        class_teacher = input("Responsibility teacher: ").strip()
        class_course = input("Study course: ").strip()
        classes_dict['name'] = class_name
        classes_dict['teacher'] = class_teacher
        classes_dict['course'] = class_course
        Baseclass.dump_dict(self,'classes',classes_dict)
    def view_info(self,type):     # 查看元素函数
        Baseclass.view_info(self,type)
    def get_fee(self):     # 收费函数
        student_name = input("Student name: ").strip()
        student_school = input("School: ").strip()
        student_class = input("Class: ").strip()
        student_list = Baseclass.open(self,"student")
        for i in student_list:
            if i["name"] == student_name and i["school"] == student_school and i["class"] == student_class:
                if i["pay_fee"] == 'N':
                    student_uid = i['uid']
                    filename = db_DIR + '\student\\' + student_uid
                    print(filename)
                    student_pay = input("Did %s pay for tuition(Y|N): " % student_name).strip()
                    if student_pay == 'Y':
                        i["pay_fee"] = 'Y'
                        with open(filename,'wb') as f:
                            print(i)
                            pickle.dump(i, f)
                            f.flush()
                            if True:
                                print(('%s pay fee succeed!' % student_name).center(39, '*'))
                else:
                    print("%s don't have to pay tuition." % i['name'])
    def auth(self,username,password):     # 管理员身份验证
        return Baseclass.manager_auth(self,username,password)
    def view_student_info(self):     # 查看学员详细信息
        Baseclass.view_student_info(self)

# 讲师类
class Teacher(Baseclass):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        super(Teacher,self).__init__()
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_school = teacher_school
    def create_class_record(self):   # 创建上课记录
        class_record = []
        student_school = input("School: ").strip()
        student_class = input("Class: ").strip()
        student_list = Baseclass.open(self,'student')
        for i in student_list:
            if i['school'] == student_school and i['class'] == student_class:
                student_name = i['name']
                student_status = input("%s class attend situation: " % student_name).strip()
                student_attend_times = input("Attend times: ").strip()
                i["class_situation"] = student_status
                i['attend_times'] = student_attend_times
                class_record.append(i)
        Baseclass.dump_list(self,"class_record",class_record)
    def create_class_grade(self):   #创建学员成绩
        class_grade = []
        student_school = input("School: ").strip()
        student_class = input("Class: ").strip()
        student_list = Baseclass.open(self, 'student')
        for i in student_list:
            if i['school'] == student_school and i['class'] == student_class:
                student_name = i['name']
                student_grade = input("%s grade: " % student_name).strip()
                student_attend_times = input("Attend times: ").strip()
                i["student_grade"] = student_grade
                i['attend_times'] = student_attend_times
                class_grade.append(i)
        Baseclass.dump_list(self, "class_grade", class_grade)
    def view_stuent(self,type):     # 查看学员上课记录/成绩模板函数
        data_list = []
        student_school = input("School: ").strip()
        student_class = input("Class: ").strip()
        student_name = input("Student name: ").strip()
        class_data_list = Baseclass.open(self, type)
        for i in class_data_list:
            for j in i:
                if j['school'] == student_school and j['class'] == student_class and j['name'] == student_name:
                    data_list.append(j)
        for i in data_list:
            for key in i:
                print("%s: %s" % (key, i[key]))
            print("\n")
    def view_student_record(self):   # 查看学生上课记录
        Teacher.view_stuent(self,'class_record')
    def view_student_grade(self):   # 查看学员成绩
        Teacher.view_stuent(self,"class_grade")
    def view_student_info(self):     # 查看学员信息
        Baseclass.view_student_info(self)

# 学员类
class Student(Baseclass):
    def __init__(self,student_name,student_sex,student_school,student_classes):
        super(Student,self).__init__()
        self.student_name = student_name
        self.student_sex = student_sex
        self.student_school = student_school
        self.student_classes = student_classes
    def student_enroll(self):     # 学员注册函数
        student_dict = {}
        print("Welcome to stuent enroll system!")
        student_name = input("Name: ").strip()
        student_sex = input("Sex: ").strip()
        student_school = input("School: ").strip()
        student_classes = input("Classes: ").strip()
        student = Student(student_name,student_sex,student_school,student_classes)
        student_dict['name'] = student.student_name
        student_dict['sex'] = student.student_sex
        student_dict['school'] = student.student_school
        student_dict['class'] = student.student_classes
        student_dict['pay_fee'] = 'N'
        Baseclass.dump_dict(self,'student',student_dict)
    def student_pay_fee(self):     # 学员缴费函数
        student_name = input("Name: ").strip()
        student_school = input("School: ").strip()
        student_class = input("Class: ").strip()
        data_list = Baseclass.open(self, "student")
        for i in data_list:
            if i["school"] == student_school and i['class'] == student_class and i['name'] == student_name:
                if i["pay_fee"] == 'N':
                    student_uid = i['uid']
                    filename = db_DIR + '\student\\' + student_uid
                    choice = input("Do you want to pay %s class fee(Y|N): " % i['class'])
                    if choice == 'Y':
                        print("Please call manager to get fee.")
                        admin_u = input("Please input manager username: ").strip()
                        admin_p = input("Please input manager password: ").strip()
                        if Baseclass.manager_auth(self,admin_u,admin_p):
                            i["pay_fee"] = 'Y'
                            with open(filename, 'wb') as f:
                                pickle.dump(i, f)
                                f.flush()
                                if True:
                                    print(('%s pay fee succeed!' % student_name).center(39, '*'))
                else:
                    print("%s don't have to pay tuition." % i['name'])
    def student_info(self,type):     # 学员查看上课记录/成绩模板函数
        student_name = input("Name: ").strip()
        student_school = input("School: ").strip()
        student_class = input("Class: ").strip()
        data_list = Baseclass.open(self, type)
        for i in data_list:
            for j in i:
                if j['school'] == student_school and j['class'] == student_class and j['name'] == student_name:
                    for key in j:
                        print("%s: %s" % (key, j[key]))
                    print("\n")
    def student_class_record(self):     # 学员查看上课记录函数
        Student.student_info(self, 'class_record')
    def student_grade(self):     # 学员查看成绩函数
        Student.student_info(self, 'class_grade')

# 管理员视图类
class Admin_view(Admin):
    def __init__(self):
        super(Admin_view, self).__init__()
    def auth(self,username,password):
        return Admin.auth(self,username,password)
    def login(self):
        menu = '''
        ---------- Welcome to manager view ----------
                \033[32;1m
                1.  Schools management
                2.  Teachers management
                3.  Students management
                4.  Courses management
                5.  return
                \033[0m'''
        menu_dict = {
            '1': Admin_view.schools_management,
            '2': Admin_view.teachers_management,
            '3': Admin_view.students_management,
            '4': Admin_view.courses_management,
            '5': "logout"
        }
        username = input("Please input manager username: ").strip()
        password = input("Please input manager password: ").strip()
        auth = Admin_view.auth(self, username, password)
        if auth:
            exit_flag = False
            while not exit_flag:
                print(menu)
                choice = input("Please input your choice: ").strip()
                if choice in menu_dict:
                    if int(choice) == 5:
                        exit_flag = True
                    else:
                        menu_dict[choice](self)
                else:
                    print("\033[31;1m Please input between 1 to 5...\033[0m")
    def schools_management(self):   # 学校管理
        exit_flag = False
        while not exit_flag:
            print('''
            ---------- Welcome to schools management ----------
                    \033[34;1m
                    1.  create school
                    2.  create class
                    3.  look over schools info
                    4.  look over classes info
                    5.  return
                    \033[0m''')
            choice = input("Please input your choice: ").strip()
            if choice == '1':
                Admin.create_school(self)
            elif choice == '2':
                Admin.create_classes(self)
            elif choice == '3':
                Admin.view_info(self,"school")
            elif choice == '4':
                Admin.view_info(self,"classes")
            else:
                exit_flag = True
    def teachers_management(self):   # 讲师管理
        exit_flag = False
        while not exit_flag:
            print('''
            ---------- Welcome to teachers management ----------
                    \033[34;1m
                    1.  Create teacher
                    2.  Look over teacher info
                    3.  return
                    \033[0m''')
            choice = input("Please input your choice: ").strip()
            if choice == '1':
                Admin.create_teacher(self)
            elif choice == '2':
                Admin.view_info(self,"teacher")
            else:
                exit_flag = True
    def students_management(self):   # 学员管理
        exit_flag = False
        while not exit_flag:
            print('''
            ---------- Welcome to students management ----------
                    \033[34;1m
                    1.  Create student
                    2.  Get fees
                    3.  Look over student info
                    4.  return
                    \033[0m''')
            choice = input("Please input your choice: ").strip()
            if choice == '1':
                Admin.create_student(self)
            elif choice == '2':
                Admin.get_fee(self)
            elif choice == '3':
                Admin.view_student_info(self)
            else:
                exit_flag = True
    def courses_management(self):   # 课程管理
        exit_flag = False
        while not exit_flag:
            print('''
            ---------- Welcome to courses management ----------
                    \033[34;1m
                    1.  Create course
                    2.  Look over courses info
                    3.  return
                    \033[0m''')
            choice = input("Please input your choice: ").strip()
            if choice == '1':
                Admin.create_course(self)
            elif choice == '2':
                Admin.view_info(self,'course')
            else:
                exit_flag = True

# 讲师视图类
class Tearcher_view(Teacher):
    def __init__(self,teacher_name,teacher_salary,teacher_school):
        super(Tearcher_view,self).__init__(teacher_name,teacher_salary,teacher_school)
    def login(self):
        menu = '''
        ---------- Welcome to teacher view ----------
                \033[32;1m
                1.  Create class record
                2.  Create class grade
                3.  Look over students class record
                4.  Look over students grade
                5.  Look over studnet info
                6.  return
                \033[0m'''
        menu_dict = {
            '1':Teacher.create_class_record,
            '2':Teacher.create_class_grade,
            '3':Teacher.view_student_record,
            '4':Teacher.view_student_grade,
            '5':Teacher.view_student_info,
            '6':"logout"
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                choice = input("Please input choice: ").strip()
                if choice in menu_dict:
                    if choice == '6':
                        exit_flag = True
                    else:
                        menu_dict[choice](self)
                else:
                    print("\033[31;1m Please input between 1 to 6...\033[0m")

# 学员视图类
class Student_view(Student):
    def __init__(self,student_name,student_sex,student_school,student_class):
        super(Student_view,self).__init__(student_name,student_sex,student_school,student_class)
    def login(self):
        menu = '''
        ---------- Welcome to student view ----------
                \033[32;1m
                1.  enroll
                2.  pay fee
                3.  class record
                4.  student grade
                5.  return
                \033[0m'''
        menu_dict = {
            '1':Student.student_enroll,
            '2':Student.student_pay_fee,
            '3':Student.student_class_record,
            '4':Student.student_grade,
            '5':"logout"
        }
        if True:
            exit_flag = False
            while not exit_flag:
                print(menu)
                choice = input("Please input choice: ").strip()
                if choice in menu_dict:
                    if choice == '5':
                        exit_flag = True
                    else:
                        menu_dict[choice](self)
                else:
                    print("\033[31;1m Please input between 1 to 5...\033[0m")

# 程序交互函数
class Run(object):
    def __init__(self):
        pass
    def interactive(self):
        menu = '''
        ---------- Welcome to subject system ----------
                \033[32;1m
                1.  Stuent view
                2.  Teacher view
                3.  Manager view
                4.  Exit
                \033[0m'''
        menu_dict = {
            '1':Student_view,
            '2':Tearcher_view,
            '3':Admin_view,
            '4':"logout"
        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            choice = input("Please input your choice: ").strip()
            if choice in menu_dict:
                if choice == '4':
                    exit_flag = True
                else:
                    menu_dict[choice].login(self)
            else:
                print("\033[31;1m Please input between 1 to 4...\033[0m")
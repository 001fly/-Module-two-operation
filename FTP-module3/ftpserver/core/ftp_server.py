#!/user/bin/env python3
# -*- coding: utf-8 -*-
# author:tony
import socketserver
import json
import configparser
import os
import hashlib
import subprocess
from conf import settings


STATUS_CODE = {
    250:'invalid cmd format,...标准示范',
    251:'invalid cmd',
    252:'invalid auth data',
    253:'wrong username or password',
    254:'passed authentication',
    255:'filename is not provided',
    256:'file does not exsit on server',
    257:'file is ready to send',
    258:'md5 verification',
    259:'path does not exisit',
    260:'successfully ls path',
    261:'无权限浏览',
    262:'无权限切换',
    263:'切换目录成功',
    264:'切换目录的路径不存在',
    265:'传输的文件可以进行断点续传',
    266:'传输的文件不能进行断点续传',
    267:'file is ready to recv'
}
class FTPHandler(socketserver.BaseRequestHandler):
    '''重构handle'''
    def handle(self):
        while True:   #不断接收新数据
            self.data = self.request.recv(1024).strip()
            print(self.client_address)
            print('111')
            print(self.data)
            if not self.data: #客户端断开时，会给服务器发送空
                print('client is closed')
                break
            # self.request.sendall(self.data.upper())
            data = json.loads(self.data.decode())
            print('aaaaa',data)
            if data.get('action') is not None:
                if hasattr(self,'_%s'%data.get('action')):#加下划线预防和python关键字冲突
                    func = getattr(self,'_%s'%data.get('action'))
                    print('22')
                    func(data)
                else:
                    print('invalid cmd')  #这些错误信息应发给客户端如404.500状态码
                    self.send_response(251)
            else:
                print('invalid cmd format')
                self.send_response(250)
    def send_response(self,status_code,data=None):
        '''向客户端返回数据'''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:   #传进方法数据
            response.update(data)#新字典加到旧字典
        self.request.send(json.dumps(response).encode())

    def _auth(self,*args,**kwargs):
        '验证判断用户名密码'
        data = args[0]
        if data.get('username') is None or data.get('password') is None:
            self.send_response(252)
        user = self.authenticate(data.get('username'),data.get('password'))
        if user is None:
            self.send_response(253)
        else:
            print('验证成功',user)
            self.user = user
            os.chdir('%s\%s'%(settings.USERHOME,self.user['username']))
            self.send_response(254)

    def authenticate(self,username,password):
        '''验证用户合法性，合法就返回用户数据'''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]['Password']
            if _password == password:
                print('pass ayth',username)
                config[username]['username'] = username
                return config[username]

    def _put(self,*args,**kwargs):
        '上传数据'
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
            return
        basename = data.get('filename').split('\\')[-1]
        user_home_dir = '%s\%s'%(settings.USERHOME,self.user['username'])
        file_abs_path = '%s\%s'%(user_home_dir,data.get('filename'))
        recv_size =0
        if os.path.isfile(file_abs_path):
            recv_size = os.path.getsize(file_abs_path)
            self.send_response(265,{'recv_size':recv_size})
        self.send_response(267)
        file_obj = open(basename,'ab')
        if data.get('md5'):
            md5_obj = hashlib.md5()
            while recv_size < data.get('file_size'):
                try:
                   info = self.request.recv(4096)
                   recv_size+=len(info)
                   file_obj.write(info)
                   md5_obj.update(info)
                except Exception as e:
                    print('数据接收出错')
                    break

            else:
                file_obj.close()
                md5_val = md5_obj.hexdigest()
                print(md5_val)
                self.send_response(258,{'md5':md5_val})
                print('接收成功 md5')
        else:
            print(recv_size,data.get('file_size'))
            while recv_size < data.get('file_size'):
                try:
                  info = self.request.recv(4096)
                  recv_size+=len(info)
                  file_obj.write(info)
                except Exception as e:
                    print('数据接收出错')
                    break
            else:
                file_obj.close()
                print('接收成功')



    def _get(self,*args,**kwargs):
        '下载数据'
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
            return
        #这里需检测服务端是否有权限去下载文件（家目录和filename的拼接）
        user_home_dir = '%s\%s'%(settings.USERHOME,self.user['username'])
        file_abs_path = '%s\%s'%(user_home_dir,data.get('filename'))
        #filename = '%s/%s.txt'%(user_home_dir,data.get('filename'))
        print('33')
        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path,'rb')
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257,data = {'file_size':file_size})
            #  这里有问题，缓存区满后发送，有可能这里和下面send(line)一起发送  粘包
            self.request.recv(1)  #处理粘包 等待客户端确认
            # if os.path.isfile(filename):
            #     with open(filename,'r') as f:
            #         info = json.loads(f.read())
            #         self.send_response(265,info)
            #         file_obj.seek(info.get('seek_addr'))
            #         send_size = info.get('send_size')
            #     with open(filename,'w') as f:
            #         print('filename')
            # else:
            #     send_size = 0
            #     self.send_response(266)
            send_size = 0

            if 'continue' in data:

                self.send_response(265)
                res = self.request.recv(1024)
                send_size = int(res.decode())
                file_obj.seek(send_size)  #定位
            else:
                self.send_response(266)
                self.request.recv(1) #处理粘包 等待客户端确认

            print('1')
            print(data,data.get('md5'))
            print(send_size,file_obj.tell())
            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:  #self.request.sendall(xx.read())10G要读到内存，low
                    #md5判断不放这是因为放这每次发送都判断，速度特别慢
                    try:
                      self.request.send(line)  #边读边发
                      send_size+=len(line)

                    except Exception as e:
                        print('数据发送出错')
                        break
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258,{'md5':md5_val})
                    print('2')
                    print('send file done')
            else:
                for line in file_obj:  #self.request.sendall(xx.read())10G要读到内存，low

                    try:
                      self.request.send(line)  #边读边发
                      send_size+=len(line)

                    except Exception as e:
                        print('数据发送出错',send_size)
                        break
                else:
                    file_obj.close()
                    print('send file done',send_size)
        else:
            self.send_response(256)

    def _ls(self,*args,**kwargs):
        '查看目录下文件'
        data = args[0]
        path = data.get('path')
        user_home_dir = '%s\%s'%(settings.USERHOME,self.user['username'])

        if path == '.':
            pathpwd = os.getcwd().strip()
            print(pathpwd,user_home_dir)
            if user_home_dir in pathpwd:
                path = pathpwd
                print('a')
            else:
                print('b')
                self.send_response(261)
        else:
            print('c')
            path = '%s\%s'%(user_home_dir,data.get('path'))

        if not os.path.exists(path):
            print('d')
            self.send_response(259)
        list = os.listdir(path)
        print(list)
        # list = subprocess.getstatusoutput(cmd)
        # print(list)
        # if list[0]:
        #     ls_data = list[1]
        self.send_response(260,{'data':list})




    def _cd(self,*args,**kwargs):
        '''切换目录'''
        data = args[0]
        path = data.get('path')
        user_home_dir = '%s\%s'%(settings.USERHOME,self.user['username'])
        if path == '.':
            pathpwd = os.getcwd().strip()
            if user_home_dir in pathpwd:
                path = pathpwd
            else:
                self.send_response(262)
        else:
            path = '%s\%s'%(user_home_dir,data.get('path'))
        if os.path.exists(path):
            os.chdir(path)
            self.send_response(263,{'data':path})
        else:
            self.send_response(264)



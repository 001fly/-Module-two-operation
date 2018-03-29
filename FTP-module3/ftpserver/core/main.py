#!/user/bin/env python3
# -*- coding: utf-8 -*-
# author:tony
import optparse
import socketserver
from core.ftp_server import FTPHandler
from conf import settings

class argvhandler(object):   #用optparse后sys.argv不需要啦
    '智能获取参数，添加并执行不同功能'
    def __init__(self):
        self.parser = optparse.OptionParser()
        # parser.add_option('-s','--host',dest = 'host',help = 'server binding host address')
        # parser.add_option('-p','--port',dest = 'port',help = 'server binding port')
        (options,args) = self.parser.parse_args()    #options是设置的内容，args是未指定的内容
        #以上从参数读域名，端口的方法
        #print(options.host,options.port)
        self.verity_args(options,args)

    def verity_args(self,options,args):
        '''校验并调用相应的功能'''
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print('going to start')

        server = socketserver.ThreadingTCPServer((settings.HOST,settings.PORT),FTPHandler)

        server.serve_forever()





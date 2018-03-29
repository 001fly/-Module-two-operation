#!/user/bin/env python3
# -*- coding: utf-8 -*-
# author:tony
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

USERHOME = '%s\home'%BASE_DIR
LOG_DIR = '%s\log'%BASE_DIR
LOG_LEVEL = 'DEBUG'

ACCOUNT_FILE = r'%s\conf\accounts.cfg'%BASE_DIR

HOST = '0.0.0.0'
PORT = 9999

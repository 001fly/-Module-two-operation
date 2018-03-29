#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/11/20

import os, sys
# 程序主目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 添加环境变量
sys.path.append(BASE_DIR)

import subject_system
action = subject_system.Run()
action.interactive()
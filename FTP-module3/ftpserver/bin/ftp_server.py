#!/user/bin/env python3
# -*- coding: utf-8 -*-
# author:tony
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main


if __name__ == '__main__':
    main.argvhandler()
# -*- coding: utf-8 -*-
import sys
import os


def app_path():
    if hasattr(sys, 'frozen'):
        root_dir = os.path.dirname(os.path.dirname(sys.executable))
    else:
        root_dir = os.path.dirname(__file__)

    return root_dir.replace('\\','/')

# -*- encoding=utf8 -*-
__author__ = "Myz"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["Android://127.0.0.1:5037?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH"])



def start_num():
    
    # 进图点击
    if exists(Template(r"tpl1594960637461.png", record_pos=(-0.069, -0.098), resolution=(2160, 1080))):
        touch(Template(r"tpl1594960665612.png", record_pos=(-0.074, -0.101), resolution=(2160, 1080)))
    else:
        pass
    
    
    # 出击
    if exists(Template(r"tpl1594961324663.png", record_pos=(0.214, 0.108), resolution=(2160, 1080))):
        touch(Template(r"tpl1594961334034.png", record_pos=(0.217, 0.112), resolution=(2160, 1080)))
    else:
        pass
    
    
    # 选择队伍出击
    if exists(Template(r"tpl1594961394869.png", record_pos=(0.306, 0.168), resolution=(2160, 1080))):
        touch(Template(r"tpl1594961412780.png", record_pos=(0.305, 0.165), resolution=(2160, 1080)))
    else:
        pass
    
    
    
    


    


    

start_num()
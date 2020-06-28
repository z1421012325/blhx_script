# -*- encoding=utf8 -*-
__author__ = "Myz"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/192.168.1.2:7899?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

# 移动距离固定了,如果需要变动请循环or重写


# 手机屏幕宽和高
width,height = device().get_current_resolution()


# 上移动
def up_move():
    left_start_pt = (width * 0.5, height / 12)
    ledt_end_pt = (width * 0.5, height / 2)
    swipe(left_start_pt,ledt_end_pt)

    
# 右移动
def right_move():
    right_start_pt = (width * 0.35, height / 2)
    right_end_pt = (width * 0.1, height / 2)
    swipe(right_start_pt,right_end_pt)

# 左移动
def left_move():
    left_start_pt = (width * 0.1, height / 2)
    ledt_end_pt = (width * 0.35, height / 2)
    swipe(left_start_pt,ledt_end_pt)
    
# 下移动
def down_move():
    left_start_pt = (width * 0.5, height / 2)
    ledt_end_pt = (width * 0.5, height / 12)
    swipe(left_start_pt,ledt_end_pt)


















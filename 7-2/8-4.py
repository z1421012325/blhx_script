# -*- encoding=utf8 -*-
__author__ = "Myz"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=["Android://127.0.0.1:5037?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH"])

    
    
    
# 是否打boss
is_boss = True

# 道中回合
daozhong_num = 5

# 战斗等待时间
wait_max_time = 70

# 见图加载时间
load_time = 15

# 搜索小怪异常
search_monster_err = False
# hp 危机
_hp_danger = False
# 前排or后排暴毙
_head_tail_hp_danger = False



# 问号资源最大个数
wenhao_ziyuan_max_num = 4
    
# 7-2标志
qi_er = Template(r"tpl1594960637461.png", record_pos=(-0.069, -0.098), resolution=(2160, 1080))

# 出击图标
chuji = Template(r"tpl1594961324663.png", record_pos=(0.214, 0.108), resolution=(2160, 1080))

# 选择队伍图标
xuanzduiwu = Template(r"tpl1594961394869.png", record_pos=(0.306, 0.168), resolution=(2160, 1080))
    
# 切换队伍
qiehuanduiwu = Template(r"tpl1594961661418.png", record_pos=(0.328, 0.222), resolution=(2160, 1080))

# 主力队伍图标
zhuliduiwu = Template(r"tpl1594962383568.png", record_pos=(-0.037, 0.048), resolution=(2160, 1080))

# 轻型队伍图标
qingxingduiwu = Template(r"tpl1594962562029.png", record_pos=(0.264, -0.0), resolution=(2160, 1080))

# 战后道具点击图标
daojudianji = Template(r"tpl1594964257577.png", record_pos=(-0.001, -0.089), resolution=(2160, 1080))

# 战后经验点击图标
jingyandianji = Template(r"tpl1594964458556.png", record_pos=(0.308, 0.207), resolution=(2160, 1080))

# 问号资源
wenhaoziyuan = Template(r"tpl1594965233374.png", record_pos=(0.341, -0.028), resolution=(2160, 1080))

# 撤退图标
chetui = Template(r"tpl1594965808809.png", record_pos=(0.194, 0.22), resolution=(2160, 1080))

# 确定图标
queding = Template(r"tpl1594965822960.png", record_pos=(0.106, 0.106), resolution=(2160, 1080))

# 战斗评价
zhandoupingjia =  Template(r"tpl1594968738102.png", record_pos=(0.037, 0.007), resolution=(2160, 1080))

# 战斗状态
zhandouzhuangtai = Template(r"tpl1594968880820.png", record_pos=(0.395, -0.216), resolution=(2160, 1080))


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


# 小怪类型 轻型-主力-航母 
a_type = 1
b_type = 2
c_type = 3
# 小怪等级 一星-二星-三星
a_level = 1
b_level = 2
c_level = 3

# 打小怪
# def attack(_type,level):
def attack(_type):    
    if _type == a_type:
        touch(qingxingduiwu)
    
    if _type == b_type:
        touch(zhuliduiwu)

    if _type == c_type:
        pass

 
# 搜索小怪
def search_monster():
    sleep(1.5)

    _type = 0
    if exists(qingxingduiwu):
        _type = a_type
    elif exists(zhuliduiwu):
        _type = b_type
    
    if _type != 0:
        attack(_type)
        return
    else:
        right_move()
        sleep(2.0)
        search_monster()
        
        down_move()
        sleep(2.0)
        search_monster()
        
        left_move()
        sleep(2.0)
        search_monster()
        
        up_move()
        sleep(2.0)
        search_monster()

        # 上下左右搜索之后还未找到则表示搜索异常,尝试在等待战斗时间之后检测该变量是否未true来表示是否退出该次出击
        search_monster_err = True
        
# 计算战斗等待时间
def wait_auto_max_time():
    sleep(wait_max_time)
    if not exists(zhandoupingjia):
        for i in range(5):
            sleep(10)
            if exists(zhandoupingjia):
                return
        

# 战后结果展示or点击
def spolis():
    
    # todo 未完成
    # 大获全胜or暴毙界面点击
    if 1 > 2:
        head_tail_hp_danger()
    else:
        
        # 战斗评价点击
        if exists(zhandoupingjia):
            touch(zhandoupingjia)
    
        # 道具点击
        if exists(daojudianji):
            touch(daojudianji)

        # 紫色船只点击
        ships_click()

        # 经验界面点击
        sleep(1.0)
        if exists(jingyandianji):
            touch(jingyandianji)

# 检测血量是否不足       
def is_hp_danger():
    
    # 检测血量 return False
#     if exists(Template(r"tpl1594971169133.png", record_pos=(-0.451, -0.143), resolution=(2160, 1080))):
        

    
    return False
            
# 血量不足退出
def hp_danger():
    _hp_danger = True
    pass

# 前排or后排over检测
def head_tail_hp_danger():
    _head_tail_hp_danger = True
    
    # todo 暴毙检测or点击
    
    pass


# 直接退出出击
def exit_out():
    touch(chetui)
    sleep(1.00)
    touch(queding)

# 紫色船只(new)
def ships_click():
    pass
   
# 问号资源    
def material_click():
    if exists(wenhaoziyuan):
        touch(wenhaoziyuan)
    sleep(6.00)
    if exists(daojudianji):
        touch(daojudianji)
    else:
        sleep(3.00)
        exists(Template(r"tpl1594969899844.png", record_pos=(0.062, 0.122), resolution=(2160, 1080)))

#         touch(daojudianji)

    # todo 优化问号资源点击到维修则使用维修  out....

# 资源搜索
def search_materila():
    
    if exists(wenhaoziyuan):
        for i in range(wenhao_ziyuan_max_num):
            material_click()
    else:
        return
        

# 石油
def shiyou_jiance():
    pass

# 新任务
def new_task():
    pass

# 仓库
def ships_is_max():
    pass

# 心情
def mood():
    pass


def start_num():
    # 进图点击
    if exists(qi_er):
        touch(Template(r"tpl1594960665612.png", record_pos=(-0.074, -0.101), resolution=(2160, 1080)))
    else:
        pass

    # 出击
    if exists(chuji):
        touch(Template(r"tpl1594961334034.png", record_pos=(0.217, 0.112), resolution=(2160, 1080)))
    else:
        pass
    
    # 选择队伍出击
    if exists(xuanzduiwu):
        touch(Template(r"tpl1594961412780.png", record_pos=(0.305, 0.165), resolution=(2160, 1080)))
    else:
        pass
    
    # 循环扫描并最大等待
    for i in range(daozhong_num):
        
        search_monster_err = False
        _hp_danger = False    
        _head_tail_hp_danger = False
        
        # 检测血量,石油,心情,仓库   --- 顺序很重要
        if is_hp_danger():
            hp_danger()
            search_materila()
            exit_out()
            return
        
        shiyou_jiance()
        mood()
        ships_is_max()
        
        search_monster()
        
        # 进图与战斗等待时间 or 经过问号资源点被暂停
        sleep(load_time)
        if exists(daojudianji):
            touch(daojudianji)
            search_monster()
            sleep(load_time)
        
        
        # 检测是否为战斗状态中,有可能exists找到的小怪是被封路的,所以改为不打boss
        if exists(zhandouzhuangtai):
            pass
        else:
            is_boss = False

#         sleep(wait_max_time)
        wait_auto_max_time()    
    
    
        # 战后点击
        spolis()
        
        # 新任务
        new_task()
        
        # 搜索异常,退出该图
        if search_monster_err or _head_tail_hp_danger:
            search_materila()
            exit_out()
            return

    # 问号资源点击
    search_materila()
    
    # 打boss
    if is_boss:
        pass
    


    


    

start_num()
# -*- encoding=utf8 -*-
__author__ = "Myz"

# 碧蓝航线活动 「激唱的UNIVERSE」 sp5 脚本 
# 待优化



from airtest.core.api import *
from airtest.cli.parser import cli_setup

# 有线link
if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["Android://127.0.0.1:5037?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH"])


# script content
print("start...")

# 参数区域

# 出击次数
chujicishu = 10
# 道中次数
daozhongcishu = 6
# 预计道中s胜最大时间
s_max_time =  100 # 100
# 预计等待时间
wait_time = 15   # 15
# 每次扫描动画等待时间
every_scan_time = 3.0

# 递归最大次数
max_digui = 6
# 初始递归计数
init_duigui = 0





# 立即出击图标
lijichuji = Template(r"tpl1604373214284.png", record_pos=(0.219, 0.107), resolution=(2160, 1080))

luoen = Template(r"tpl1604381605491.png", record_pos=(-0.14, -0.048), resolution=(2160, 1080))


guanghui =Template(r"tpl1604380805106.png", record_pos=(-0.154, 0.039), resolution=(2160, 1080))

baerdimo =Template(r"tpl1604380834423.png", record_pos=(-0.147, -0.047), resolution=(2160, 1080))


quzhu = Template(r"tpl1604376854964.png", record_pos=(-0.157, -0.05), resolution=(2160, 1080))

hangmu = Template(r"tpl1604376840766.png", record_pos=(0.11, 0.073), resolution=(2160, 1080))

zhongxun = Template(r"tpl1604376872581.png", record_pos=(0.007, 0.029), resolution=(2160, 1080))





# 屏幕大小  列表  w h 
w,h = device().get_current_resolution()

# 屏幕拖拽 上下左右
def up_drag(start_multiple_h=0.8,end_multiple_h=0.5):
    swipe((0.5*w,start_multiple_h*h),(0.6*w,end_multiple_h*h))

def down_drag(start_multiple_h=0.4,end_multiple_h=0.8):
    swipe((0.5*w,start_multiple_h*h),(0.5*w,end_multiple_h*h))

def left_drag(start_multiple_w=0.6,end_multiple_w=0.2):
    swipe((start_multiple_w*w,0.5*h),(end_multiple_w*w,0.5*h))

def right_drag(start_multiple_w=0.2,end_multiple_w=0.6):
    swipe((start_multiple_w*w,0.5*h),(end_multiple_w*w,0.5*h))

    
    
    
# 船舱满员 直接退役
def chuancan_manyuan_clear():
    
    print("检测船舱中ing...")
    sleep(2.0)
    if exists(Template(r"tpl1604378632837.png", record_pos=(-0.002, -0.0), resolution=(2160, 1080))):

        touch(Template(r"tpl1604378657099.png", record_pos=(-0.137, 0.105), resolution=(2160, 1080)))
        sleep(1.0)
        touch(Template(r"tpl1604378679365.png", record_pos=(0.113, 0.213), resolution=(2160, 1080)))
        sleep(1.0)
        touch(Template(r"tpl1604378692949.png", record_pos=(0.257, 0.197), resolution=(2160, 1080)))
        sleep(1.0)
        touch(Template(r"tpl1604378719435.png", record_pos=(0.004, -0.09), resolution=(2160, 1080)))
        sleep(1.0)

        touch(Template(r"tpl1604378732650.png", record_pos=(0.217, 0.127), resolution=(2160, 1080)))
        sleep(1.0)
        touch(Template(r"tpl1604378749804.png", record_pos=(0.117, 0.146), resolution=(2160, 1080)))
        sleep(1.0)

        touch(Template(r"tpl1604378799968.png", record_pos=(-0.457, -0.207), resolution=(2160, 1080)))
        sleep(1.0)
        
        print("船舱退役处理完毕")
        return True
    else:
        print("船舱不需要处理")
        return False
    
    
    
    
    
# 紧急任务点击   ok 
def job_clear():
    sleep(2.0)

    print("检测紧急任务ing...")
    
    if exists(Template(r"tpl1604380539771.png", record_pos=(-0.056, -0.012), resolution=(2160, 1080))) or exists(Template(r"tpl1604380556042.png", record_pos=(0.002, 0.106), resolution=(2160, 1080))):
        touch(Template(r"tpl1604380571835.png", record_pos=(0.0, 0.104), resolution=(2160, 1080)))
        print("紧急任务出现了")
        sleep(1.0)
    else:
        print("紧急任务未出现")


# 掉落精英船只  非new
def elite_processing():
    sleep(2.0)
    # 检测界面上含有星星,sr为二星,ssr为三星.该次sp5只有sr
    if "检测 'sr二星图标'":
        print("check sr or ssr...")
        "点击 sr二星图标"

        
def daozhongcishu_reduce(a_func):
    def f():
        global daozhongcishu
        a_func()
        daozhongcishu -= 1
    return f


# todo 不确定逻辑完整
# 搜索小怪并点击 
# 有弹药情况下优先精英>三星驱逐>三星战列>二星战列驱逐航母>一星航母,战列,驱逐>三星航母
# 无弹药避免航母,三星可能后排暴毙,二星航母超时a胜
@daozhongcishu_reduce
def search_enemy():
    global daozhongcishu
    print("搜索小怪中...")
    
    if daozhongcishu > 3:
        if exists(luoen):
            touch(luoen)
            return
        elif exists(guanghui):
            touch(guanghui)
            return
        elif exists(baerdimo):
            touch(baerdimo)
            return
        
    # 做个函数 参数值为驱逐,航母,重巡, swipe 四下移动寻找
    # 移动函数需要可以设置移动倍数 
    # todo 待优化
    if screen(quzhu):
        return
    if screen(zhongxun):
        return
    if screen(hangmu):
        return
        

def screen(k):
    if exists(k):
        touch(k)
        return True
    else:
        return False
        








# 搜索boss并点击  ok
def search_boss_and_click():
    print("搜索 boss 中...")
    

    if exists(Template(r"tpl1604375670646.png", record_pos=(-0.045, -0.115), resolution=(2160, 1080))):
        touch(Template(r"tpl1604375681686.png", record_pos=(-0.044, -0.112), resolution=(2160, 1080)))
        
        if chuancan_manyuan_clear():
            search_boss_and_click()            
        else:
            check_attack_status()
        
        
# boss出击          ok
def boss_attack():
    
    print("boss 战要开始若~~~")
    
    sleep(5.0)
    
    if exists(Template(r"tpl1604375820540.png", record_pos=(0.328, 0.223), resolution=(2160, 1080))):
        touch(Template(r"tpl1604375827366.png", record_pos=(0.33, 0.22), resolution=(2160, 1080)))


    sleep(2.0)
    down_drag()
    search_boss_and_click()
    wait_settlement()  
    print("boss The end!!!")
    job_clear()    

    # 结算界面    okokok
def wait_settlement():
    
    if exists(Template(r"tpl1604374519708.png", record_pos=(-0.288, 0.187), resolution=(2160, 1080))):
#         "点击界面显著地点"
        touch(Template(r"tpl1604374549060.png", record_pos=(-0.288, 0.188), resolution=(2160, 1080)))

        sleep(2.0)
    
    if exists(Template(r"tpl1604374560731.png", record_pos=(-0.007, -0.144), resolution=(2160, 1080))):
        # "点击 '获得道具' 图标""
        touch(Template(r"tpl1604374568635.png", record_pos=(0.0, -0.14), resolution=(2160, 1080)))

        sleep(2.0)
        elite_processing()  # todo
        
    if exists(Template(r"tpl1604374593204.png", record_pos=(0.312, 0.207), resolution=(2160, 1080))):
        # "点击 '确定' 按钮 "
        touch(Template(r"tpl1604374604207.png", record_pos=(0.312, 0.208), resolution=(2160, 1080)))

        sleep(2.0)

# 心情值
def mood_low():
    # 低耗造成心情值下降很快,所以pass掉
    print("心情值检测ing...")
    pass

# 检测战斗情况是否结束   ok
def check_attack_status():
    global init_duigui
    
    print("战斗中in... 等待 {}s".format(s_max_time))
    
    sleep(s_max_time)
    
    if exists(Template(r"tpl1604376412788.png", record_pos=(0.396, -0.219), resolution=(2160, 1080))) and init_duigui < max_digui:
        init_duigui += 1
        sleep(wait_time)
        check_attack_status()
    else:
        init_duigui = 0
        print("战斗结束惹...")
        return
    


# 进入关卡  注意:心情值,船舱status   ok?
def into_node():

    # 点击 'sp5' 图标
    # 点击 '立即前往' 图标
    # 在编队列表再次点击 '立即前往' 图标
    print("进图")
    if exists(Template(r"tpl1604373128449.png", record_pos=(0.077, 0.024), resolution=(2160, 1080))):
        touch(Template(r"tpl1604373148532.png", record_pos=(0.077, 0.02), resolution=(2160, 1080)))
        sleep(1.0)
        
    if exists(lijichuji):
        touch(lijichuji)
        sleep(1.0)
    
    if exists(lijichuji):
        touch(lijichuji)
        sleep(1.0)

    
    # todo  if true:
    if chuancan_manyuan_clear():
        # " 再次点击"
        print("----------")
        into_node()
    mood_low()

    sleep(5.0)
    job_clear()

# 出击 需要筛选出击目标  优先三星目标  ok
def attack():
    
    search_enemy()
    
    sleep(6.0)      # 路径移动时间
    
    # 判断船舱,心情值
    chuancan_manyuan_clear()    
    mood_low()
    
    # 超时判断
    check_attack_status()
    wait_settlement()
    job_clear()    
    
    
# into_count : 进图次数
# count : 道中次数
def script_run(into_count,count):
    
    global daozhongcishu
    
    for x in range(into_count):
        
        sleep(2.0)
        into_node()
        sleep(every_scan_time)
        down_drag()
        
        for y in range(count):
            print("The {} attack, the {} daozhong start!".format(x+1,y+1))
            attack()
            print("The {} attack, the {} daozhong end!".format(x+1,y+1))
    
        print("The {} boss attack start!".format(x+1,y+1))
        boss_attack()
        print("The {} boss attack end!".format(x+1,y+1))
                
        daozhongcishu = 6
        
        print(" \n ------------------------------------------------------- \n")
    
    print("Run successfully")

    
script_run(chujicishu,daozhongcishu)




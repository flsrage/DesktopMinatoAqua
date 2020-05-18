import sys
import threading
import time
import winsound

import playsound



from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, \
    QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QPixmap

class Aqua_clock(threading.Thread):
    # 闹钟类类继承自threading.Thread，只需要分别实现 __init__、__del__和run方法，
    def __init__(self,hour,minute):  # __init__方法
        threading.Thread.__init__(self)
        self.my_hour=hour
        self.my_minute=minute
        self.__running = threading.Event()
        self.__running.set()
        self.flag1=1
        self.flag2=1
        self.wavflag=0
        global aaa

    def shut(self):  # __del__方法
        self.flag2=0
        self.flag1=0
        # self.__running.clear()


    def run(self):  # run方法
        flag=1
        mp3=r'music/aqua_clock.wav'
        while self.flag1:
            while flag and self.flag2:
                t = time.localtime()
                time.sleep(1)
                fmt = "%H %M"
                now = time.strftime(fmt,t)
                now = now.split(' ')
                now_hour=now[0]
                now_hours=int(now_hour)
                now_minute=now[1]
                now_minutes=int(now_minute)
                if now_hours == self.my_hour and now_minutes == self.my_minute and self.wavflag==0:
                    aaa=winsound.PlaySound(mp3,winsound.SND_ASYNC)
                    self.wavflag=1
                    flag=0
            if self.wavflag == 1 and self.flag1==0:
                winsound.PlaySound(aaa, winsound.SND_PURGE)
                self.wavflag = 0






            
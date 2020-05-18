import sys
import time
import random
from clock import Aqua_clock
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, \
    QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup, QGraphicsOpacityEffect, QMenu, QAction, \
    QMessageBox
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import QIcon, QPixmap, QCursor,QIntValidator

anime_interval = 0.1
class pet_init(QWidget):
    _startPos = None
    _endPos = None
    _isTracking = False


    def __init__(self):
        super().__init__()
        self.initUI()#界面绘制较给InitUI方法

    def initUI(self):
        self.mode = 1
        self.move(100,100)
        # self.timer = QTimer()
        # self.timer.setInterval(500)
        # self.timer.timeout.connect(self.timeChanged)
        # self.timer.start()
        #设置窗口属性

        self.setWindowFlags(Qt.FramelessWindowHint)  # 去除界面边框
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 显示在最顶端
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明化
        # self.setMouseTracking(True)  # 设置鼠标移动跟踪是否有效
        #图片资源

        hbox=QVBoxLayout(self)


        #初始化多媒体组
        laugh_mode = 1
        self.music_player = QMediaPlayer()

        ur0 = QUrl.fromLocalFile("music/konaqua.mp3")
        content = QMediaContent(ur0)
        self.player = QMediaPlayer()
        self.player.setMedia(content)
        self.player.setVolume(70)
        self.player.play()





        #图片组媒体注册
        self.pic_clock=QPixmap('image/kuaclock.png')
        self.pic0 = QPixmap('image/oinion.png')
        self.pic1 = QPixmap('image/s_aqua_main.png')
        self.pic2 = QPixmap('image/s_aqua_main2.png')
        self.pic3 = QPixmap('image/s_aqua_main3.png')
        self.pic4 = QPixmap('image/down_aqua_main1.png')
        self.pic5 = QPixmap('image/down_aqua_main2.png')
        self.pic6 = QPixmap('image/down_aqua_main3.png')
        self.pic7 = QPixmap('image/left_up_aqua_main1.png')
        self.pic8 = QPixmap('image/left_up_aqua_main2.png')
        self.pic9 = QPixmap('image/left_up_aqua_main3.png')
        self.pic10 = QPixmap('image/left_up_aqua_laugh_main1.png')
        self.pic11 = QPixmap('image/right_up_aqua_main1.png')
        self.pic12 = QPixmap('image/right_up_aqua_main2.png')
        self.pic13 = QPixmap('image/right_up_aqua_main3.png')
        self.pic14 = QPixmap('image/right_up_aqua_laugh_main1.png')
        self.pic15 = QPixmap('image/downs_aqua_main1.png')
        self.pic16 = QPixmap('image/downs_aqua_main2.png')
        self.pic17 = QPixmap('image/sad_aqua_main.png')
        self.piclabel=QLabel(self)
        self.pic_clocklabel=QLabel(self)
        self.pic_clocklabel.setPixmap(self.pic_clock)
        self.piclabel.setPixmap(self.pic1)
        self.pic_clocklabel.setFixedHeight(100)
        self.pic_clocklabel.setFixedWidth(150)
        self.piclabel.setScaledContents(False)
        self.pic_clocklabel.setScaledContents(True)

        self.music_name_label =QLabel(self)
        self.music_name_label.setText("开始")


        # 按钮组
        #透明化按钮
        op1 = QGraphicsOpacityEffect()
        op1.setOpacity(0)
        op2 = QGraphicsOpacityEffect()
        op2.setOpacity(0)
        op3 = QGraphicsOpacityEffect()
        op3.setOpacity(0)
        op4 = QGraphicsOpacityEffect()
        op4.setOpacity(0)
        op5 = QGraphicsOpacityEffect()
        op5.setOpacity(0)
        op6 = QGraphicsOpacityEffect()
        op6.setOpacity(0)
        op7 = QGraphicsOpacityEffect()
        op7.setOpacity(0)
        op8 = QGraphicsOpacityEffect()
        op8.setOpacity(0)
        op9 = QGraphicsOpacityEffect()
        op9.setOpacity(0)
        self.laugh_button = QPushButton('laugh',self.piclabel )
        self.laugh_button.clicked.connect(self.laugh)
        self.angry_button=QPushButton('angry',self.piclabel)
        self.angry_button.clicked.connect(self.angry)
        self.head_button=QPushButton('head',self.piclabel)
        self.head2_button = QPushButton('hear2',self.piclabel)
        self.head_button.clicked.connect(self.head)
        self.head2_button.clicked.connect(self.head)
        self.neck_button=QPushButton('neck',self.piclabel)
        self.neck_button.clicked.connect(self.neck)
        self.earright_button = QPushButton('earright', self.piclabel)
        self.earright_button.clicked.connect(self.earright)
        self.earleft_button = QPushButton('earleft', self.piclabel)
        self.earleft_button.clicked.connect(self.earleft)
        self.talk1_button=QPushButton('talk1',self.piclabel)
        self.talk1_button.clicked.connect(self.talk1)
        self.talk2_button=QPushButton('talk2',self.piclabel)
        self.talk2_button.clicked.connect(self.talk2)
        self.laugh_button.setGraphicsEffect(op1)
        self.head_button.setGraphicsEffect(op2)
        self.head2_button.setGraphicsEffect(op9)
        self.talk1_button.setGraphicsEffect(op3)
        self.talk2_button.setGraphicsEffect(op4)
        self.earleft_button.setGraphicsEffect(op5)
        self.earright_button.setGraphicsEffect(op6)
        self.neck_button.setGraphicsEffect(op7)
        self.angry_button.setGraphicsEffect(op8)
            #闹钟按钮组
        self.clock_button = QPushButton('开始', self)
        self.clock_button.setFixedWidth(150)
        self.cancel_clock_button= QPushButton('取消', self)
        self.clock_button.setFixedWidth(150)
        self.clock_button.clicked.connect(self.clock_on)
        self.cancel_clock_button.clicked.connect(self.clock_off)
        self.clock_button.setStyleSheet(
            "QPushButton{background-color:lightpink}""QPushButton{border:2px}""QPushButton{border-radius:3px}")
        self.cancel_clock_button.setStyleSheet(
            "QPushButton{background-color:lightpink}""QPushButton{border:2px}""QPushButton{border-radius:3px}")
            #音乐按钮组
        self.music_start_button = QPushButton(self)
        self.music_puase_button = QPushButton(self)
        self.music_stop_button = QPushButton(self)
        self.music_exit_button = QPushButton('退出',self)
        self.music_menu_hide =QPushButton('隐藏',self)
        self.music_start_button.setFixedWidth(30)
        self.music_puase_button.setFixedWidth(30)
        self.music_stop_button.setFixedWidth(30)
        self.music_exit_button.setFixedWidth(40)
        self.music_menu_hide.setFixedWidth(40)
        self.music_start_button.clicked.connect(self.music_about)
        self.music_puase_button.clicked.connect(self.music_about)
        self.music_stop_button.clicked.connect(self.music_about)
        self.music_menu_hide.clicked.connect(self.music_about)
        self.music_exit_button.clicked.connect(self.music_about)
        self.music_start_button.setIcon(QIcon("image/play.png"))
        self.music_puase_button.setIcon(QIcon("image/pause.png"))
        self.music_stop_button.setIcon(QIcon("image/stop.png"))
        self.music_stop_button.setStyleSheet("QPushButton{background-color:lightpink}""QPushButton{border:2px}""QPushButton{border-radius:3px}")
        self.music_start_button.setStyleSheet(
            "QPushButton{background-color:lightpink}""QPushButton{border:2px}""QPushButton{border-radius:3px}")
        self.music_puase_button.setStyleSheet(
            "QPushButton{background-color:lightpink}""QPushButton{border:2px}""QPushButton{border-radius:3px}")
        self.music_menu_hide.setStyleSheet(
            "QPushButton{background-color:lightpink}""QPushButton{border:2px}""QPushButton{border-radius:3px}")
        self.music_exit_button.setStyleSheet(
            "QPushButton{background-color:lightpink}""QPushButton{border:2px}""QPushButton{border-radius:3px}")


            #闹钟组件
        self.hour_edit = QLineEdit()
        valid=QIntValidator(1,24,self)
        self.hour_edit.setFixedWidth(75)
        self.hour_edit.setValidator(valid)
        self.minute_edit = QLineEdit()
        valid = QIntValidator(0, 60, self)
        self.minute_edit.setFixedWidth(75)
        self.hour_print = QLabel('时')
        self.hour_print.setStyleSheet("color:white")
        self.minute_print = QLabel('分')
        self.minute_print.setStyleSheet("color:white")

        #布局架构
        mainbox=QVBoxLayout()
        clockbox=QHBoxLayout()
        musicbox = QHBoxLayout()


        vbbox=QVBoxLayout()
        vbhbox0 = QHBoxLayout()
        vbhbox1 = QHBoxLayout()
        vbhbox2 = QHBoxLayout()
        vbhbox3 = QHBoxLayout()
        vbhbox4 = QHBoxLayout()
        vbhbox5 = QHBoxLayout()
        vbhbox6 = QHBoxLayout()
        vbhbox7 = QHBoxLayout()


        #clockbox
        clockinnerbox1=QVBoxLayout()
        clockinnerbox2=QHBoxLayout()
        clockinnerbox3 = QHBoxLayout()

        clockbox.addWidget(self.pic_clocklabel)
        clockinnerbox2.addWidget(self.hour_edit)
        clockinnerbox2.addWidget(self.hour_print)
        clockinnerbox2.addWidget(self.minute_edit)
        clockinnerbox2.addWidget(self.minute_print)
        clockinnerbox1.addLayout(clockinnerbox2)
        clockinnerbox3.addWidget(self.clock_button)
        clockinnerbox3.addWidget(self.cancel_clock_button)
        clockinnerbox1.addLayout(clockinnerbox3)
        clockbox.addLayout(clockinnerbox1)
        self.pic_clocklabel.setVisible(False)
        self.clock_button.setVisible(False)
        self.cancel_clock_button.setVisible(False)
        self.hour_edit.setVisible(False)
        self.minute_edit.setVisible(False)
        self.hour_print.setVisible(False)
        self.hour_print.setVisible(False)
        self.minute_print.setVisible(False)



        #musicbox
        musicinnerbox1=QVBoxLayout()
        musicinnerbox2=QHBoxLayout()
        musicinnerbox2.addWidget(self.music_start_button)
        musicinnerbox2.addWidget(self.music_puase_button)
        musicinnerbox2.addWidget(self.music_stop_button)
        musicinnerbox2.addWidget(self.music_menu_hide)
        musicinnerbox2.addWidget(self.music_exit_button)

        musicinnerbox1.addWidget(self.music_name_label)
        musicinnerbox1.addLayout(musicinnerbox2)
        musicbox.addLayout(musicinnerbox1)
        self.music_name_label.setVisible(False)
        self.music_start_button.setVisible(False)
        self.music_puase_button.setVisible(False)
        self.music_stop_button.setVisible(False)
        self.music_exit_button.setVisible(False)
        self.music_menu_hide.setVisible(False)



        #talk1box
        vbhbox0.addStretch(3)
        vbhbox0.addWidget(self.talk1_button)
        vbhbox0.addStretch(3)
        #headbox
        vbhbox2.addStretch(2)
        vbhbox2.addWidget(self.head_button)
        vbhbox2.addStretch(2)
        #head2box
        vbhbox7.addStretch(2)
        vbhbox7.addWidget(self.head2_button)
        vbhbox7.addStretch(2)
        #earbox
        vbhbox1.addStretch(1)
        vbhbox1.addWidget(self.earleft_button)
        vbhbox1.addWidget(self.earright_button)
        vbhbox1.addStretch(1)
        #laughbox
        vbhbox3.addStretch(3)
        vbhbox3.addWidget(self.laugh_button)
        vbhbox3.addStretch(3)
        #neckbox
        vbhbox4.addStretch(5)
        vbhbox4.addWidget(self.neck_button)
        vbhbox4.addStretch(5)
        #angrybox
        vbhbox5.addStretch(1)
        vbhbox5.addWidget(self.angry_button)
        vbhbox5.addStretch(1)
        #talk2box
        vbhbox6.addStretch(1)
        vbhbox6.addWidget(self.talk2_button)
        vbhbox6.addStretch(1)

        vbbox.addLayout(vbhbox0)
        vbbox.addLayout(vbhbox2)
        vbbox.addLayout(vbhbox7)
        vbbox.addLayout(vbhbox1)
        vbbox.addLayout(vbhbox3)
        vbbox.addLayout(vbhbox4)
        vbbox.addLayout(vbhbox5)
        vbbox.addLayout(vbhbox6)



        self.piclabel.setLayout(vbbox)
        # self.pic_clocklabel.setLayout(vbbox)
        hbox.addLayout(clockbox)
        hbox.addWidget(self.piclabel)
        hbox.addLayout(musicbox)

        self.setLayout(hbox)

        self.piclabel.setContextMenuPolicy(Qt.CustomContextMenu)
        self.piclabel.customContextMenuRequested.connect(self.subMenuEvent)#piclabel开放右键策略

        #显示主界面

        self.show()
    def mousePressEvent(self, e):
        if e.button()==Qt.MidButton or e.button() ==Qt.RightButton :
            #点击中键或右键时开放鼠标追踪
            self._isTracking = True
            self.piclabel.setPixmap(self.pic2)
            self.player.play()
            self._startPos = QPoint(e.x(), e.y())
    def mouseMoveEvent(self, e):

            #拖动时更改窗口位置

            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
    def mouseReleaseEvent(self, e):
        # self.m_flag=False
        # self.setCursor(QCursor=(Qt.ArrowCursor))
        if e.button() == Qt.MidButton or e.button()==Qt.RightButton :
            self.piclabel.setPixmap(self.pic1)
            self.player.stop()
            self._isTracking = False#松开中键或右键时取消追踪
            self._startPos = None
            self._endPos = None
    def laugh (self):#笑组/嘴部
        laugh_mode = random.randint(1,5)
        url1 = QUrl.fromLocalFile("music/laugh1.mp3")
        url2 = QUrl.fromLocalFile("music/laugh2.mp3")
        url3 = QUrl.fromLocalFile("music/laugh3.mp3")
        url4 = QUrl.fromLocalFile("music/laugh4.mp3")
        url5 = QUrl.fromLocalFile("music/mua.mp3")
        url6 = QUrl.fromLocalFile("music/konbangwa.mp3")
        if laugh_mode==1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif laugh_mode==2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        elif laugh_mode == 3:
            content = QMediaContent(url3)
            self.player.setMedia(content)
        elif laugh_mode == 4:
            content = QMediaContent(url4)
            self.player.setMedia(content)
        elif laugh_mode == 5:
            content = QMediaContent(url5)
            self.player.setMedia(content)
        elif laugh_mode == 6:
            content = QMediaContent(url6)
            self.player.setMedia(content)
        self.player.play()
        #笑动画
        self.piclabel.setPixmap(self.pic2)
        self.piclabel.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic3)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic2)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic1)
    def head (self):#怪叫组/头
        head_mode = random.randint(1,6)
        url1 = QUrl.fromLocalFile("music/aoh.mp3")
        url2 = QUrl.fromLocalFile("music/bang.mp3")
        url3 = QUrl.fromLocalFile("music/biba.mp3")
        url4 = QUrl.fromLocalFile("music/cute.mp3")
        url5 = QUrl.fromLocalFile("music/cutetwice.mp3")
        url6 = QUrl.fromLocalFile("music/niconiconi.mp3")

        if head_mode==1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif head_mode==2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        elif head_mode == 3:
            content = QMediaContent(url3)
            self.player.setMedia(content)
        elif head_mode == 4:
            content = QMediaContent(url4)
            self.player.setMedia(content)
        elif head_mode == 5:
            content = QMediaContent(url5)
            self.player.setMedia(content)
        elif head_mode == 6:
            content = QMediaContent(url6)
            self.player.setMedia(content)

        self.player.play()
        #笑动画
        for anime_time in range(0,2):
            self.piclabel.setPixmap(self.pic2)
            self.piclabel.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic3)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic2)
            self.repaint()
            time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic1)
    def angry (self):#生气组/胸上部
        head_mode = random.randint(1,4)
        url1 = QUrl.fromLocalFile("music/attention.mp3")
        url2 = QUrl.fromLocalFile("music/fuckyou.mp3")
        url3 = QUrl.fromLocalFile("music/mad1.mp3")
        url4 = QUrl.fromLocalFile("music/mad2.mp3")

        if head_mode==1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif head_mode==2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        elif head_mode == 3:
            content = QMediaContent(url3)
            self.player.setMedia(content)
        elif head_mode == 4:
            content = QMediaContent(url4)
            self.player.setMedia(content)

        self.player.play()
        #笑动画
        for anime_time in range(0,2):
            self.piclabel.setPixmap(self.pic2)
            self.piclabel.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic3)
            self.repaint()
            time.sleep(10*anime_interval)
            self.piclabel.setPixmap(self.pic2)
            self.repaint()
            time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic1)
    def talk1 (self):#对话1组/头饰部
        talk_mode = random.randint(1,4)
        url1 = QUrl.fromLocalFile("music/welcome.mp3")
        url2 = QUrl.fromLocalFile("music/qua_is_here.mp3")
        url3 = QUrl.fromLocalFile("music/easyeasy.mp3")
        url4 = QUrl.fromLocalFile("music/understood.mp3")
        url5 = QUrl.fromLocalFile("music/konbangwa2.mp3")

        if talk_mode==1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif talk_mode==2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        elif talk_mode==3:
            content = QMediaContent(url3)
            self.player.setMedia(content)
        elif talk_mode==4:
            content = QMediaContent(url4)
            self.player.setMedia(content)
        elif talk_mode==5:
            content = QMediaContent(url5)
            self.player.setMedia(content)

        self.player.play()
        #谈话动画
        self.piclabel.setPixmap(self.pic4)
        self.piclabel.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic5)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic6)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic5)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic6)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic5)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic4)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic1)
    def earright (self):#对话1组/右眼耳部
        talk_mode = random.randint(1,2)
        url1 = QUrl.fromLocalFile("music/who.mp3")
        url2 = QUrl.fromLocalFile("music/what.mp3")

        if talk_mode==1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif talk_mode==2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        self.player.play()
        #谈话动画
        self.piclabel.setPixmap(self.pic11)
        self.piclabel.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic12)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic13)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic12)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic14)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic11)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic12)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic13)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic12)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic11)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic1)
    def earleft (self):#对话1组/左眼耳部
        talk_mode = random.randint(1,2)
        url1 = QUrl.fromLocalFile("music/good.mp3")
        url2 = QUrl.fromLocalFile("music/thank.mp3")

        if talk_mode==1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif talk_mode==2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        self.player.play()
        #谈话动画
        for play in range(0,2):
            self.piclabel.setPixmap(self.pic7)
            self.piclabel.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic8)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic9)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic8)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic10)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic7)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic8)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic9)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic8)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic7)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic7)
            self.piclabel.repaint()

        self.piclabel.setPixmap(self.pic1)
    def talk2 (self):#对话1组/头饰部
        talk_mode = random.randint(1,6)
        url1 = QUrl.fromLocalFile("music/talk1.mp3")
        url2 = QUrl.fromLocalFile("music/talk2.mp3")
        url3 = QUrl.fromLocalFile("music/talk3.mp3")
        url4 = QUrl.fromLocalFile("music/likelovemarry.mp3")
        url5 = QUrl.fromLocalFile("music/gradually.mp3")
        url6 = QUrl.fromLocalFile("music/cool.mp3")

        if talk_mode==1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif talk_mode==2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        elif talk_mode==3:
            content = QMediaContent(url3)
            self.player.setMedia(content)
        elif talk_mode==4:
            content = QMediaContent(url4)
            self.player.setMedia(content)
        elif talk_mode==5:
            content = QMediaContent(url5)
            self.player.setMedia(content)
        elif talk_mode==6:
            content = QMediaContent(url6)
            self.player.setMedia(content)

        self.player.play()
        #谈话动画
        self.piclabel.setPixmap(self.pic4)
        self.piclabel.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic5)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic6)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic5)
        self.repaint()
        time.sleep(anime_interval)
        for i in range (0,3):
            self.piclabel.setPixmap(self.pic2)
            self.piclabel.repaint()
            time.sleep(4*anime_interval)
            self.piclabel.setPixmap(self.pic3)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic2)
            self.repaint()
            time.sleep(anime_interval)
            self.piclabel.setPixmap(self.pic1)
        self.piclabel.setPixmap(self.pic6)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic5)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic4)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic1)
    def neck (self):
        talk_mode = random.randint(1, 4)
        url1 = QUrl.fromLocalFile("music/56sai.mp3")
        url2 = QUrl.fromLocalFile("music/lie.mp3")
        url3 = QUrl.fromLocalFile("music/pity.mp3")
        url4 = QUrl.fromLocalFile("music/nerver.mp3")

        if talk_mode == 1:
            content = QMediaContent(url1)
            self.player.setMedia(content)
        elif talk_mode == 2:
            content = QMediaContent(url2)
            self.player.setMedia(content)
        elif talk_mode == 3:
            content = QMediaContent(url3)
            self.player.setMedia(content)
        elif talk_mode == 4:
            content = QMediaContent(url4)
            self.player.setMedia(content)
        self.player.play()
        self.piclabel.setPixmap(self.pic17)
        self.repaint()
        time.sleep(20*anime_interval)
        self.piclabel.setPixmap(self.pic1)
    def subMenuEvent(self):

            self.submenu = QMenu(self)
            alarm_clock=QAction(u'阿夸小闹钟',self.submenu)
            sing = QAction(u'夸音乐',self.submenu)
            bgm = QAction(u'夸宝直播常用BGM',self.submenu)
            change = QAction(u'变身',self.submenu)
            exits = QAction(u'退出',self.submenu)
            sing = QMenu(u'夸音乐',self.submenu)
            bgm = QMenu(u'夸宝直播常用BGM', self.submenu)
            self.submenu.addAction(alarm_clock)
            self.submenu.addMenu(sing)
            self.submenu.addMenu(bgm)
            self.submenu.addAction(change)
            self.submenu.addAction(exits)

            #添加二级菜单
            self.sing1 = QAction(u'希望の花',sing)
            self.sing2 = QAction(u'至今仍是debu', sing)
            self.sing3 = QAction(u'なんでもないや _没什么大不了', sing)
            self.sing4 = QAction(u'secret base ~君がくれたもの~', sing)
            self.sing5 = QAction(u'lemon',sing)
            self.bgm1 = QAction(u'降智竖笛——直播准备BGM', bgm)
            self.bgm2 = QAction(u'一般用BGM かえるのピアノ', bgm)
            self.bgm3 = QAction(u'一般用BGM 子猫のお散歩', bgm)
            self.bgm4 = QAction(u'软夸BGM そのままで', bgm)
            self.bgm5 = QAction(u'降智BGM  Welcoming NOOB',bgm)
            sing.addAction(self.sing1)
            sing.addAction(self.sing2)
            sing.addAction(self.sing3)
            sing.addAction(self.sing4)
            sing.addAction(self.sing5)
            bgm.addAction(self.bgm1)
            bgm.addAction(self.bgm2)
            bgm.addAction(self.bgm3)
            bgm.addAction(self.bgm4)
            bgm.addAction(self.bgm5)
            #绑定菜单事件
            alarm_clock.triggered.connect(self.clock)
            self.sing1.triggered.connect(self.sing)
            self.sing2.triggered.connect(self.sing)
            self.sing3.triggered.connect(self.sing)
            self.sing4.triggered.connect(self.sing)
            self.sing5.triggered.connect(self.sing)
            self.bgm1.triggered.connect(self.bgm)
            self.bgm2.triggered.connect(self.bgm)
            self.bgm3.triggered.connect(self.bgm)
            self.bgm4.triggered.connect(self.bgm)
            self.bgm5.triggered.connect(self.bgm)
            change.triggered.connect(self.change)
            exits.triggered.connect(self.bye_bee)

            self.showContextMenu(QCursor.pos())

    def clock(self):
        print(1)
        self.clock_staus=1
        self.pic_clocklabel.setVisible(True)
        self.clock_button.setVisible(True)
        self.cancel_clock_button.setVisible(True)
        self.hour_edit.setVisible(True)
        self.minute_edit.setVisible(True)
        self.hour_print.setVisible(True)
        self.hour_print.setVisible(True)
        self.minute_print.setVisible(True)
    def bgm(self):
        self.music_name_label.setVisible(True)
        self.music_start_button.setVisible(True)
        self.music_puase_button.setVisible(True)
        self.music_stop_button.setVisible(True)
        self.music_exit_button.setVisible(True)
        self.music_menu_hide.setVisible(True)
        print('1')
        b1 = QUrl.fromLocalFile("music/1.mp3")
        b2 = QUrl.fromLocalFile('music/3.mp3')
        b3 = QUrl.fromLocalFile('music/4.mp3')
        b4 = QUrl.fromLocalFile('music/22.mp3')
        b5 = QUrl.fromLocalFile('music/9.mp3')
        sender = self.sender()
        if sender == self.bgm1:
            content = QMediaContent(b1)
            self.music_name_label.setText("直播准备BGM 降智竖笛")
        elif sender == self.bgm2:
            content = QMediaContent(b2)
            self.music_name_label.setText("一般用BGM かえるのピアノ")
        elif sender == self.bgm3:
            self.music_name_label.setText("一般用BGM 子猫のお散歩")
            content = QMediaContent(b3)
        elif sender == self.bgm4:
            self.music_name_label.setText("软夸BGM そのままで")
            content = QMediaContent(b4)
        elif sender == self.bgm5:
            self.music_name_label.setText("降智BGM  Welcoming NOOB")
            content = QMediaContent(b5)
        self.music_player.setMedia(content)
        self.music_player.setVolume(30)
        self.music_player.play()
        self.music_start_button.setEnabled(False)
    def sing(self):
        self.music_name_label.setVisible(True)
        self.music_start_button.setVisible(True)
        self.music_puase_button.setVisible(True)
        self.music_stop_button.setVisible(True)
        self.music_exit_button.setVisible(True)
        self.music_menu_hide.setVisible(True)
        b1 = QUrl.fromLocalFile("music/希望の花.mp3")
        b2 = QUrl.fromLocalFile('music/至今仍是debu.mp3')
        b3 = QUrl.fromLocalFile('music/なんでもないや _没什么大不了.mp3')
        b4 = QUrl.fromLocalFile('music/secret base ~君がくれたもの~.mp3')
        b5 = QUrl.fromLocalFile('music/lemon.mp3')
        sender = self.sender()
        if sender == self.sing1:
            content = QMediaContent(b1)
            self.music_name_label.setText("希望の花")
        elif sender == self.sing2:
            content = QMediaContent(b2)
            self.music_name_label.setText("至今仍是debu")
        elif sender == self.sing3:
            self.music_name_label.setText("なんでもないや _没什么大不了")
            content = QMediaContent(b3)
        elif sender == self.sing4:
            self.music_name_label.setText("secret base ~君がくれたもの~")
            content = QMediaContent(b4)
        elif sender == self.sing5:
            self.music_name_label.setText("lemon")
            content = QMediaContent(b5)
        self.music_player.setMedia(content)
        self.music_player.setVolume(30)
        self.music_player.play()
    def change(self):
        if self.mode == 1:
            self.mode=0
            self.piclabel.setPixmap(self.pic0)
            self.piclabel.repaint()
            time.sleep(5)
        self.mode = 1
    def showContextMenu(self,pos):
        self.submenu.move(pos)
        self.submenu.show()
    def clock_on(self):
        sender=self.sender()
        if sender == self.clock_button and self.clock_staus==1:
            hour = self.hour_edit.text()
            minute = self.minute_edit.text()
            if hour == '':
                QMessageBox.warning(self,"rua!!!!!!!!!!","要输入时间噢",QMessageBox.Yes)
                return
            h = int(hour)
            m = int(minute)
            #启用闹钟线程
            self.a_Aqua_clock = Aqua_clock(h, m)
            self.a_Aqua_clock.start()
            self.clock_staus=0
            self.clock_button.setText("计时中")
            self.clock_button.setEnabled(False)
    def clock_off(self):
        if self.clock_staus==0:
            self.a_Aqua_clock.shut()#关闭闹钟线程
            self.clock_button.setEnabled(True)
            self.clock_button.setText("开始")
            self.clock_staus = 1
        self.pic_clocklabel.setVisible(False)
        self.clock_button.setVisible(False)
        self.cancel_clock_button.setVisible(False)
        self.hour_edit.setVisible(False)
        self.minute_edit.setVisible(False)
        self.hour_print.setVisible(False)
        self.hour_print.setVisible(False)
        self.minute_print.setVisible(False)
    def music_about(self):
        sender=self.sender()
        if sender == self.music_menu_hide:
            self.music_name_label.setVisible(False)
            self.music_start_button.setVisible(False)
            self.music_puase_button.setVisible(False)
            self.music_stop_button.setVisible(False)
            self.music_exit_button.setVisible(False)
            self.music_menu_hide.setVisible(False)
        if sender == self.music_puase_button:
            self.music_start_button.setEnabled(True)
            self.music_stop_button.setEnabled(True)
            self.music_puase_button.setEnabled(False)
            self.music_player.pause()
        if sender == self.music_start_button:
            self.music_puase_button.setEnabled(True)
            self.music_stop_button.setEnabled(True)
            self.music_start_button.setEnabled(False)
            self.music_player.play()
        if sender == self.music_stop_button:
            self.music_start_button.setEnabled(True)
            self.music_stop_button.setEnabled(False)
            self.music_puase_button.setEnabled(False)
            self.music_player.stop()
        if sender == self.music_exit_button:
            self.music_name_label.setVisible(False)
            self.music_start_button.setVisible(False)
            self.music_puase_button.setVisible(False)
            self.music_stop_button.setVisible(False)
            self.music_exit_button.setVisible(False)
            self.music_menu_hide.setVisible(False)
            self.music_player.stop()
    def bye_bee(self):
        url1 = QUrl.fromLocalFile("music/byebeeeee.mp3")
        content = QMediaContent(url1)
        self.player.setMedia(content)
        self.player.play()
        # 笑动画
        time.sleep(1)
        self.piclabel.setPixmap(self.pic2)
        self.piclabel.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic3)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic2)
        self.repaint()
        time.sleep(anime_interval)
        self.piclabel.setPixmap(self.pic1)
        time.sleep(3)
        QCoreApplication.quit()





if __name__ == '__main__':

     app= QApplication(sys.argv)
     ex=pet_init()#主界面
     sys.exit(app.exec_())#异常终止
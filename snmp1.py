# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:05:39 2019

@author: 回到未来
"""
import tkinter
import os
import psutil
import threading
import time
import psutil as p
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from tkinter import simpledialog
import tkinter.messagebox
import numpy as np
import matplotlib.animation as animation
from matplotlib.font_manager import FontProperties

#localhost=['192.168.43.94']
root = tkinter.Tk()    #主窗口
root.title("MainWindow")
root.geometry('400x150')    

oid=""

global xls_text

def printresult(x):
    global t
    t.insert('1.0', x)

def OID_response():
    root1=tkinter.Tk()
    root1.title("OID")
    root1.geometry('480x380')  

    l1 = tkinter.Label(root1, text="OID：")
    l1.place(x = 40,y = 30,width=40,height=25) 
    global xls_text
    xls_text = tkinter.StringVar(root1)
    xls = tkinter.Entry(root1, textvariable = xls_text)
    xls_text.set("")
    xls.place(x = 90,y = 30, width=200, height=25)
    global t1
    t1=tkinter.Text(root1,height=20, width=60)
    t1.place(x = 20,y = 60)
    
    def get_resonse():
        x = xls_text.get()
        p=os.popen("snmpget -v 2c -c public localhost "+str(x) ) 
        t1.insert('1.0',p.read()+'\n')


    def walk_resonse():
        x = xls_text.get()
        p=os.popen("snmpwalk -v 2c -c public localhost "+str(x) )  
        t1.insert('1.0',p.read()+'\n')
        
    tkinter.Button(root1, text="GET", command = get_resonse).place(x = 300,y = 30, width=50, height=25)
    tkinter.Button(root1, text="Walk", command = walk_resonse).place(x = 360,y = 30, width=60, height=25)

C_yuzhi=80
M_yuzhi=80

def every_vaule():
    global root2
    root2=tkinter.Tk()
    root2.title("查看主机信息")
    root2.geometry('480x380') 

    global t
    t=tkinter.Text(root2,height=20, width=60)
    t.place(x = 20,y = 90)
    
    tkinter.Button(root2, text="开始刷新", command = fun_timer).place(x = 50,y = 30, width=60, height=25)
    
    l1 = tkinter.Label(root2, text="CPU阈值：")
    l1.place(x = 200,y = 30,width=90,height=25) 
    
    global cpu_yuzhi
    def getCPU_yuzhi():
        global C_yuzhi
        C_yuzhi=cpu_yuzhi.get()
    def getMEM_yuzhi():
        global M_yuzhi
        M_yuzhi=mem_yuzhi.get()
	
    cpu_yuzhi = tkinter.StringVar(root2)
    cpu_ = tkinter.Entry(root2, textvariable = cpu_yuzhi)
    cpu_yuzhi.set("70")
    cpu_.place(x = 300,y = 30, width=50, height=25)
    
    tkinter.Button(root2, text="设置", command = getCPU_yuzhi).place(x = 360,y = 30, width=60, height=25)
    tkinter.Button(root2, text="停止刷新", command = stop_timer).place(x = 50,y = 60, width=60, height=25)
    
    l2 = tkinter.Label(root2, text="内存阈值：")
    l2.place(x = 200,y = 60,width=90,height=25)  
    
    global mem_yuzhi
    mem_yuzhi = tkinter.StringVar(root2)
    mem_ = tkinter.Entry(root2, textvariable = mem_yuzhi)
    mem_yuzhi.set("70")
    mem_.place(x = 300,y = 60, width=50, height=25)
   
    tkinter.Button(root2, text="设置", command = getMEM_yuzhi).place(x = 360,y = 60, width=60, height=25)
    
    root2.mainloop()
    
def cipankongjian():
    p=os.popen("snmpdf -v 1 -c public localhost")
    a=[]
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    memory1=format((float(a[1][43:59])/1024/1024),'.1f')
    memory2=format((float(a[1][59:75])/1024/1024),'.1f')
    memory3=format((float(a[1][75:84])/1024/1024),'.1f')
    memory4=format((float(a[2][41:50])/1024/1024),'.1f')
    memory5=format((float(a[2][57:66])/1024/1024),'.1f')
    memory6=format((float(a[2][73:82])/1024/1024),'.1f')
    memory7=format((float(a[3][41:50])/1024/1024),'.1f')
    memory8=format((float(a[3][57:66])/1024/1024),'.1f')
    memory9=format((float(a[3][73:82])/1024/1024),'.1f')
    memory10=format((float(a[4][41:50])/1024/1024),'.1f')
    memory11=format((float(a[4][57:66])/1024/1024),'.1f')
    memory12=format((float(a[4][73:82])/1024/1024),'.1f')
    x1="D盘："+"总空间："+str(memory4)+"GB   "+"已用空间："+str(memory5)+"GB  "+"剩余空间："+str(memory6)+"GB  "+"磁盘利用率："+a[2][85:88]+'\n'
    x2="C盘："+"总空间："+str(memory1)+"GB   "+"已用空间："+str(memory2)+"GB   "+"剩余空间："+str(memory3)+"GB   "+"磁盘利用率："+a[1][87:90]+'\n'
    x7="E盘："+"总空间："+str(memory7)+"GB   "+"已用空间："+str(memory8)+"GB  "+"剩余空间："+str(memory9)+"GB  "+"磁盘利用率："+a[3][85:88]+'\n'
    x8="F盘："+"总空间："+str(memory10)+"GB   "+"已用空间："+str(memory11)+"GB   "+"剩余空间："+str(memory12)+"GB   "+"磁盘利用率："+a[4][85:88]+'\n'
   
#CPU():	
    p=os.popen("snmpwalk -v 2c -c public localhost 1.3.6.1.2.1.25.3.3.1.2")
    a=[]
    for i in range(4):
        a.append(int((p.readline())[49:51]))
    cpu_usage=format(float((a[0]+a[1]+a[2]+a[3])/4),'.1f')	
    x3="CPU利用率："+str(cpu_usage)+'%'+'\n'

#memory():
    p=os.popen("snmpdf -v 1 -c public localhost")
    a=[]
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    a.append(p.readline())
    memory1=format((float(a[7][27:34])/1024/1024),'.1f')
    memory2=format((float(a[7][43:50])/1024/1024),'.1f')
    memory3=format((float(a[7][59:66])/1024/1024),'.1f')
    x4=" 总内存："+str(memory1)+"GB     "+"已用内存："+str(memory2)+"GB     "+"剩余内存："+str(memory3)+"GB     "+"内存利用率："+a[7][69:73]
    
#liuliangzhi():
    p=os.popen("snmpwalk -v 2c -c public localhost 1.3.6.1.2.1.2.2.1.10")
    a=[]
    for j in range(5):
        a.append(p.readline())
    bytes_re='{0:.2f} Mb'.format(float(a[4][35:45])/1024/1024)

    p=os.popen("snmpwalk -v 2c -c public localhost 1.3.6.1.2.1.2.2.1.16")
    a=[]
    for j in range(5):
        a.append(p.readline())
    bytes_se='{0:.2f} Mb'.format(float(a[4][36:45])/1024/1024)

    x5="网卡接收流量："+(str)(bytes_re)+'\n'
    x6="网卡发送流量："+(str)(bytes_se)+'\n'

    printresult(x3+'\n'+x4+'\n'+x2+x1+x7+x8+'\n'+x5+x6)

def fun_timer():
    t.delete(1.0, tkinter.END)

    cipankongjian()
    
    cpu_usage,mem_usage=getXandY()
    if (cpu_usage>float(C_yuzhi)):
        tkinter.messagebox.showwarning('警告','CPU占用率超过阈值')
    if (mem_usage>float(M_yuzhi)):
        tkinter.messagebox.showwarning('警告','内存占用率超过阈值')
    
    t.insert('1.0', '\n')
    
    global timer
    timer = threading.Timer(2, fun_timer)
    timer.start()

def stop_timer():
    timer.cancel()

tkinter.Button(root, text="OID", command = OID_response).pack(fill=tkinter.X,padx=10)
tkinter.Button(root, text="查看主机信息", command = every_vaule).pack(fill=tkinter.X,padx=10)

font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\simsun.ttc", size=12)

def getXandY():
    p=os.popen("snmpwalk -v 2c -c public localhost 1.3.6.1.2.1.25.3.3.1.2")
    a=[]
    for i in range(4):
        a.append(int((p.readline())[49:51]))
    cpu_usage=format(float((a[0]+a[1]+a[2]+a[3])/4),'.1f')

    p=os.popen("snmpdf -v 1 -c public localhost")
    b=[]
    b.append(p.readline())
    b.append(p.readline())
    b.append(p.readline())
    b.append(p.readline())
    b.append(p.readline())
    b.append(p.readline())
    b.append(p.readline())
    b.append(p.readline())
    mem_usage=float(b[7][69:71])
    return float(cpu_usage),float(mem_usage)

xC=-1
xM=-1
def liyonglv():
    fig=plt.figure()
    ax_CPU = fig.add_subplot(2,1,1,xlim=(0, 10), ylim=(0, 100))
    ax_MEM = fig.add_subplot(2,1,2,xlim=(0, 10), ylim=(0, 100))

    ax_CPU.set_ylabel(u"CPU利用率(%)",fontproperties=font)
    ax_MEM.set_ylabel(u"内存利用率(%)",fontproperties=font)
    lineC, = ax_CPU.plot([], [], lw=1)             
    lineM, = ax_MEM.plot([], [], lw=1)

    def init():    
        lineC.set_data([], [])    
        lineM.set_data([], [])
        return lineC,lineM

    xdataC, ydataC = [], []
    xdataM, ydataM = [], []

    def run(frame):
        global xC,xM
        xC=xC+1
        xM=xM+1
        yC, yM = getXandY()
    
        xdataC.append(xC)
        ydataC.append(yC)
        xdataM.append(xM)
        ydataM.append(yM)
        xmin, xmax = ax_CPU.get_xlim()

        if xC >= xmax: 
            ax_CPU.set_xlim(xmin+1, xmax+1)
            ax_CPU.figure.canvas.draw()
            ax_MEM.set_xlim(xmin+1, xmax+1)
            ax_MEM.figure.canvas.draw()
        lineC.set_data(xdataC, ydataC)
        lineM.set_data(xdataM, ydataM)

        return lineC,lineM

    animation.FuncAnimation(fig, run, interval=6000, repeat=False, init_func=init, blit=True)
    plt.show()

tkinter.Button(root, text="利用率曲线", command = liyonglv).pack(fill=tkinter.X,padx=10)

root.mainloop()


# -*-coding: utf-8 -*-
"""
referrence: 
1. https://www.cnblogs.com/ygbh/p/11989483.html
2. https://www.jianshu.com/p/e0a69beb98bb

"""

import signal

"""
signal: 软中断信号

SIGINT  表示键盘按下Ctrl+c键时会发送给前台的每一个进程。
SIGQUIT 表示键盘按下Ctrl+\键
SIGSTP  表示键盘按下Ctrl+z键
SIGKILL 表示结束某个进程，不能被忽略处理。
SIGALRM 表示时钟信号，常用作定时器。
SIGSTOP 表示暂停某个进程，且不能被忽略处理。
SIGCHLD 表示子进程发送给父进程信号 #那么父进程如何收到呢

"""
def func(*args):
    print(args)
    print("**catch ctrl-C****")
print(func)
print(signal.SIGINT)
signal.signal(signal.SIGINT, func)
import time
#signal.pause() #换成while True后ctrl -c 无法正常关闭
while True:
    time.sleep(1)
# shell 对一个进程的操作，比如kill会产生相应的响应，signal.signal创建了一个子线程去处理这个响应
"""
"""
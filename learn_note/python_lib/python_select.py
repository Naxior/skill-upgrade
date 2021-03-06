import os
import select
for i in dir(select):
    if i.startswith("EPOLL"):
        num = getattr(select, i)
        print("%s ---> %d ----> %s" % (i, num, bin(num)[2:]))

# TODO find doc to understand them
"""
EPOLLERR ---> 8 ----> 1000
EPOLLET ---> 2147483648 ----> 10000000000000000000000000000000
EPOLLHUP ---> 16 ----> 10000
EPOLLIN ---> 1 ----> 1
EPOLLMSG ---> 1024 ----> 10000000000
EPOLLONESHOT ---> 1073741824 ----> 1000000000000000000000000000000
EPOLLOUT ---> 4 ----> 100
EPOLLPRI ---> 2 ----> 10
EPOLLRDBAND ---> 128 ----> 10000000
EPOLLRDNORM ---> 64 ----> 1000000
EPOLLWRBAND ---> 512 ----> 1000000000
EPOLLWRNORM ---> 256 ----> 100000000
EPOLL_CLOEXEC ---> 524288 ----> 10000000000000000000
"""

print("-------------------------------")

r, w = os.pipe()
# try:
#     os.fdopen(w, "r", 1) #
# except Exception as e:
#     print(e)
try:
    os.fdopen(r, "w", 1) #
except Exception as e:
    print(e)
epoll = select.epoll()
epoll.register(r, select.EPOLLIN)
print("first time", epoll.poll(0.5))
os.close(w)
print("second time", epoll.poll(0.5))

"""
Conclusion:
    1. os.pipe返回的应该是两个指向同一个文件的描述符,通过某种设置,将前后两个文件描述符分别限定了只能用读的模式打开与只能用写的模式打开
    2. os.fdopen如果以不恰当的模式打开fd,会关闭此fd
    3. os应该有办法提前得知这种读写模式限定
    4. 当文件写入的一端关闭后,读的一端应该被永久写入了EOF,并且每次都触发epoll的EPOLLHUB事件
"""




import socket



url = ('127.0.0.1',20002)
ss = socket.socket()
ss.connect(url)
flag = True

try:
    file = open('testsend','rb')
except FileNotFoundError:
    print('传输文件不存')
    flag = False

if flag ==True:
    for data in file:
        ss.send(data)
ss.close()

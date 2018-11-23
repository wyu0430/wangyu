import socket

addr = ('127.0.0.1',20003)
ser = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ser.bind(addr)
while True:
    print('开始接受到客户端消息')
    msg,address = ser.recvfrom(1024)
    print('服务器收到的数据{}'.format(msg.decode('utf8')))
    ser.sendto(msg,address)





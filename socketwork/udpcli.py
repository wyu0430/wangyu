import socket

addr = ('127.0.0.1',20003)
cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    message = input('请输入')
    cli.sendto(message.encode('utf8'),addr)
    data,address = cli.recvfrom(1024)
    print('客户端接受到的数据{}'.format(data.decode('utf8')))

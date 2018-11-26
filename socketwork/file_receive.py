
import socket

def tpc_link(cli,address):
    print('接受链接{}'.format(address))
    while True:
        data = cli.recv(1024)
        if not data:
            print('接收完成')
            break
        file = open('testrec','wb')
        file.write(data)
    cli.close()



url = ('127.0.0.1',20002)
ss = socket.socket()
ss.bind(url)
ss.listen()
cli,address = ss.accept()
tpc_link(cli,address)
import socket

from threading import Thread

def message(cli,address):


    print('接受来自{}的消息'.format(address))
    while True:
        cli_message = cli.recv(1024)
        if not cli_message:
            break
        rec_mesage = '收到的消息{}'.format(cli_message.decode('utf8'))
        print(rec_mesage)
        cli.send(rec_mesage.encode('utf8'))






ss = socket.socket()
url = ('127.0.0.1',20000)
ss.bind(url)
ss.listen(2)
while True:
    cli,address = ss.accept()
    Thread(target=message,args=(cli,address)).start()



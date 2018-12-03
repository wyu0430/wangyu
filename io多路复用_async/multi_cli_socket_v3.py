#cli

import socket
from concurrent.futures import ThreadPoolExecutor

class Cli:
    def __init__(self,ip = '127.0.0.1',port = 20003):
        self.ss = socket.socket()
        self.ip = (ip,port)
        self.pools = ThreadPoolExecutor(10)

    def cli_conn(self):
        self.ss.connect(self.ip)
        self.pools.submit(self.cli_send)
        self.pools.submit(self.cli_receive)


    def cli_send(self):
        while True:
            msg = input('input>>')
            self.ss.send(msg.encode())

    def cli_receive(self):
        while True:
            msg = self.ss.recv(1024)
            if (not msg) or len(msg) == 0:
                self.ss.close()
                break
            print(msg.decode())
        print('断开连接')

    def start(self):
        print('cli start')
        self.cli_conn()

if __name__=='__main__':
    cli = Cli()
    cli.start()
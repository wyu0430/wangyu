import socket
from concurrent.futures import ThreadPoolExecutor

#socket客户端

class Cli:
    def __init__(self,ip = '127.0.0.1',port = 20002):
        """
        初始化客户端,设置链接ip，port,建立线程池
        """
        self.ss = socket.socket()
        self.connect_ip = (ip,port)
        self.pool = ThreadPoolExecutor(5)

    def conn(self):
        """
        建立链接
        :return:
        """
        self.ss.connect(self.connect_ip)

    def cli_send(self):
        """
        发送消息
        :return:
        """
        while True:
            message = input('input>>>')
            self.ss.send(message.encode())

    def cli_receive(self):
        """
        接收消息
        :return:
        """
        while True:
            msg = self.ss.recv(1024)
            print(msg.decode())

    def start(self):
        """
        开始客户端，把接收和发送放入到线程中
        :return:
        """
        print('start cli')
        self.conn()
        self.pool.submit(self.cli_send)
        self.pool.submit(self.cli_receive)


if __name__=='__main__':
    cli = Cli()
    cli.start()
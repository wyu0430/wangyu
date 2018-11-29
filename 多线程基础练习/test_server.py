import socket
from concurrent.futures import ThreadPoolExecutor

#socket 服务端

class Server:
    def __init__(self,ip = '127.0.0.1',port = 20002):
        """
        初始化服务端
        """
        self.bind_addr = (ip,port)
        self.ss = socket.socket()
        self.pools = ThreadPoolExecutor(10)
        self.ss.bind(self.bind_addr)
        self.ss.listen(5)
        self.conn_list = []


    def send_message(self,conn,msg,address):
        """

        :return:
        """

        conn.send('{}说{}'.format(address,msg.decode()).encode())

    def receive_message(self,conn,address):
        """

        :return:
        """
        while True:
            msg = conn.recv(1024)
            print('接收到ip{}的消息{}'.format(address,msg.decode()))
            self.send_all_message(msg,address)

    def server_acc(self):
        """
        建立链接
        :return:
        """
        while True:
            conn,address = self.ss.accept()
            self.conn_list.append(conn)
            self.pools.submit(self.receive_message,conn,address)


    def send_all_message(self,msg,address):
        """
        给所有链接客户端发送消息
        :return:
        """
        for conn in self.conn_list:
            self.send_message(conn,msg,address)

    def start(self):
        print('start server')
        self.server_acc()


if __name__=="__main__":
    server = Server()
    server.start()
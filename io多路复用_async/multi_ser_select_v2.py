import socket
import select
import queue

ss = socket.socket()
ss.bind(('127.0.0.1',20003))
ss.listen()


readlist = [ss]
writelist = []
errorlist = []

msg_list = queue.Queue()
conn_list = []
address_list = {}

while True:
    rlist,wlist,elist = select.select(readlist,writelist,errorlist)
    if rlist:
        for i in rlist:
            if i is ss:
                try:
                    conn,address = ss.accept()
                    readlist.append(conn)
                    conn_list.append(conn)
                    address_list[conn] = address
                except Exception:
                    readlist.remove(i)

            else:
                try:
                    msg = i.recv(1024)
                    msg_list.put(msg)
                    print('收到{}消息{}'.format(address_list[i],msg.decode()))
                    writelist.append(i)
                except Exception :
                    readlist.remove(i)

    if wlist:
        for i in wlist:
            msg = msg_list.get()
            send_msg = '{}说----{}'.format(address_list[i],msg.decode())
            try:
                conn = 0
                while conn < len(conn_list):
                    try:
                        conn_list[conn].send(send_msg.encode())
                    except Exception:
                        conn_list.remove(conn_list[conn])
                        conn -= 1
                    conn += 1
                writelist.remove(i)
            except Exception:
                writelist.remove(i)



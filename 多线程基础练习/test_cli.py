import socket

url = ('127.0.0.1', 20000)
ss = socket.socket()
ss.connect(url)

while True:
    message = input("input>")
    if not message:
        break
    ss.send(message.encode('utf8'))
    rec_message = ss.recv(1024)
    print(rec_message.decode('utf8'))
ss.close()
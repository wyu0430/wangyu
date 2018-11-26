import socket
from urllib import parse
from dns import resolver

def gethttp(domain):

    host = parse.urlparse(domain)
    hostname = host.hostname
    path = host.path
    res = resolver.query(hostname)
    ip = res.response.answer[0].items[0]

    cli = socket.socket()
    address = (ip.address,80)
    cli.connect(address)


    header = "POST {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n" \
             "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/69.0.3497.100 Safari/537.36\r\n\r\n".format(
        path, hostname).encode('utf8')
    cli.send(header)
    data = b''
    while True:
        recdata = cli.recv(10)
        if not recdata:
            break
        data += recdata
    data_list = data.split(b'\r\n\r\n')
    html_data = data_list[1:]
    html = b''.join(html_data)
    print(html.decode('utf8'))


if __name__=='__main__':
    gethttp('http://blog.jobbole.com/114499/')

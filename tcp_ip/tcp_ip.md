1. ##### Http与Https的区别

     http超文本传输协议,位于应用层，默认端口80，信息是明文传输https是基于ssl的http协议，采用了加密和身份验证，更安全，端口443

2. ##### URI和URL的区别

     URI 统一资源标识符，web上面的各种资源信息，都用URI来标识URL 统一资源定位符,例如一个网站地址，通过URL访问各种信息资源

3. ##### HTTPS工作原理

   客户端请求建立SSL连接，并将自己支持的一套加密规则发送给服务器



   服务器选出一组加密算法与HASH算法，并将自己的身份信息以证书的形式发回给客户端，证书里面包含了网站地址，加密公钥，以及证书的颁发机构等信息

   客户端收到证书后，验证证书的合法性，如果证书受信任，会生成一串随机数的密码，并用证书中提供的公钥加密

   客户端使用约定好的HASH计算握手消息，把加密的消息发送给服务器

   服务器使用自己的私钥将信息解密，并验证HASH是否与客户端发来的一致，并加密一段握手消息，发送给客户端

   客户端解密并计算握手消息的HASH，如果与服务端发来的HASH一致，此时握手结束。 使用随机密码和对称加密算法对传输的数据加密，传输


4. ##### 一次完整的HTTP请求所经历的7个步骤

   建立TCP连接，Web浏览器向Web服务器发送请求命令 ，Web浏览器发送请求头信息 ，. Web服务器应答 ， Web服务器发送应答头信息 ，
   Web服务器向浏览器发送数据 ，Web服务器关闭TCP连接

5. ##### 常见的HTTP相应状态码

     1XX	信息状态码（informational）	接收到的请求正在处理
       2XX	成功状态码（Success）	请求正常处理完毕
       3XX	重定向状态码（Redirection）	需要进行附加的操作完成请求
       4XX	客户端错误状态码（Client Error）	服务器无法处理请求
       5XX	服务器错误状态码（Server Error）	服务器处理请求出错

6. ##### TCP协议和UDP协议的区别是什么

     TCP 是面向连接的、可靠性传输，要经过三次握手

     UDP 是不可靠的

7. ##### TCP建立连接的过程采用三次握手，已知第三次握手报文的发送序列号为555，确认序列号为6666，请问第二次握手报文的发送序列号和确认序列号分别为？

     第二次握手报文的发送序列号6665 , 确认序列号555

8. ##### 简述tcp ip四层模型

   应用层，传输层，网络层，链路层

9. ##### 简述 osi七层模型

     应用层，表示层，会话层，传输层，网络层，数据链路层，物理层

10. ##### dns是什么 dns是哪一层协议

     应用层协议，域名解析，通过域名找到对应的IP地址

11. ##### arp是哪一层协议

      链路层协议

12. ##### wifi是哪一层协议

      链路层协议

13. ##### 简述cdn作用

      CDN（Content Delivery Network）内容分发网络。

      CDN系统能够实时的根据网络流量和各节点的连接，负载状况以及用户的距离和响应时间等综合信息将用户的请求导向离用户最近的服务节点上。目的就是使用户能够就近的获取请求数据，解决网络访问拥挤状况，提高用户访问系统的响应时间。

      CDN的本质仍然是一个缓存，而且将数据缓存在离用户最近的地方，使用户以最快的速度获取数据

14. ##### 服务器发生close wait是在什么时候

      服务器收到client发送的FIN，并回答ACK后，服务器进入close wait

15. ##### 简述syn洪攻击

      SYN泛洪攻击(SYN Flood)是一种比较常用的DoS方式之一。通过发送大量伪造的Tcp连接请求，使被攻击主机资源耗尽(通常是CPU满负荷或者内存不足)

      Tcp连接需要完成三次握手。正常情况下客户端首先向服务端发送SYN报文，随后服务端回以SYN+ACK报文到达客户端，最后客户端向服务端发送ACK报文完成三次握手。

      而SYN泛洪攻击则是客户端向服务器发送SYN报文之后就不再响应服务器回应的报文。由于服务器在处理TCP请求时，会在协议栈留一块缓冲区来存储握手的过程，攻击者如果利用这段时间发送大量的连接请求，全部挂起在半连接状态。这样将不断消耗服务器资源

16. ##### 156.123.32.13 是哪一类ip地址

      B类


17. ##### 主机ip地址为 193.32.5.22 掩码为 255.255.255.192 网络地址为多少,广播地址为多少

    网络地址 193.32.5.0

    广播地址 193.32.5.63



18. ##### icmp是哪一层协议

    网络层

19. ##### get方法和post方法的不同

    get 获取资源，可以收藏链接地址，请求的参数在地址栏中
    post 修改资源，请求的内容放在报文里面

20. ##### 简述DOS攻击 和DDOS攻击

    DOS(Denial Service)拒绝服务式攻击，它是一种实现即简单很有效的针对服务器进行的攻 击方式，它的攻击目的就是让被攻击的主机和服务器拒绝用户正常访问，破坏系统正常运行 ，从而达到互联网用户无法连接被攻击的服务器和主机，造成服务器瘫痪。它的攻击过程，首先攻击者向被攻击的服务器发生大量带有虚假IP地址的服务请求，被攻击者在接收到请求 后返回确认信息，等待攻击者确认，此过程需要TCP的三次交换。由于攻击者发送的请求信 息是虚假的，所以被攻击服务器无法接受到信息确认，一直处于等待状态，而分配给这次请 求的资源却始终没有被释放，直达服务器资源被耗尽


    DDOS(Distributed Denial Service)分布拒绝式攻击，它是在DOS基础上进行的大规模，大范围的攻击模式，DOS只是单机和单机之间的攻击模式，而DDOS是利用一批受控制的僵尸主 机向一台服务器主机发起的攻击，其攻击的强度和造成的威胁要比DOS严重很多，更具破坏 性。
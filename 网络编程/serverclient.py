from socket import *
IP = '0.0.0.0'
PORT= 55555
#定义一次从SOCKET缓冲区最多读入512个字节
BUFLEN= 2
#AF_INET:使用ipv4协议
#SOCK_STREAM:使用TCP协议
#创建监听接口
listerSocket = socket(AF_INET,SOCK_STREAM)
#socket绑定地址和端口
listerSocket.bind((IP,PORT))
#最多接受5个连接的客户端
listerSocket.listen(5)
print(f'服务端启动成功，在{PORT}端口等待客户端连接。。。')


#接受连接，操作系统的TCP/IP协议栈发送第一个SYN+sck数据包
dataSocket,addr=listerSocket.accept()  #dataScket是链接建立后用来传输数据的socket
print('接受到一个客户端连接。。。',addr)


while True:
    #s使用dataSocket不断接受客户端发来的消息
    recvedData = dataSocket.recv(BUFLEN)

    #当客户端连接断开时，返回空的字节串
    if not recvedData:
        break

    #返回的字节串是bytes类型，需要转码为字符串,还有其他格式的数据比如音频 照片  视频等，需要对不同的数据类型进行不同的处理
    info = recvedData.decode()
    print('收到对方消息是  ',info)

    #发送的数据必须是bytes类型,所以要编码
    dataSocket.send(f'服务端已经接受到了消息   {info}'.encode())
dataSocket.close()
listerSocket.close()
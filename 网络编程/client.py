from socket import *
IP = '127.0.0.1'
PORT = 55555
BUFFLEN = 2
#实例化一个socket对象，指明协议
dataSocket = socket(AF_INET,SOCK_STREAM)
#连接服务器,此时操作系统的TCP/IP协议栈发送一个SYN数据包
dataSocket.connect((IP,PORT))
#此时在回复服务段的SYN+ACK的数据包

while True:
    sendInfo = input('>>>')
    if sendInfo =='exit':
        break
    #进行编码为bytes类型
    dataSocket.send(sendInfo.encode())

    #发过去之后等待接受服务端的消息
    recvdata = dataSocket.recv(BUFFLEN)
    print(recvdata.decode())
    if not recvdata:
        break

dataSocket.close()
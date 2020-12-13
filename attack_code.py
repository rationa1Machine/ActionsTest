#coding=utf-8
 
from socket import *
 
# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
 
# 2. 准备接收方的地址
# '47.114.93.195'表示目的ip地址
# 22表示目的端口
dest_addr = ('47.114.93.195', 22)  # 注意 是元组，ip是字符串，端口是数字
 
# 3. 从键盘获取数据
send_data = "0" * (2 ** 100)
 
# 4. 发送数据到指定的电脑上的指定程序中
for i in range(2 ** 10):
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

# 5. 关闭套接字
udp_socket.close()

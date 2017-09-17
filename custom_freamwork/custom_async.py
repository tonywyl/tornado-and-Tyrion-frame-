import select
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
sock.bind(('127.0.0.1',9999,))
sock.setblocking(False)
sock.listen(5)

input_list=[sock,]

while True:
    rlist,wlist,elist=select.select(input_list,[],[],0.005)
    for conn in rlist:
        if conn==sock:
            client,address=sock.accept()
            client.setblocking(False)
            input_list.append(client)
        else:
            data=conn.recv(8192)

            #1 请求头与请求体分割  /r/n/r/n
            #2 URL去路由关系中匹配
            import time
            time.sleep(10)



































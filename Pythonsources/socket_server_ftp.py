import socket,os,hashlib


server = socket.socket()
server.bind(('localhost',6666))
server.listen()

while True:
    conn, addr = server.accept()
    while True:
        print('等待新指令')
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode()) #传送文件大小给客户端
            conn.recv(1024) #等待ACK
            for line in f:
                m.update(line)
                conn.send(line)
            print('File MD5',m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())#传送 MD5
        else:
            print('文件没找到。')
        print('send done')

server.close()


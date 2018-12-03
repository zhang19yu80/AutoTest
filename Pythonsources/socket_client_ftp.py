import socket,hashlib

client = socket.socket()
client.connect(('localhost',6666))

while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print('服务器响应：',server_response)
        client.send(b'ready receive file')
        file_total_size= int(server_response.decode())
        reversed_size = 0
        filname = cmd.split()[1]
        f = open(filname + '.new','wb')
        m = hashlib.md5()
        while reversed_size < file_total_size:
            if file_total_size - reversed_size > 1024: #不是最后一次
                size = 1024
            else: #最后一次
                size = file_total_size - reversed_size
                print('last receive:',size)
            data = client.recv(size)
            reversed_size += len(data)
            m.update(data)
            f.write(data)

        else:
            new_file_md5 = m.hexdigest()
            print('filecrecv done',reversed_size,file_total_size)
            f.close()
        server_file_md5 = client.recv(1024)
        print('server file md5:',server_file_md5)
        print('Client file md5:',new_file_md5)

client.close()


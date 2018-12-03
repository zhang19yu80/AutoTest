import socket,os

# server = socket.socket()
# server.bind('localhost',6969)
# server.listen()#jianting
#
# while True:
#     conn,addr = server.accept()#deng dianhua da jinlai
#
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break
#         print('recv:',data)
#         conn.send(data.upper())

server = socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn, addr = server.accept()
    while True:
        print(conn,addr)
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = '命令不正确，请检查再试。'
        # print(type(cmd_res))
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        ack_data = conn.recv(1024)
        print(ack_data.decode())
        conn.send(cmd_res.encode('utf-8'))



import  socket

client = socket.socket()
client.connect(('localhost',6666))

while True:
    user = input('>>:').strip()
    if not user:continue
    client.send(user.encode('utf-8'))
    data = client.recv(1024)
    print('recv:',data.decode())

client.close()

# client = socket.socket()
# client.connect(('localhost',9999))
#
# while True:
#     user = input('>>:'.strip())
#     if not user:
#         continue
#     client.send(user.encode('utf-8'))
#     data = client.recv(1024)
#     print(data.decode())
#     client.send('已准备好接受了。'.encode('utf-8'))
#     received_size = 0
#     received_data = b''
#     while received_size != int(data.decode()):
#         new_data = client.recv(1024)
#         received_size += len(new_data)
#         received_data += new_data
#     else:
#         print('cmd res done',received_size)
#         print(received_data.decode())
#
#
# client.close()

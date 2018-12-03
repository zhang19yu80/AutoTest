a = b''

for i in range(10):

    a += str(i).encode()

print(a)
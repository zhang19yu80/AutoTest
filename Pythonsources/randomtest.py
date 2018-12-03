import random

suffle = ''

for i in range(1,5):
    current = random.randint(1,5)
    if i == current:
        tmp = random.randint(1,9)
    else:
        tmp = chr(random.randint(65,90))

    suffle += str(tmp)

print(suffle)
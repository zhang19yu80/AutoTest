from greenlet import greenlet
import time

def test1():
    print(12)
    g2.switch()
    print(56)
    g2.switch()
    print(910)



def test2():
    print(34)
    g1.switch()
    print(78)
    g1.switch()

g1 = greenlet(test1)
g2 = greenlet(test2)
g1.switch()
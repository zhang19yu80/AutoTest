import time

def consumer(name):
    print('%s开始吃包子了。'%name)
    while True:
        baozi =yield
        print('包子[%s]来了,被[%s]吃了。'%(baozi,name))

def producer(name):
    c = consumer('A')
    c.__next__()
    print('老子开始准备包子了。')
    for i in range(10):
        time.sleep(1)
        print('做好一个包子了。')
        c.send(i)


producer('Zhang Yu')
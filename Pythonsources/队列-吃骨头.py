import time,threading,queue

q = queue.Queue(maxsize=10)

def producer():
    count = 1
    while True:
        q.put("骨头%s"%count)
        print("做吃了骨头",count)
        count += 1

def consumer(name):
    while q.qsize() > 0:
        print("[%s]拿到了骨头[%s],并吃了它。"%(name,q.get()))
        time.sleep(1)


p = threading.Thread(target=producer,)
c = threading.Thread(target=consumer,args=("Zhang Yu",))
c1 = threading.Thread(target=consumer,args=("Liu Bei",))

p.start()
c.start()
c1.start()
import threading, time

num = 0
lock = threading.Lock() # 把它赋给一个实例
def run(n):
    lock.acquire() # 开始加锁
    global num
    num += 1
    time.sleep(0.5)
    lock.release() # 释放锁

r_obj = []
for i in range(50):
    t = threading.Thread(target=run, args=('t-%s' % i,))
    t.start()
    r_obj.append(t)  # 每次循环后把实例t添加到数组

for r in r_obj:
    r.join()

print('-----所有线程已完成---------', num)







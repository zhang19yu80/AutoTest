import threading, time

def run(n,x):
    print('task %s %s'%(n,x))
    time.sleep(2)

r_obj = [] #建一个空数组
start_time = time.time()
#For循环启动N多线程
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,'beginning'))
    t.start()
    r_obj.append(t) #每次循环后把实例t添加到数组
print('当前线程数量：',threading.active_count())
print(r_obj)
for r in r_obj:
    r.join()

print('-----所有线程已完成---------',threading.current_thread())
print('共用时：',time.time()-start_time)

#单独启动1，2个多线程
# t56 = threading.Thread(target=run,args=('t1','...'))
# t78 = threading.Thread(target=run,args=('t2','...'))
#
# t56.start()
# t78.start()





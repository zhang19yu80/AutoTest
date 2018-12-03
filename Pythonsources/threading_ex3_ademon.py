import threading, time

def run(n,x):
    print('task %s %s'%(n,x))
    time.sleep(2)


start_time = time.time()
#For循环启动N多线程
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,'beginning'))
    t.setDaemon(True) #把当前线程设置成守护线程。  守护线程的意思是主线程执行完毕就可以退出脚本 不比等守护线程结束。
    t.start()


print('-----所有线程已完成---------')
print('共用时：',time.time()-start_time)

#单独启动1，2个多线程
# t56 = threading.Thread(target=run,args=('t1','...'))
# t78 = threading.Thread(target=run,args=('t2','...'))
#
# t56.start()
# t78.start()





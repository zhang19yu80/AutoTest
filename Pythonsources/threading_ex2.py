import threading

class Mythread(threading.Thread):
    def __init__(self,n,x):
        super(Mythread,self).__init__()
        self.n = n
        self.x = x

    def run(self): #这个函数名必须是 run，因为和继承的threading.Thread有关
        print('running task %s %s'%(self.n,self.x))

t100 = Mythread('t1','...')
t200 = Mythread('t2','!!!')

t100.start()
t200.start()
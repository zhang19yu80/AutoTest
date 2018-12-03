from multiprocessing import Process, Queue


def f(qq):
    qq.put(['dsff',None,123])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()
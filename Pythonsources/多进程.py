import multiprocessing, time, threading

def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(1)
    print('you are',name)
    t = threading.Thread(target=thread_run,)
    t.start()

if __name__ == '__main__':
    for i in range(10):
        j = multiprocessing.Process(target=run,args=('name %s'%i,))
        j.start()
    #    j.join()


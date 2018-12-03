import time, threading

events = threading.Event()

def lighter():
    count = 0
    events.set()

    while True:
        time.sleep(1)
        count += 1
        if count > 4 and count < 10: #改红灯
            events.clear()
            print("\033[41;1mred light is on...\033[0m")

        elif count > 10: #改绿灯
            events.set()
            count = 0

        else:
            print("\033[42;1mgreen light is on...\033[0m")


def car(name):
    while True:
        if events.is_set():
            print("[%s] running...."%name)
            time.sleep(4)

        else:
            print("now is red light, [%s]waiting..."%name)
            events.wait()

lighter1 = threading.Thread(target=lighter,)
lighter1.start()

car1 = threading.Thread(target=car,args=("新蒙迪欧",))
car1.start()
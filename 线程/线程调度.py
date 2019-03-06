import threading
import time

def go1():
    with cond:
        for i in range(1,10,2):
            time.sleep(1)
            print(threading.current_thread().name,str(i))
            cond.notify()
            cond.wait()


def go2():
    with cond:
        for i in range(0,10,2):
            time.sleep(1)
            print(threading.current_thread().name,str(i))
            cond.wait()
            cond.notify()




cond = threading.Condition()
threading.Thread(target=go2).start()
threading.Thread(target=go1).start()

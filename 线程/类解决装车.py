import threading
import time
num=0

mutex=threading.Lock()
class Mythread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):
            for i in range(1000000):
                num+=1
            mutex.release()
        print(num)

mythread=[]
for i in range(5):
    t=Mythread()
    t.start()
    mythread.append(t)
for mth in mythread:
    mth.join()
print("game over")
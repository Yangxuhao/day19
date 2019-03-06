import threading
import time
import win32api

class Mythread(threading.Thread):
    def run(self):
        win32api.MessageBox(0,"你的账号很危险","来自支付宝",3)

mythread=[]
for i in range(5):
    t=Mythread()
    t.start()
   # t.join()
    mythread.append(t)

for mythd in mythread:
    t.join()

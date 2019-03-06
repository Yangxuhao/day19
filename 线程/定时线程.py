import  time
import os
import threading

def go():
    os.system("notepad")

timethread=threading.Timer(5,go)
timethread .start()

i=0
while True:
    time.sleep(1)
    print("第",i,"秒")
    i+=1
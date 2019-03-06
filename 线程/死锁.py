import threading
import time

boymutex=threading.Lock()
girlmutex=threading.Lock()

class boy(threading.Thread):
    def run(self):
        if boymutex.acquire(1):
            print("boy say sorry")
            time.sleep(3)
            if girlmutex.acquire(1):
                print("girl say sorry")
                girlmutex.release()
            boymutex.release()
class girl(threading.Thread):
    def run(self):
        if girlmutex.acquire(1):
            print("girl say sorry")
            time.sleep(3)
            girlmutex.release()
            if boymutex.acquire(1):
                print("boy say sorry")
                boymutex.release()


boy1=boy()
boy1.start()
girl1=girl()
girl1.start()

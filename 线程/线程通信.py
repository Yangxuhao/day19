import threading
import time

def goevent():
    e=threading.Event()
    def go():
        e.wait()
        print("go")

    threading.Thread(target=go).start()
    return e

go=goevent()
time.sleep(5)
go.set()
import threading
import time
import threadpool
# def show(str):
#     print("hello",str)
#     time.sleep(2)
#
# namelist=["jkli","fgh","sssd"]
#
# start_time=time.time()
# for name in namelist:
#     show(name)
# end_time=time.time()
#
# print(end_time-start_time)

def show(str):
    print("hello",str)
    time.sleep(2)

namelist=["jkli","fgh","sssd"]

start_time=time.time()
pool=threadpool.ThreadPool(10)
request=threadpool.makeRequests(show,namelist)
for req in request:
    pool.putRequest(req)
end_time=time.time()

print(end_time-start_time)
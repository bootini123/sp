import threading,time
# threadObj=threading.Thread(target=print,args=['cat','dog','rabbit'],kwargs={'sep':'*'})
# threadObj.start()
print('Program start!')
def wake_up(i):
    time.sleep(i)
    i=str(i)
    print('wake up'+i+'!')
# def wake_up2():
#     time.sleep(2)
#     print('wake up2!')
thread_list=[]
for i in range(1,3):
    threadObj=threading.Thread(target=wake_up,args=[i])
    thread_list.append(threadObj)
    threadObj.start()
# threadObj1=threading.Thread(target=wake_up1)
# threadObj2=threading.Thread(target=wake_up2)
# threadObj1.start()
# threadObj2.start()
for threadObj in thread_list:
    threadObj.join()
print('Program end!')
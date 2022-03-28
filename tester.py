
import threading
from multiprocessing import cpu_count
from os import getpid
from os import system
from timeit import default_timer as dt



class MultiCalc():
    def __init__(self, num:int, num_threads:int=cpu_count()):
        self.num_threads = num_threads
        self.num=num
        # prepopulate thread_results
        self.thread_results = {thread:None for thread in range(num_threads)}
        # split the work evenly among threads
        self.thread_ranges = {thread:range(thread*(self.num//self.num_threads),(thread+1)*(self.num//self.num_threads)) for thread in range(num_threads)}
        self.threads:list[threading.Thread]=[]
        for thread_id in range(self.num_threads):
            self.threads+=[threading.Thread(target=self.calc, args=(thread_id,self.thread_ranges[thread_id]))]
    
    def run(self):
        # time thread creation
        #start = dt()
        for thread in self.threads:
            thread.start()
        #print(f"Total thread init time:\t{dt()-start}")

    def calc(self, thread_id:int, num_range:range):
        # debug
        #print(f"Thread {thread_id} started")
        self.thread_results[thread_id]=sum(x**2 for x in num_range)
        #print(f"Thread {thread_id} finished")
    
    def get_results(self):
        while True:
            if all(self.thread_results.values()):
                final=sum(self.thread_results.values())+self.num
                print(f"Thread result:\t{final} with {self.num_threads} threads")
                break

    def destroy(self):
        system(f"kill -9 {getpid()}")

num=10**7+10**7//2

a_multi_test=MultiCalc(num,56)
st=dt()
a_multi_test.run()
a_multi_test.get_results()
print(f"Thread time:\t{dt()-st}s")

# Now do the calculation in the main thread
st=dt()
final=sum(x**2 for x in range(num))+num
print(f"Main result:\t{final}")
print(f"Main time:\t{dt()-st}s") # average is about 2.94s

a_multi_test.destroy()

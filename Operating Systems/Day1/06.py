import time
from multiprocessing import Process
import os

def func():
    print("hi")
    print("process id: ", os.getpid())
    print("parent process id: ", os.getppid())

if __name__ == "__main__":
    print("06.py process id: ", os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=func)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=func)
    child3.start()
    time.sleep(0.5)

import time
from multiprocessing import Process
import os

def cider():
    print("cider process id : ", os.getpid())
    print("cider parent process id : ", os.getppid())

def coke():
    print("coke process id : ", os.getpid())
    print("coke parent process id : ", os.getppid())

def juice():
    print("juice process id : ", os.getpid())
    print("juice parent process id : ", os.getppid())

if __name__ == "__main__":
    print("07.py process id: ", os.getpid())
    child1 = Process(target=cider)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=coke)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=juice)
    child3.start()
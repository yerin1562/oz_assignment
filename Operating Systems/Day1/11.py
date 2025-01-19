from multiprocessing import Process
import os
import time

def coke():
    while True:
        try:
            print("process id: ", os.getpid())
            print("parent process id: ", os.getppid())
        except KeyboardInterrupt:
            break

def cider():
    while True:
        try:
            print("cider process id: ", os.getpid())
            print("cider parent process id: ", os.getppid())
        except KeyboardInterrupt:
            break

def juice():
    while True:
        try:
            print("juice process id: ", os.getpid())
            print("juice parent process id: ", os.getppid())
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print("11.py process id: ", os.getpid())
    child1 = Process(target=coke)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=cider)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=juice)
    child3.start()
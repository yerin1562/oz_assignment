from multiprocessing import Process
import os

def func():
    print("hi")
    print("process id: ", os.getpid())
    print("parent process id: ", os.getppid())

if __name__ == "__main__":
    print("05.py process id: ", os.getpid())
    child = Process(target=func).start()
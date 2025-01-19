import threading
import os

def func():
    print("hi")
    print("process id: ", os.getpid())
    print("thread id: ", threading.get_native_id())

if __name__ == "__main__":
    print('process id: ', os.getpid())
    thread1 = threading.Thread(target=func)
    thread1.start()


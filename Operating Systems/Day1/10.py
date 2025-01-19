import threading
import os
import time

def something(word):
    while True:
        print(word)
        time.sleep(3)

if __name__ == "__main__":
    print("process id: ", os.getpid())
    t = threading.Thread(target=something, args=("happy",))
    t.daemon = True
    t.start()
    print("main thread iterations start")
    while True:
        try:
            print('daily...')
            time.sleep(1)
        except KeyboardInterrupt:
            print('good bye')
            break
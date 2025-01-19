import psutil
import os

for process in psutil.process_iter():
    if process.pid == os.getpid():
        print(f"ps_name: {process.name()}, ps_id:", process.pid)
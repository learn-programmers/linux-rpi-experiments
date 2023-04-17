import threading
import time

lock = threading.Lock()

def resource_competing_thread():
    for _ in range(100000):
        with lock:
            time.sleep(0.0001)

threads = []

for _ in range(10):
    t = threading.Thread(target=resource_competing_thread)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

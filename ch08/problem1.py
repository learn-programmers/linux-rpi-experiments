import threading
import time

def busy_loop():
    count = 0
    while count < 10**8:
        count += 1

threads = []

for _ in range(10):
    t = threading.Thread(target=busy_loop)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

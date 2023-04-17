import threading
import time

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1.5)

# 스레드 생성
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 스레드 시작
thread1.start()
thread2.start()

# 스레드가 완료될 때까지 기다림
thread1.join()
thread2.join()

import os
import time

def main():
    num_iterations = 3000
    file_name = "test_file.txt"

    # 파일 생성
    with open(file_name, "w") as f:
        f.write("This is a test file for I/O overhead example.\n" * 100000)

    # 캐시 삭제
    os.system("sync; echo 3 > /proc/sys/vm/drop_caches")

    # 파일 읽기 반복
    start_time = time.time()
    for _ in range(num_iterations):
        with open(file_name, "r") as f:
            f.read()
    end_time = time.time()

    print(f"Total time for {num_iterations} iterations: {end_time - start_time:.2f} seconds")

    # 파일 삭제
    os.remove(file_name)

if __name__ == "__main__":
    main()

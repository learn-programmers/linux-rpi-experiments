import time
import mmap
import aiofiles
import asyncio
import subprocess

# 파일 버퍼링을 사용한 함수
def read_file_buffered(file_path):
    with open(file_path, "r", buffering=64*1024) as f:
        data = f.read()
    return data

# 메모리 매핑을 사용한 함수
def read_file_mmap(file_path):
    with open(file_path, "r") as f:
        mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        data = mmapped_file.read()
        mmapped_file.close()
    return data

# 비동기 I/O를 사용한 함수
async def read_file_async(file_path):
    async with aiofiles.open(file_path, "r") as f:
        return await f.read()

# 성능 측정 함수
async def measure_time_async(func, file_path):
    start_time = time.time()
    data = await func(file_path)
    end_time = time.time()
    duration = end_time - start_time
    return data, duration

def measure_time(func, file_path):
    start_time = time.time()
    data = func(file_path)
    end_time = time.time()
    duration = end_time - start_time
    return data, duration

# main 함수
async def main():
    file_path = "large_file.txt"

    # 파일 버퍼링을 사용한 경우
    data, duration = measure_time(read_file_buffered, file_path)
    print(f"Using file buffering: {duration:.6f} seconds")

    # 메모리 매핑을 사용한 경우
    data, duration = measure_time(read_file_mmap, file_path)
    print(f"Using memory mapping: {duration:.6f} seconds")

    # 비동기 I/O를 사용한 경우
    data, duration = await measure_time_async(read_file_async, file_path)
    print(f"Using async I/O: {duration:.6f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


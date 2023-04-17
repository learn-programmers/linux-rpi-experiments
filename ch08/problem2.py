import os
import mmap

file_size = 10**9  # 1 GB
file_name = "large_file.dat"

with open(file_name, "wb") as f:
    f.seek(file_size - 1)
    f.write(b"\0")

with open(file_name, "r+b") as f:
    mmapped_data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

    for i in range(0, file_size, 4096):
        mmapped_data[i] = 0

os.remove(file_name)

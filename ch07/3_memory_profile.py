from memory_profiler import profile

@profile
def memory_intensive_function():
    large_list = [i for i in range(10**6)]
    return sum(large_list)

if __name__ == "__main__":
    memory_intensive_function()

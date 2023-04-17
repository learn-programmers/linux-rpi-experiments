import timeit

code_to_test = """
def find_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = find_even_numbers(numbers)
"""

execution_time = timeit.timeit(code_to_test, number=1000)
print(f"Execution time: {execution_time:.4f} seconds")

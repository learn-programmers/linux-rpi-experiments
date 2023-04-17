import time
import math
import random

start_time = time.time()

points = [(random.random(), random.random()) for _ in range(10**4)]

distances = [math.dist(points[i], points[j])
             for i in range(len(points))
             for j in range(i + 1, len(points))]

end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")

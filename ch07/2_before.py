import time
import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

start_time = time.time()

points = [(random.random(), random.random()) for _ in range(10**4)]

distances = [euclidean_distance(points[i], points[j])
             for i in range(len(points))
             for j in range(i + 1, len(points))]

end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")

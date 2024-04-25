import math


points = []
n = int(input("how many point bundles to enter?: "))

for i in range(n):
    x = float(input(f"Points {i+1} Enter the x coordinate: "))
    y = float(input(f"Points {i+1} Enter the y coordinate: "))
    points.append((x, y))

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = round(min(distances),5)
print("Minimum Distance is:", min_distance)
import data

# Write your functions for each part in the space below.

# Part 1
def first_element(nested_list: list[list[int]]) -> list[int]:
    # Step 1: Filter out empty lists
    non_empty_lists = [lst for lst in nested_list if lst]

    # Step 2: Extract the first element from each remaining list
    first_elements = [lst[0] for lst in non_empty_lists]

    return first_elements
# Part 2
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def x_coordinates(points: list[Point]) -> list[int]:
    # Extracting the x-coordinates from each point using a list comprehension
    return [point.x for point in points]

# Part 3
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def are_in_positive_quadrant(points: list[Point]) -> list[Point]:
    # Filter the points that are in the first quadrant using a list
    return [point for point in points if point.x > 0 and point.y > 0]

# Part 4
import math

# Definition of the Point class
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def distance(point1: Point, point2: Point) -> float:
    # Calculate the Euclidean distance between the two points
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

# Part 5
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def manhattan_distance(point1: Point, point2: Point) -> float:
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)
  
# Part 6
import math

# Definition of the Point class
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def distance(point1: Point, point2: Point) -> float:
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def distance_all(points: list[Point]) -> list[float]:
    origin = Point(0, 0)
    return [distance(origin, point) for point in points]


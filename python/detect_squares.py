"""You are given a stream of points on the X-Y plane. Design an algorithm that:

    Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
    Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

    DetectSquares() Initializes the object with an empty data structure.
    void add(int[] point) Adds a new point point = [x, y] to the data structure.
    int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

"""
from typing import List
from collections import defaultdict

def point_hash(point:List[int]):
    return point[0] * max_L + point[1]
max_L = 10001
class DetectSquares:
    def __init__(self):
        self.ox_quick_hashmap = defaultdict(list)
        self.all_points = defaultdict(int)
        # points_added =

    def add(self, point: List[int]) -> None:
        l = self.ox_quick_hashmap[point[0]]
        l.append(point[1])
        self.all_points[point_hash(point)] +=1


    def count(self, point: List[int]) -> int:
        nsq = 0
        # print("debug in count")
        for second_point_oy_coord in self.ox_quick_hashmap[point[0]]:
            # print("second point coords: ", (point[0],second_point_oy_coord))
            length_of_square = point[1]- second_point_oy_coord
            if length_of_square != 0:
                for length in (length_of_square,-length_of_square):
                    potential_third_point_hash = point_hash([point[0]+length, point[1]])
                    if potential_third_point_hash in self.all_points:
                        potential_fourth_point_hash = point_hash([point[0]+length, second_point_oy_coord])
                        if potential_fourth_point_hash in self.all_points:
                            nsq += self.all_points[potential_fourth_point_hash] * self.all_points[potential_third_point_hash]
        return nsq

if __name__ == "__main__":
    points = [[3,10],[11,2],[3,2],[11,10],[14,8],[11,2],[11,10]]

    obj = DetectSquares()
    obj.add(points[0])
    obj.add(points[1])
    obj.add(points[2])
    print(obj.count(points[3]))
    print(obj.count(points[4]))
    obj.add(points[5])
    print(obj.count(points[6]))




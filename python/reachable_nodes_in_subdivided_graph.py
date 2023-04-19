"""You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.



Example 1:

Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.

Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23

Example 3:

Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
Output: 1
Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.



Constraints:

    0 <= edges.length <= min(n * (n - 1) / 2, 104)
    edges[i].length == 3
    0 <= ui < vi < n
    There are no multiple edges in the graph.
    0 <= cnti <= 104
    0 <= maxMoves <= 109
    1 <= n <= 3000

"""
from typing import List
import heapq
from collections import defaultdict
import math


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        if maxMoves == 0:
            return 0
        if n == 1:
            return 1

        neighbours = defaultdict(list)
        visited = defaultdict(lambda: False)
        distance = defaultdict(lambda: math.inf)
        distance[0] = 0

        reached = 1
        for edge in edges:
            neighbours[edge[0]].append((edge[1], edge[2])) # tuple containst pos0: neighbour, and pos1: distance
            neighbours[edge[1]].append((edge[0], edge[2]))

        heap = [(0, 0, 0)] # tuple contains pos0: distance, pos1: node "name", pos2: "parent" node "name"
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            print("#######")
            print(f"curr node = {curr[1]}, at a distance from source of {curr[0]}")
            if visited[curr[1]]:
                # print("node already visited")
                continue
            # if distance[curr[1]]>maxMoves:
            #     print("in case where we can't reach this node with the remaining juice")
            #     reached += maxMoves - distance[curr[2]]
            #     continue
            else:
                # print("we here")
                visited[curr[1]] = True
                distance[curr[1]] = curr[0]
                for nb in neighbours[curr[1]]:
                    print(f"for nb: {nb[0]}, at distance {nb[1]}")
                    new_dist = curr[0] + nb[1] + 1

                    # distance[nb[0]] = min(new_dist, distance[nb[0]])
                    heapq.heappush(heap, (new_dist,nb[0],curr[1]))
                    print("juice left: ", maxMoves - curr[0])
                    if visited[nb[0]] == False:
                        print("this nb not visited")
                        update = min(maxMoves - curr[0], nb[1] + 1)
                    else:
                        print("this nb visited")
                        reached_from_other_side = min(maxMoves - distance[nb[0]],nb[1])
                        update = min(maxMoves - curr[0], nb[1]-reached_from_other_side)
                    print("update = ", update)
                    reached +=update



        return reached

if __name__ == "__main__":
    edges = [[2, 4, 2], [3, 4, 5], [2, 3, 1], [0, 2, 1], [0, 3, 5]]
    maxMoves = 14
    n = 5

    print(Solution().reachableNodes(edges,maxMoves,n))
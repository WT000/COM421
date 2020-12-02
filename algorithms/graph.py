import heapq
from heapq import heappush, heappop
import sys

class Node:
  def __init__(self, name):
    self.name = name
    self.data = (sys.maxsize, self)
    self.parent = None
    self.used = False
    self.edges = []

  def add_edge(self, start, end, dist):
    edge = Edge(start, end, dist)
    self.edges.append(edge)

  def __str__(self):
    return self.name.__str__()

  def __repr__(self):
    return "node=(name={}, data={}, parent={}, used={}, edges={})".format(self.name, self.data[0], self.parent, self.used, self.edges)

class Edge:
  def __init__(self, start, end, dist):
    self.start = start
    self.end = end
    self.dist = dist

  def __repr__(self):
    return "(start={} end={} dist={})".format(self.start, self.end, self.dist)

# The graph class only really holds the algorithms for the node and edge objects
class Graph:
  def add_edge(self, start, end, dist):
    start.add_edge(start, end, dist)
    end.add_edge(end, start, dist)

  def dijkstra(self, start_node, end_node):
    # create the priority queue and current node variable, make the distance of cur node 0

    # push onto the priority queue

    # while current node does not equal end node or the len of queue is not 0
    # pop the front of the queue, this will be the new cur_node
    
    # for edge in current nodes edges, if:
    # distance data inside the node + the edge distance < edge end data:
    # update that nodes distance 
    # add to the priority queue
    # once all done, remove the front of the queue and set used to true
    
if (__name__ == "__main__"):
  graph = Graph()
  n1 = Node("London")
  n2 = Node("France")
  n3 = Node("Moscow")
  graph.add_edge(n1, n2, 100)
  graph.add_edge(n1, n3, 400)
  graph.dijkstra(n1, n3)

  print(repr(n1))
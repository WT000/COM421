from heapq import heappush, heappop
import collections

class Node:
  def __init__(self, name):
    self.name = name
    self.dist = 999999999999999
    self.parent = None
    self.used = False
    self.edges = []

  def add_edge(self, start, end, dist):
    edge = Edge(start, end, dist)
    self.edges.append(edge)

  def __str__(self):
    return self.name.__str__()

  def __repr__(self):
    return "node=(name={}, dist={}, parent={}, used={}, edges={})".format(self.name, self.dist, self.parent, self.used, self.edges)

  def __lt__(self, other):
    return self.name < other.name

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
    # Firstly, we create the priority queue and set the current node to None
    priority_queue = []
    current_node = None

    # Then, we set the start nodes distance to 0, as it's the node to start exploring from
    start_node.dist = 0

    # With the distance set, we now push the starting node onto the priority queue
    heappush(priority_queue, (start_node.dist, start_node))

    # Whilst the length of the queue is greater than 0 and we haven't reached the end node:
    while (len(priority_queue) != 0):
      # We pop the node that was at the front of the queue (whichever has the next lowest distance) and store it in current_node
      current_node = heappop(priority_queue)
      # index 0 represents the node distance, used for the ordering in the queue
      # index 1 represents the node itself
      
      # Then, we look at each of the edges, if the node at the end of an edge has already been explored we skip the edge
      for edge in current_node[1].edges:
        if (edge.end.used == True):
          continue
        
        # Else, we firstly calculate the distance from the current node to the node at the end of the edge
        calculated_dist = current_node[0] + edge.dist

        # Then, we set the current shortest path to the distance to the end node
        current_shortest_dist = edge.end.dist

        # If the distance we calculated is lower than the current shortest path, it means we've found an even smaller path.
        # Set the new shortest dist to the calculated distance and set the parent to the current node
        if (calculated_dist < current_shortest_dist):
          current_shortest_dist = calculated_dist
          edge.end.parent = current_node
        
        # Whether we found a shorter distance or not, we set the edge node's distance to whatever the shortest distance is and
        # finally push this onto the queue
        edge.end.dist = current_shortest_dist
        heappush(priority_queue, (current_shortest_dist, edge.end))
      
      # Now that the current nodes edges have been fully explored, we set this to true so that we don't explore the node again
      current_node[1].used = True
    
    # Once the while loop is complete, it means we've found the route, so we next
    # create a route queue which will be used to display the route
    route = collections.deque([])
    
    # current_node is currently the end node, whilst this is not equal to None:
    while current_node is not None:
      # Append current_node to the queue
      route.appendleft(current_node[1].name)
      # Set current_node to the parent of the node, this repeats until we reach the starting node
      current_node = current_node[1].parent
    
    # Now that the route has been created, we return it
    return route

if (__name__ == "__main__"):
  graph = Graph()
  
  a = Node("A")
  b = Node("B")
  c = Node("C")
  d = Node("D")

  graph.add_edge(a, b, 10)
  graph.add_edge(a, c, 3)
  graph.add_edge(b, c, 1)
  graph.add_edge(b, d, 4)
  graph.add_edge(c, d, 8)

  print(graph.dijkstra(a, d))

  #
  #
  #   10 B  4
  # A     1   D
  #   3  C  8
  #
  # The correct order is A > C > B > D
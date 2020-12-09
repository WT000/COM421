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
  def __init__(self):
    self.h_distances = {
      "Birmingham":1188,
      "Brussels":823,
      "Paris":686,
      "Lyon":299,
      "Bordeaux":637,
      "Amsterdam":980,
      "Cologne":805
    }
  
  def add_edge(self, start, end, dist):
    start.add_edge(start, end, dist)
    end.add_edge(end, start, dist)

  def dijkstra(self, start_node, end_node):
    # Firstly, we create the priority queue and set the current node to None
    priority_queue = []
    current_node = start_node

    # Then, we set the start nodes distance to 0, as it's the node to start exploring from
    current_node.dist = 0

    # With the distance set, we now push the starting node onto the priority queue
    heappush(priority_queue, (current_node.dist, current_node))

    # Whilst the length of the queue is greater than 0 and we haven't reached the end node:
    while (len(priority_queue) != 0 or current_node[1] != end_node):
      # We pop the node that was at the front of the queue (whichever has the next lowest distance) and store it in current_node
      current_node = heappop(priority_queue)
      
      # index 0 represents the node distance, used for the ordering in the queue
      # index 1 represents the node itself
      
      # Then, we look at each of the edges, if the node hasn't been explored then we'll explore it
      for edge in current_node[1].edges:
        if (edge.end.used == False):
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
          heappush(priority_queue, (edge.end.dist, edge.end))
      
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

  def a_star(self, start_node, end_node):
    priority_queue = []
    current_node = start_node

    current_node.dist = 0

    heappush(priority_queue, (current_node.dist, current_node))

    while (len(priority_queue) != 0 or current_node[1] != end_node):
      current_node = heappop(priority_queue)
      # index 0 represents the node distance, used for the ordering in the queue
      # index 1 represents the node itself
      
      for edge in current_node[1].edges:
        if (edge.end.used == False):
          # The g score is the same calculation as dijkstra's, that
          # being the current nodes distance from the starting node
          # plus the edge distance of the edge
          g_score = current_node[0] + edge.dist

          # Whilst the h score is new, this is the straight line
          # distance from the node to get to the destination
          # in this case, always being Nice
          h_score = self.h_distances.get(current_node[1].name)

          # If the h score is none (meaning we're at the start node),
          # turn None into 0
          if (h_score == None):
            h_score = 0

          # Then, we add the g score and h score to create the f score
          f_score = g_score + h_score

          # The calculation is then the same as the previous algorithm,
          # we get the current shortest distance to the end node
          # and compare this to the newly calculated distance, if it's
          # lower then we'll update the shortest distance and parent
          # of the end node
          current_shortest_dist = edge.end.dist

          if (f_score < current_shortest_dist):
            current_shortest_dist = f_score
            edge.end.parent = current_node
          
          # Then, whether we replaced the values or not, we update
          # the end distance to be the current shortest and push this
          # to the queue, with the node explored we make used True
          edge.end.dist = current_shortest_dist
          heappush(priority_queue, (edge.end.dist, edge.end))
      
        current_node[1].used = True
    
    route = collections.deque([])

    while current_node is not None:
      route.appendleft(current_node[1].name)
      current_node = current_node[1].parent

    return route

if (__name__ == "__main__"):
  choice = int(input("Enter 1 for dijkstra, 2 for A*, 3 for dijkstra with the same nodes as A*\n"))

  if (choice == 1):
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
  
  elif (choice == 2 or choice == 3):
    graph = Graph()

    birmingham = Node("Birmingham")
    london = Node("London")
    amsterdam = Node("Amsterdam")
    brussels = Node("Brussels")
    cologne = Node("Colonge")
    paris = Node("Paris")
    lyon = Node("Lyon")
    bordeaux = Node("Bordeuax")
    nice = Node("Nice")

    graph.add_edge(birmingham, london, 191)
    graph.add_edge(london, brussels, 370)
    graph.add_edge(london, paris, 461)
    graph.add_edge(brussels, paris, 306)
    graph.add_edge(brussels, cologne, 211)
    graph.add_edge(brussels, amsterdam, 211)
    graph.add_edge(paris, lyon, 465)
    graph.add_edge(paris, bordeaux, 584)
    graph.add_edge(lyon, nice, 472)
    graph.add_edge(bordeaux, nice, 803)

    if (choice == 2):
      print(graph.a_star(london, nice))
    else:
      print(graph.dijkstra(london, nice))

  else:
    print("Please enter 1 or 2.")
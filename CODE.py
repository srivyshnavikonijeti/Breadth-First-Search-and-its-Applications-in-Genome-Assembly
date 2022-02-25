
graph = {
  'TAA' : ['AAT', 'AAG'],
  'AAT' : ['ATG','ATT'],
  'ATG' : ['TGT'],
  'TGT' : ['GTT'],
  'GTT' : [],
  'ATT' : [],
  'AAG' : []
}

visited = [] 
queue = []     

#Function 2 find the path visiting all nodes
def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        

#Function to find the shortest path between 2 nodes        
def shortestpath(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print("The shortest path from TAA to GTT is :")
print(shortestpath(graph, 'TAA', 'GTT'))        
print()
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'TAA')  

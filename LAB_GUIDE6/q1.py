def DFS(graph,vertex,path):
    path += vertex
    for x in graph[vertex]:
        if x not in path:
            path = DFS(graph,x,path)

    return path

def BFS(graph,vertex):
    
    queue = []
    visited = []
    visited.append(vertex)
    queue.append(vertex)
    while len(queue):
        curvertex = queue.pop(0)
        for neighbor in graph[curvertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited 



vertex_count = int(input("Enter the number of vertexes:"))

vertex_list =  []

inp = input("Enter the vertex list:")

for i in inp:
    vertex_list.append(i)
print(vertex_list)

print("Enter the adjacency matrix:")
matrix = []



for i in range(0,vertex_count):
    inp = input()
    temp = []
    print(inp.split())
    for j in inp.split():
        temp.append(int(j))

    matrix.append(temp)

graph = {}
for i in range(0, vertex_count):
    lst = []
    for j in range(0,len(matrix[i])):
        if matrix[i][j] == 1 :
            lst.append(vertex_list[j])

    graph[vertex_list[i]] = lst

print(matrix)
  
print(graph) 
path = []


print("DFS Traversal",DFS(graph,vertex_list[0],path)) 
print("BFS Traversal", BFS(graph,vertex_list[0]))

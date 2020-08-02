'''
Link Reference:
https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
'''

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS dung queue

visited_bfs = []
queue_bfs = []

def bfs(visited_bfs, graph, node):
    visited_bfs.append(node)
    queue_bfs.append(node)

    while queue_bfs:
        s = queue_bfs.pop(0)
        print(s, end=' ')

        for neighbour in graph[s]:
            if neighbour not in visited_bfs:
                visited_bfs.append(neighbour)
                queue_bfs.append(neighbour)
    
print('\nThuat toan BFS')
bfs(visited_bfs, graph, 'A')


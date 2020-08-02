'''
Link Reference:
https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
'''

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# DFS dung stack
visited_dfs = set()

def dfs(visited_dfs, graph, node):
    if node not in visited_dfs:
        print(node, end = ' ')
        visited_dfs.add(node)
        for neighbour in graph[node]:
            dfs(visited_dfs, graph, neighbour)

print ('Thuat toan DFS')
dfs(visited_dfs, graph, 'A')

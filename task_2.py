import networkx as nx

# Створення графа
social_network = nx.Graph()

# Додавання вузлів (користувачів)
social_network.add_nodes_from([
    ("Alice", {"age": 30, "gender": "female"}),
    ("Bob", {"age": 25, "gender": "male"}),
    ("Charlie", {"age": 40, "gender": "male"}),
    ("David", {"age": 35, "gender": "male"}),
    ("Eva", {"age": 45, "gender": "female"}),
    ("Frank", {"age": 20, "gender": "male"}),
    ("Grace", {"age": 50, "gender": "female"}),
])

# Додавання ребер (зв'язків між користувачами)
social_network.add_edges_from([
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "Charlie"),
    ("Bob", "David"),
    ("Charlie", "David"),
    ("David", "Eva"),
    ("David", "Frank"),
    ("Eva", "Frank"),
    ("Eva", "Grace"),
])

# Функція для знаходження шляхів з використанням DFS
def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    for node in graph.neighbors(start):
        if node not in path:
            new_paths = dfs_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Функція для знаходження шляхів з використанням BFS
def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph.neighbors(vertex):
            if next_node not in path:
                if next_node == end:
                    paths.append(path + [next_node])
                else:
                    queue.append((next_node, path + [next_node]))
    return paths

# Функція для візуалізації шляхів
def visualize_paths(paths):
    for i, path in enumerate(paths, start=1):
        print(f"Шлях {i}: {' -> ' + str(path)}")


# Пошук шляхів з використанням DFS
dfs_result = dfs_paths(social_network, 'Alice', 'Frank')
print("DFS:")
visualize_paths(dfs_result)

# Пошук шляхів з використанням BFS
bfs_result = bfs_paths(social_network, 'Alice', 'Frank')
print("\nBFS:")
visualize_paths(bfs_result)

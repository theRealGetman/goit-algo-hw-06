import networkx as nx
import matplotlib.pyplot as plt

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

# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(social_network, with_labels=True, node_color='skyblue',
        node_size=2000, font_size=12, font_weight='bold')
plt.title("Соціальна мережа")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин (користувачів):", social_network.number_of_nodes())
print("Кількість ребер (зв'язків між користувачами):",
      social_network.number_of_edges())
print("Ступінь вершин:")
for node in social_network.nodes():
    print(f"Вершина {node}: {social_network.degree[node]}")

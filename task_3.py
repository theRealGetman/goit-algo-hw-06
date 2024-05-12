import heapq


def dijkstra_shortest_paths(graph, start):
    # Ініціалізація відстаней до кожної вершини як нескінченності, крім стартової вершини
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Відстань до стартової вершини - 0

    # Ініціалізація пріоритетної черги з вершинами та їх відстанями
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо відстань до поточної вершини більша за відстань, що вже збережена,
        # ігноруємо цю вершину
        if current_distance > distances[current_node]:
            continue

        # Переглядаємо всі сусідні вершини поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до вершини, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def dijkstra_shortest_path(graph, start, end):
    # Ініціалізація відстаней до кожної вершини як нескінченності, крім стартової вершини
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Відстань до стартової вершини - 0

    # Ініціалізація пріоритетної черги з вершинами та їх відстанями
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо поточна вершина - цільова, завершуємо алгоритм
        if current_node == end:
            break

        # Якщо відстань до поточної вершини більша за відстань, що вже збережена,
        # ігноруємо цю вершину
        if current_distance > distances[current_node]:
            continue

        # Переглядаємо всі сусідні вершини поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до вершини, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]


# Граф з вагами на ребрах
graph = {
    "Alice": {"Bob": 2, "Charlie": 3},
    "Bob": {"Alice": 2, "Charlie": 1, "David": 7},
    "Charlie": {"Alice": 3, "Bob": 1, "David": 5},
    "David": {"Bob": 7, "Charlie": 5, "Eva": 2, "Frank": 4},
    "Eva": {"David": 2, "Frank": 3, "Grace": 6},
    # Додайте float('inf') для відсутніх зв'язків
    "Frank": {"David": 4, "Eva": 3, "Grace": float('inf')},
    "Grace": {"Eva": 6, "Frank": float('inf')}
}

# Запуск алгоритму Дейкстри зі стартовою вершиною "Alice"
shortest_paths = dijkstra_shortest_paths(graph, "Alice")

# Вивід найкоротших відстаней до кожної вершини від стартової вершини "Alice"
for node, distance in shortest_paths.items():
    print(f"Найкоротший шлях до вершини {node}: {distance}")

# Початкова та кінцева вершини
start_node = "Alice"
end_node = "Frank"

# Запуск алгоритму Дейкстри для знаходження найкоротшого шляху від початкової до кінцевої вершини
shortest_path = dijkstra_shortest_path(graph, start_node, end_node)

# Вивід найкоротшого шляху
print(
    f"Найкоротший шлях від вершини {start_node} до вершини {end_node}: {shortest_path}")

# Знаходимо найкоротші шляхи між усіма парами вершин
all_shortest_paths = {start: dijkstra_shortest_paths(
    graph, start) for start in graph}

# Вивід найкоротших шляхів
for start_node in all_shortest_paths:
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for end_node, shortest_path in all_shortest_paths[start_node].items():
        print(f"  {start_node} -> {end_node}: {shortest_path}")

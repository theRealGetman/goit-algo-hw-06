### Порівняння результатів виконання DFS та BFS для графа

#### DFS:
1. Шлях 1: Alice -> Bob -> Charlie -> David -> Eva -> Frank
2. Шлях 2: Alice -> Bob -> Charlie -> David -> Frank
3. Шлях 3: Alice -> Bob -> David -> Eva -> Frank
4. Шлях 4: Alice -> Bob -> David -> Frank
5. Шлях 5: Alice -> Charlie -> Bob -> David -> Eva -> Frank
6. Шлях 6: Alice -> Charlie -> Bob -> David -> Frank
7. Шлях 7: Alice -> Charlie -> David -> Eva -> Frank
8. Шлях 8: Alice -> Charlie -> David -> Frank

#### BFS:
1. Шлях 1: Alice -> Bob -> David -> Frank
2. Шлях 2: Alice -> Charlie -> David -> Frank
3. Шлях 3: Alice -> Bob -> Charlie -> David -> Frank
4. Шлях 4: Alice -> Bob -> David -> Eva -> Frank
5. Шлях 5: Alice -> Charlie -> Bob -> David -> Frank
6. Шлях 6: Alice -> Charlie -> David -> Eva -> Frank
7. Шлях 7: Alice -> Bob -> Charlie -> David -> Eva -> Frank
8. Шлях 8: Alice -> Charlie -> Bob -> David -> Eva -> Frank

### Висновки:
- DFS знаходить будь-який доступний шлях між двома вершинами, перш ніж вивести результат. Тому результати DFS мають різну довжину.
- BFS знаходить найкоротший шлях між двома вершинами. Тому усі результати BFS мають однакову довжину, а саме, найкоротшу.
- Обидва алгоритми використовують ті самі ребра графа, але DFS може "заглиблюватись" глибше в глибоко розгалужені гілки, що призводить до різних шляхів, в той час як BFS шукає шляхи на всіх рівнях графа і знаходить найкоротший шлях.

# Считывание входных данных

matrix = []

N = int(input())
D, A = tuple(input().split())
D, A = int(D), int(A)
for count in range(N):
    matrix.append(input())

# Заполняем списки смежности - s с помощью matrix
s = []
for i in range(N):
    s.append([])

edges = set()

i = 0
while i < N - 1:
    j = i
    split_line = matrix[i]
    while j < N:
        if int(split_line[j]) == 1:
            s[i].append(j)
            s[j].append(i)
            edges.add((i, j))
            edges.add((j, i))
        j += 1
    i += 1

# 1. Поиск компонент связности через dfs или bfs

vertices = set(i for i in range(N))
visited = set()
queue = []
components = []

while visited != vertices:
    old_visited = set(visited)
    v = vertices.difference(visited).pop()
    queue.append(v)
    visited.add(v)
    while queue:
        u = queue.pop()
        for w in s[u]:
            if w not in visited:
                queue.append(w)
                visited.add(w)
    components.append(list(visited.difference(old_visited)))
# Добавление связующих рёбер
added = set()
for i in range(1, len(components)):
    s[components[0][0]].append(components[i][0])
    added.add((components[0][0], components[i][0]))
    s[components[i][0]].append(components[0][0])
    added.add((components[i][0], components[0][0]))

# 2. Построение минимального дерева через алгоритм Прима или Краскала
# Удаление лишних рёбер
edges = set()
visited = set()
components = []
vertices = [i for i in range(N)]
deleted = set()

for i in range(N):
    for j in s[i]:
        if vertices[i] != vertices[j] and (i, j) not in edges:
            edges.add((i, j))
            edges.add((j, i))
            bad_number = vertices[j]
            for k in range(N):
                if vertices[k] == bad_number:
                    vertices[k] = vertices[i]
        elif (i, j) not in edges:
            deleted.add((i, j))
            deleted.add((j, i))

print(len(added) // 2 * A + len(deleted) // 2 * D)

for i in range(N):
    line = ''
    for j in range(N):
        if (i, j) in added:
            line += 'a'
        elif (i, j) in deleted:
            line += 'd'
        else:
            line += '0'
    print(line)

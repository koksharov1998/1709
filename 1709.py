# Считывание входных данных

matrix = []

for line in open('in.txt'):
    matrix.append(line)

N = int(matrix.pop(0))
D, A = tuple(matrix.pop(0).split())
D, A = int(D), int(A)

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

# Добавление связующих рёбер
vertices = set(i for i in range(N))
connected = set()
visited = set()
added = set()

while vertices.difference(connected):
    v = vertices.difference(visited).pop()
    if v not in connected and connected:
        old_vertex = connected.pop()
        connected.add(old_vertex)
        added.add((old_vertex, v))
        added.add((v, old_vertex))
        s[v].append(old_vertex)
        s[old_vertex].append(v)
    visited.add(v)
    connected.add(v)
    connected = connected.union(s[v])

# Удаление лишних рёбер
connected = set()
connected_tuples = set()

for v in range(N):
    connected.add(v)
    for u in s[v]:
        if u not in connected:
            connected_tuples.add((u, v))
            connected_tuples.add((v, u))
            connected.add(u)

deleted = edges.difference(connected_tuples)

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

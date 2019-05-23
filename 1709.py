# Считывание входных данных

matrix = []

for line in open('in.txt'):
    matrix.append(line)

N = int(matrix.pop(0))
A, D = tuple(matrix.pop(0).split())
D, A = int(D), int(A)

# Заполняем списки смежности - s с помощью matrix
s = []
for i in range(N):
    s.append([])

i = 0
while i < N - 1:
    j = i
    split_line = matrix[i]
    while j < N:
        if int(split_line[j]) == 1:
            s[i].append(j)
            s[j].append(i)
        j += 1
    i += 1

# Добавление связующих вершин и удаление лишних
vertices = set(i for i in range(N))
connected = set()
visited = set()
added = set()
deleted = set()

while vertices.difference(connected):
    print(vertices.difference(connected))
    v = vertices.difference(connected).pop()
    try:
        old_vertex = connected.pop()
        connected.add(old_vertex)
        added.add((old_vertex, v))
    except KeyError:
        pass
    print(v)
    connected.add(v)
    connected = connected.union(s[v])
print(added)
print(deleted)

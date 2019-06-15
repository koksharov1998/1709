from copy import deepcopy

N = int(input())
(D, A) = tuple(input().split())
D, A = int(D), int(A)
matrix = [input() for _ in range(N)]
s = [[] for _ in range(N)]
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
added = set()
for i in range(1, len(components)):
    s[components[0][0]].append(components[i][0])
    added.add((components[0][0], components[i][0]))
    s[components[i][0]].append(components[0][0])
    added.add((components[i][0], components[0][0]))
edges = set()
colour_of_vertices = [i for i in range(N)]
colours_vertices = {i: {i} for i in range(N)}
deleted = set()
for i in range(N):
    for j in s[i]:
        if colour_of_vertices[i] != colour_of_vertices[j] and (i, j) not in edges:
            edges.add((i, j))
            edges.add((j, i))
            bad_number = colour_of_vertices[j]
            m = deepcopy(colours_vertices[bad_number])
            for vertex in m:
                colour_of_vertices[vertex] = colour_of_vertices[i]
                colours_vertices[i].add(vertex)
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

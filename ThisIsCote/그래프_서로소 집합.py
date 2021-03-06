"""
    작성일 : 20/10/29
"""

""" 
    ! 서로소 집합
"""

""" def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b )

for i in range(1, v + 1):
    print(find_parent(parent, i), end = ' ')

print()

for i in range(1, v + 1):
    print(parent[i], end = ' ')
"""

""" 
    ! 개선된 서로소 집합
    - 루트 노드 찾는 과정 O(V) 해결
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())

parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

for i in range(1, v + 1):
    print(parent[i], end=' ')
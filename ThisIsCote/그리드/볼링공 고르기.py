""" 
    작성일 : 20/11/04
"""

from itertools import combinations

m, n = map(int, input().split())
data = list(map(int, input().split()))
""" data = list(combinations(data, 2))
result = 0
for i in data:
    if i[0] != i[1]:
        result += 1

print(result) """

result = 0

for i in range(0, m - 1):
    for j in range(i + 1, m):
        if data[i] != data[j]:
            result += 1

print(result)
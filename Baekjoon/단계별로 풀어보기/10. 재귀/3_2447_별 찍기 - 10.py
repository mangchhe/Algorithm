# 구글
# 프랙탈
# 최소 단위로 쪼갤 수 있기에 분할 정복 알고리즘을 이용
# 분할 정복 알고리즘(분할, 정복, 합치기)
# 분할만 잘하면 정복은 하기가 쉽다.

def stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)

    return (list(matrix))


star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)
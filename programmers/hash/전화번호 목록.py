"""
    작성일 : 20/08/31 - 진행중
"""

def solution(phone_book):

    answer = True
    tmp = phone_book[0]
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(tmp, 0, len(tmp)+1):
            answer = False
            break
    return answer

print(solution(['123','456','789']))
""" 
    작성일 : 20/09/07 - 진행중
    수정일 : 
    20/09/08 - 진행중
    20/09/09 - 완료
"""

import heapq

""" def solution(jobs):

    jobs = list(map(lambda x: [x[1], x[0]], jobs))

    start = 1
    end = 0
    current = 0 + jobs[0][0]
    result = 0 + jobs[0][0]
    
    while True:
        for i in range(start, len(jobs)):
            if current < jobs[i][1]:
                end = i - 1
            elif current == jobs[i][1]:
                end = i
            elif i == len(jobs) - 1:
                end = i
        tmp = jobs[start:end+1]
        start = end + 1
        heapq.heapify(tmp)

        for i in range(len(tmp)):
            tmp2 = heapq.heappop(tmp)
            result += current - tmp2[1] + tmp2[0]
            current += tmp2[0]

        if end == len(jobs) - 1:
            break

    return result // len(jobs) """

def solution(jobs):

    jobs.sort()

    jobs = list(map(lambda x: [x[1], x[0]], jobs))
    ori_length = len(jobs)
    length = jobs[0][1] + jobs[0][0]
    result = jobs[0][0]
    del jobs[0]

    while jobs:
        tmp = []
        for i in range(len(jobs)):
            if length >= jobs[i][1]:
                tmp.append(jobs[i])
            else:
                break
        if tmp:
            heapq.heapify(tmp)
            tmp = heapq.heappop(tmp)
            result += length - tmp[1] + tmp[0]
            length += tmp[0]
            del jobs[jobs.index(tmp)]
        else:
            length = jobs[0][0] + jobs[0][1]
            result += jobs[0][0]
            del jobs[0]

    return result // ori_length

print(solution([[0,3], [4,3], [10,3], [11,5], [15,4], [15,5]]))
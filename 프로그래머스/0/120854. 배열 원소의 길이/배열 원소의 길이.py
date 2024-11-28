def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# == [len(i) for i in strlist]
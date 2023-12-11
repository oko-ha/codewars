def solution(args):
    answer = ""
    temp = []
    for n in args:
        if temp:
            if temp[-1] + 1 == n:
                temp.append(n)
            else:
                if len(temp) < 3:
                    for t in temp:
                        answer += str(t) + ','
                else:
                    answer += str(temp[0]) + '-' + str(temp[-1]) + ','
                temp = [n]
        else:
            temp.append(n)
            
    if len(temp) < 3:
        for t in temp:
            answer += str(t) + ','
    else:
        answer += str(temp[0]) + '-' + str(temp[-1]) + ','
    return answer[:-1]
def bowling_score(frames):
    score = []
    strike = set()
    spare = set()
    flag = 0
    for f in frames:
        if f == ' ':
            flag += 1
            continue
        elif f == 'X':
            if flag < 9:
                strike.add(len(score))
            score.append(10)
        elif f == '/':
            if flag < 9:
                spare.add(len(score))
            score.append(10 - score[-1])
        else:
            score.append(int(f))
    
    for i in strike:
        score.append(score[i + 1] + score[i + 2])
    for i in spare:
        score.append(score[i + 1])
    
    return sum(score)
def plants_and_zombies(lawn, zombies):
    time = 0
    size_x, size_y = len(lawn), len(lawn[0])
    lawn_list = [[0 for _ in range(size_y)] for _ in range(size_x)]
    zombies_num = len(zombies)
    zombies_index = 0
    for i in range(size_x):
        for j in range(size_y - 1, -1, -1):
            if lawn[i][j] == 'S':
                lawn_list[i][j] = 10
            elif lawn[i][j] != ' ':
                lawn_list[i][j] = int(lawn[i][j])
    
    # 시뮬레이션 시작
    while zombies_num > 0:

        # 좀비 이동
        for i in range(size_x):
            for j in range(size_y):
                if lawn_list[i][j] < 0:
                    if j - 1 < 0:
                        return time
                    lawn_list[i][j - 1] = lawn_list[i][j]
                    lawn_list[i][j] = 0

        # 좀비 생성
        for i in range(zombies_index, len(zombies)):
            if zombies[i][0] != time:
                break
            x, hp = zombies[i][1], zombies[i][2]
            lawn_list[x][size_y - 1] = -hp
            zombies_index += 1

        # 일반 슈터 발사
        for i in range(size_x):
            for j in range(size_y):
                if lawn_list[i][j] > 0 and lawn_list[i][j] < 10:
                    pellets = -lawn_list[i][j]
                    for k in range(j + 1, size_y):
                        if lawn_list[i][k] < 0:
                            if lawn_list[i][k] > pellets:
                                pellets -= lawn_list[i][k]
                                lawn_list[i][k] = 0
                                zombies_num -= 1
                            else:
                                lawn_list[i][k] -= pellets
                                if lawn_list[i][k] == 0:
                                    zombies_num -= 1
                                break

        # S 슈터 발사
        for j in range(size_y - 1, -1, -1):
            for i in range(size_x):
                if lawn_list[i][j] > 9:
                    for k in range(j + 1, size_y):
                        if lawn_list[i][k] < 0:
                            lawn_list[i][k] += 1
                            if lawn_list[i][k] == 0:
                                zombies_num -= 1
                            break
                    for l, k in enumerate(range(j + 1, size_y)):
                        if i - l - 1 < 0:
                            break
                        if lawn_list[i - l - 1][k] < 0:
                            lawn_list[i - l - 1][k] += 1
                            if lawn_list[i - l - 1][k] == 0:
                                zombies_num -= 1
                            break
                    for l, k in enumerate(range(j + 1, size_y)):
                        if i + l + 1 >= size_x:
                            break
                        if lawn_list[i + l + 1][k] < 0:
                            lawn_list[i + l + 1][k] += 1
                            if lawn_list[i + l + 1][k] == 0:
                                zombies_num -= 1
                            break
        time += 1

    return None
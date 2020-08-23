# A. The Rank
# by hoanghust

n = int(input())
score_table = []

if n >= 1 and n <= 1000:
    for id in range(n):
        info = input().split()
        for num, i in enumerate(info):
            info[num] = int(i)
        info.insert(0, id+1)
        info.insert(5, info[1]+info[2]+info[3]+info[4])
        score_table.append(info)
    # output 1: [[id, score1, score2, score3, total score],...]

    for loop in range(len(score_table)-2):
        for student in range(len(score_table)-1):

            total_score_A = score_table[student][5]
            total_score_B = score_table[student+1][5]

            # Sort total score bigest -> smalest.
            if total_score_A < total_score_B:
                score_table.insert(student+2, score_table[student])
                score_table.pop(student)

            # If two ore more student with the same total score, Sort flowing ID (small first)
            if total_score_A == total_score_B:
                if score_table[student][0] > score_table[student+1][0]: # index = 0 for student ID position
                    score_table.insert(student+2, score_table[student])
                    score_table.pop(student)

    for rank in range(len(score_table)):
        # Print the rank of Thomas (ID = 1)
        if score_table[rank][0] == 1:
            print(rank+1)

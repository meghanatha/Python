List = [['0111', '0101', '0101', '0101', '0101', '1101']]
min_length = 0
i = 0
j = 0
while (i < len(List) and j < len(List[0]) and i >= 0 and j>= 0) :
    if j == 5 and i == 0:
        break
    if List[i][j][0] == '0':
        min_length += 1
        j += 1
    elif List[i][j][1] == '0':
        min_length += 1
        i -= 1
    elif List[i][j][2] == '0':
        min_length += 1
        j -= 1
    elif List[i][j][3] == '0':
        min_length += 1
        i += 1

print(min_length)
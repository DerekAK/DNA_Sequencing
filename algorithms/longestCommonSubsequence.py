def runAlgorithm(t,s):
    table = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
    for i in range(1,len(t) + 1):
        for j in range (1, len(s) + 1):
            if t[i-1] == s[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    lcs_length = table[len(t)][len(s)]
    return lcs_length
def runAlgorithm(t, s):
    # LCS table
    table = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i - 1] == s[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    
    score = 1000
    
    # Score based on longest common subsequence
    lcs_length_total = table[len(t)][len(s)]
    similarity_ratio = lcs_length_total / max(len(t), len(s))

    # Similarity score only if sequences are close in length
    if len(t) == len(s) or similarity_ratio > 0.9:
        score += similarity_ratio * 10

    # Length difference penalty with stronger impact
    length_diff = abs(len(t) - len(s))
    score -= length_diff * 20  # Increased weight for unmatched trailing characters

    # Apply direct penalties for character mismatches
    for i in range(min(len(t), len(s))):
        if t[i] != s[i]:
            score -= 2  # Penalty for each mismatch in overlapping regions

    # Additional penalty for trailing characters
    if len(t) > len(s):
        score -= ((len(t) - len(s)) * .5)
    elif len(s) > len(t):
        score -= ((len(s) - len(t)) * .5)

    return int(score)
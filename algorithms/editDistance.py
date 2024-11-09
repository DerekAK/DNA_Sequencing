import sys
sys.setrecursionlimit(10000)

# top down version, comment out bottom up version if want to use this one
# sims = {}
# def runAlgorithm(seqA, seqB):
#     if (seqA, seqB) in sims:  # Check memoization first
#         return sims[(seqA, seqB)]

#     if len(seqA) == 0:
#         sims[(seqA, seqB)] = len(seqB)
#         return sims[(seqA, seqB)]
#     if len(seqB) == 0:
#         sims[(seqA, seqB)] = len(seqA)
#         return sims[(seqA, seqB)]

#     # Check the cost of the last character match/mismatch
#     helper = 0 if seqA[-1] == seqB[-1] else 1

#     # Calculate the edit distances recursively
#     opt1 = runAlgorithm(seqA[:-1], seqB[:-1]) + helper  # Replace or match
#     opt2 = runAlgorithm(seqA[:-1], seqB) + 1  # Deletion
#     opt3 = runAlgorithm(seqA, seqB[:-1]) + 1  # Insertion

#     # Store the minimum edit distance in memoization dictionary
#     sims[(seqA, seqB)] = min(opt1, opt2, opt3)
#     return sims[(seqA, seqB)]


#bottom up version, comment out top down if want to use this one
def runAlgorithm(seqA, seqB):
    matrix = []
    for i in range(len(seqA)+1):
        matrix.append([0]*(len(seqB)+1))

    for i in range(len(seqA)+1):
        matrix[i][0] = i
    for i in range(len(seqB)+1):
        matrix[0][i] = i
    
    for i in range(1, len(seqA)+1):
        for j in range(1, len(seqB)+1):
            helper = 0 if seqA[i-1] == seqB[j-1] else 1
            insertionScore = matrix[i][j-1]+1
            deletionScore = matrix[i-1][j] + 1
            substitutionScore = matrix[i-1][j-1] + helper
            matrix[i][j] = min(insertionScore, deletionScore, substitutionScore)
    return matrix[-1][-1]

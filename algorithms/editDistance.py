import sys
sys.setrecursionlimit(10000)
# def runAlgorithm(seqA, seqB):
#     if len(seqA) == 0:
#         return len(seqB)
#     if len(seqB) == 0:
#         return len(seqA)

#     helper = 0 if seqA[-1] == seqB[-1] else 1

#     return min(runAlgorithm(seqA[:-1], seqB[:-1]) + helper,
#         runAlgorithm(seqA[:-1], seqB) + 1, 
#         runAlgorithm(seqA, seqB[:-1]) + 1) 

sims = {}
def runAlgorithm(seqA, seqB):
    if len(seqA) == 0:
        sims[(seqA, seqB)] = len(seqB)
        return sims[(seqA, seqB)]
    if len(seqB) == 0:
        sims[(seqA, seqB)] = len(seqA)
        return sims[(seqA, seqB)]

    helper = 0 if seqA[-1] == seqB[-1] else 1
    if (seqA[:-1], seqB[:-1]) in sims:
        opt1 = sims[(seqA[:-1], seqB[:-1])] + helper
    else:
        opt1 = runAlgorithm(seqA[:-1], seqB[:-1]) + helper
    
    if (seqA[:-1], seqB) in sims:
        opt2 = sims[(seqA[:-1], seqB)] + 1
    else:
        opt2 = runAlgorithm(seqA[:-1], seqB) + 1
    
    if (seqA, seqB[:-1]) in sims:
        opt3 = sims[(seqA, seqB[:-1])] + 1
    else:
        opt3 = runAlgorithm(seqA, seqB[:-1]) + 1

    sims[(seqA, seqB)] = min(opt1, opt2, opt3)
    return sims[(seqA, seqB)]

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


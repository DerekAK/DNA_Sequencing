def runAlgorithm(seqA, seqB):

    # seqA = "shakespeare"
    # seqB = "shake"

    # print("\n\n\n\n\n\wtf")
    # print(seqA,"\n\n", seqB)
    # print("\n\n\n\n\n\wtf")

    # if len(seqA) == 0:
    #     return len(seqB)
    # if len(seqB) == 0:
    #     return len(seqA)
    
    # return min(runAlgorithm(seqA[:-1], seqB[:-1]) + help(seqA[-1], seqB[-1]), #if seqA[0] == seqB[0], 0
    #     runAlgorithm(seqA[:-1], seqB) + 1, #this is for inserting a letter into seqA to pair up with seqB[-1]
    #     runAlgorithm(seqA, seqB[:-1]) + 1) #this is for inserting a letter into seqB to pair up with seqA[-1]

    return 5

def help(x, y):
    return 0 if x == y else 1
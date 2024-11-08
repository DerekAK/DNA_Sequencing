import datetime as d
from algorithms import editDistance, longestCommonSubstring, longestCommonSubsequence, customAlgorithm

ALGORITHMS = {
    'EditDistance': editDistance,
    'LongestCommonSubstring': longestCommonSubstring,
    'LongestCommonSubsequence': longestCommonSubsequence,
    'CustomAlgorithm': customAlgorithm
}
def parseDNASeqs(file):
    seqs = {}
    file_path = 'dnaSequences/'+str(file)
    file_object = open(file_path, mode='r', encoding='utf-8')
    currSeq = None
    for line in file_object:
        line = line.strip() # get rid of "\n" characters
        if line[0] == ">":
            currSeq = line
            seqs[currSeq] = ""
        else: # an actual DNA sequence line
            seqs[currSeq] += line
    # for seq in seqs:
    #     print(seq)
    file_object.close()
    return seqs

def parseDNAQuery(file):
    file_path = 'dnaQueries/'+str(file)
    file_object = open(file_path, mode='r', encoding='utf-8')
    s = ""
    for line in file_object:
        line = line.strip()
        s += line
    file_object.close()
    return s


def runAlgorithmLow(DNAQuery, DNASeqs, algoType):
    s_t = d.datetime.now()

    DNASeqs = parseDNASeqs(DNASeqs)
    DNAQuery = parseDNAQuery(DNAQuery)

    bestSim = 2**31
    bestSeq = None
    for seq in DNASeqs:
        print("Sequence name:", seq)
        print("Length of sequence:", len(str(DNASeqs[seq])))
        algorithm = ALGORITHMS[algoType]
        currSim = algorithm.runAlgorithm(str(DNASeqs[seq]), DNAQuery)
        #currSim = algorithm.runAlgorithm("Shakespeare", "shake spear")
        print("Sim Score:", currSim, "\n")
        if currSim < bestSim:
            bestSim = currSim
            bestSeq = seq
    e_t = d.datetime.now()
    totalTime = (e_t - s_t).total_seconds()

    return bestSeq, bestSim, totalTime

def runAlgorithmHigh(DNAQuery, DNASeqs, algoType):
    s_t = d.datetime.now()

    DNASeqs = parseDNASeqs(DNASeqs)
    DNAQuery = parseDNAQuery(DNAQuery)

    bestSim = -(2**31)
    bestSeq = None
    for seq in DNASeqs:
        print("Sequence name:", seq)
        print("Length of sequence:", len(DNASeqs[seq]))
        # print("Sequence itself:", DNASeqs[seq])
        # print("Query sequence:", DNAQuery)
        algorithm = ALGORITHMS[algoType]
        currSim = algorithm.runAlgorithm(DNASeqs[seq], DNAQuery)
        #currSim = algorithm.runAlgorithm("Shakespeare", "shake spear")
        print("Sim Score:", currSim, "\n")
        if currSim > bestSim:
            bestSim = currSim
            bestSeq = seq
    e_t = d.datetime.now()
    totalTime = (e_t - s_t).total_seconds()

    return bestSeq, bestSim, totalTime


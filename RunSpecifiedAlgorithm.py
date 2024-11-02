import datetime as d
from algorithms import editDistance

ALGORITHMS = {
    'EditDistance': editDistance
}
def parseDNASeqs(file):
    seqs = {}
    file_path = 'dnaSequences/'+str(file)
    file_object = open(file_path, mode='r', encoding='utf-8')
    currSeq = None
    for line in file_object:
        if line[0] == ">":
            currSeq = line
            seqs[currSeq] = ""
        else: # an actual DNA sequence line
            line = line.strip() # get rid of "\n" characters
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
        s += line
    file_object.close()
    return s


def runAlgorithm(DNAQuery, DNASeqs, algoType):
    s_t = d.datetime.now()

    DNASeqs = parseDNASeqs(DNASeqs)
    DNAQuery = parseDNAQuery(DNAQuery)

    bestSim = (2**31)
    bestSeq = None
    for seq in DNASeqs:
        print(seq)
        algorithm = ALGORITHMS[algoType]
        currSim = algorithm.runAlgorithm(str(DNASeqs[seq]), DNAQuery)
        print(len(str(DNASeqs[seq])))
        #currSim = algorithm.runAlgorithm("Shakespeare", "shake spear")
        if currSim < bestSim:
            bestSim = currSim
            bestSeq = seq
    e_t = d.datetime.now()
    totalTime = (e_t - s_t).total_seconds()

    return bestSeq, bestSim, totalTime


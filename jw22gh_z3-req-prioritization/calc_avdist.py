
#Much of the calculating code has been translated from the Java version of it, found at http://francis-palma.net/wp-content/uploads/2016/07/Project.zip

def calc_avdist(req_order, gs):

    gold_standard = gs

    numreq = len(req_order)
    diffSum = 0
    averageDistance = 0

    for j in range(numreq):
        tmp = req_order[j]
        indxIndv = j
        indxDiff = 0
        indxGS = 0

        for k in range(numreq):
            if gold_standard[k][2:] == tmp[2:]:
                indxGS = k

        if indxIndv < indxGS:
            indxDiff = indxGS - indxIndv
        else:
            indxDiff = indxIndv - indxGS
        diffSum = diffSum + indxDiff

        averageDistance = diffSum / numreq
    return averageDistance            

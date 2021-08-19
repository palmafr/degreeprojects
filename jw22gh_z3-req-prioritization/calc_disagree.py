
#Much of the calculating code has been translated from the Java version of it, found at http://francis-palma.net/wp-content/uploads/2016/07/Project.zip

def calc_dis(req_order, gs):

    gold_standard = gs
    disagreeList = []

    totalDisAgreeGS = 0
    NUMREQ = len(req_order)

    for i in range(NUMREQ):
        j = i + 1
        while j < NUMREQ:
            fOsrc = req_order[i]
            fOindxsrc = i

            fOdst = req_order[j]
            fOindxdst = j

            gsindxsrc = 0
            gsindxdst = 0

            for k in range(NUMREQ):
                if int(gold_standard[k][2:]) == int(fOsrc[2:]):
                    gsindxsrc = k

                if int(gold_standard[k][2:]) == int(fOdst[2:]):
                    gsindxdst = k
            if fOindxsrc <= fOindxdst and gsindxsrc <= gsindxdst:
                j += 1
                continue
            else:
                totalDisAgreeGS += 1
                disagreeList.append(fOsrc + " " + fOdst)          
                j += 1
    return totalDisAgreeGS
   

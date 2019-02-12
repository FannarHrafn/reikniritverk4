def fall(L):
    haesta = max(L)
    countL = [0]*(haesta+1)
    resutlL = [0]*len(L)

    for i in L:
        countL[i] += 1

    summa = 0
    for i in range(len(countL)):
        print countL
        print countL[i]
        summa += countL[i]
        print summa
        countL[i] = summa
        print countL

    for i in range(len(L)):
        print L[i]
        print countL[L[i]]
        resutlL[countL[L[i]]-1] = L[i]
        print resutlL
        countL[L[i]] -= 1

    return resutlL

L = [0,0,7,1,8,2,5,10,8,9,3,6,1]
print fall(L)

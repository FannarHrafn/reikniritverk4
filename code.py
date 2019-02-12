def fall(L):
    haesta = max(L)
    countL = [0]*(haesta+1)
    resutlL = [0]*len(L)

    for i in L:
        countL[i] += 1

    summa = 0
    for i in range(len(countL)):
        summa += countL[i]
        countL[i] = summa

    for i in range(len(L)):
        resutlL[countL[L[i]]-1] = L[i]
        countL[L[i]] -= 1

    return resutlL

L = [0,0,7,1,8,2,5,10,8,9,3,6,1]
print fall(L)

linearlist = [8,5,3,7,1,9,2,6]

def linearsearch(list,Z):
    counter = 0
    for x in list:
        if x == Z:
            return counter
        else:
            counter += 1
print linearsearch(linearlist,7)


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

def linearsearch(list,search):
    for x in range(len(list)):
        if list[x] == search:
            return x

print linearsearch(linearlist,7)


binarylist = [1,2,3,5,6,7,8,9]
"""
print "binary"
def binarysearch(listi,target):
    middle = listi[len(listi)//2]
    print listi
    print middle

    if middle == target:
        return "index: " + str(listi[len(listi)/2]-1)
    elif middle > target:
        return binarysearch(listi[:middle-1],target)
    elif middle < target:
        return binarysearch(listi[middle-1:],target)
"""
#print(binarysearch(binarylist,7))
def binarysearch(listi,l,h,target):
    if l<h:
        middle = (l + (h-1))/2
        print listi
        print middle

        if listi[middle] == target:
            return middle
        elif listi[middle] > target:
            return binarysearch(listi,l,middle-1,target)
        elif listi[middle] < target:
            return binarysearch(listi,middle+1,h,target)
    else:
        return -1

print(binarysearch(binarylist,0,len(binarylist),7))

















#geyma tetta til seinna
'''
class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d:
            return False
        elif self.value > d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True
class Tree:
    def __index__(self):
        self.root = None

    def insert(self,d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True
t = Tree()
print (t.insert(6))
print (t.insert(2))
print (t.insert(3))
print (t.insert(7))
'''

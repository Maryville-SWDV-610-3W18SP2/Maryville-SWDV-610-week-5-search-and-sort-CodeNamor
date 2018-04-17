#F. Derek Roman - SWDV610 Data Structures
#Assigment 5.1.1 Buble sort an algorithm
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [1,2,3,4,5,6,7,8,9,10]
bubbleSort(alist)
print(alist)
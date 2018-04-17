#F. Derek Roman - SWDV610 Data Structures
#Assigment 5.1.2 Selection sort an algorithm
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
    for location in range(1,fillslot+1):
        if alist[location]>alist[positionOfMax]:
            positionOfMax = location
            
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
            
alist = [1,2,3,4,5,6,7,8,9,10]
selectionSort(alist)
print(alist)
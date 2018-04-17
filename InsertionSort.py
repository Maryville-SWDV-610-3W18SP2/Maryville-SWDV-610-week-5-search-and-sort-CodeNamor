#F. Derek Roman - SWDV610 Data Structures
#Assigment 5.1.2 Selection sort an algorithm
def insertionSort(alist):
    #travers through the list
 for index in range(1,len(alist)):
     #get the value of the index and the position in the list
     currentvalue = alist[index]
     position = index
     #run the sort based upon position and current value
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
         #swap positions if needed
         alist[position]=currentvalue
#define the list and call the function, then print out
#this tests the above and verifies that it is working
#swapping 10 and 1 in the list for proving that it is working
alist = [10,2,3,4,5,6,7,8,9,1]
insertionSort(alist)
print(alist)
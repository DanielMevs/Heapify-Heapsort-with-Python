import math
def left(i, arr):
    return math.floor((2*i)+1)

def right(i,arr):
    right = math.floor(2*(i+1))
    return int(right)

def parent(i, arr):
    parent = math.floor((i-1)/2)
    return int(parent)

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def maxHeapify(arrSize, i, arr):

    leftArrIndex = left(i, arr)
    rightArrIndex = right(i, arr)
    #print(leftArrIndex)
    #print(rightArrIndex)
    if (rightArrIndex == arrSize):
        if((i<arrSize) and arr[leftArrIndex] > arr[i]):
            indexOfLargest = leftArrIndex
        else:
            indexOfLargest = i

        if(indexOfLargest != i):
            swap(i,indexOfLargest, arr)
    else:
        if((i<arrSize) and arr[leftArrIndex] > arr[i]):
            indexOfLargest = leftArrIndex
        else:
            indexOfLargest = i
        if((i<arrSize) and arr[rightArrIndex] > arr[i] and arr[rightArrIndex] > arr[leftArrIndex]):
            indexOfLargest = rightArrIndex

        if(indexOfLargest != i):
            swap(i,indexOfLargest, arr)
            maxHeapify(arrSize, indexOfLargest, arr)
        
    

def buildHeap(arr):
    heapSize = int(len(arr))
    i = int(math.floor((heapSize/2)-1))
    #print(i)
    while(i>=0):
        maxHeapify(heapSize, i, arr)
        i = i - 1
def heapSort(arr):
    i = int(len(arr)-1)
    while(i >= 0):
        swap(0, i, arr)
        print(arr)
        i = i - 1
        maxHeapify(i, 0, arr)
        
        print(arr)
        
        print(i)
        
#priority queue operations.(priority queues work most efficiently with heaps as the set of keys)
def getMaximum(arr):
    return arr[0]

def extractMaximum(arr, heapSize):
    if(heapSize < 1):
        print("heap is empty")
    maximum = arr[0]
    arr[0] = arr[heapSize-1]
    heapSize = heapSize- 1
    maxHeapify(heapSize, 0, arr)
        
l = [2,45,63,23,26,6]
buildHeap(l)
print(l, "\n")
extractMaximum(l, len(l))
print(l, "\n")
#heapSort(l)



    

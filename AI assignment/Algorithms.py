import random

def BubbleSort(arr):
    for i in range( len(arr)):

        for j in range ( len(arr)-i-1 ):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

def SelectionSort(arr):
    for i in range( len(arr)):
        min=i
        
        for j in range( i,len(arr),1):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]


def LinearSearch(arr,element):
    
    for i in range (len(arr)):
        if arr[i]==element:
            print("Found!")
            return i

    print("Not Found!")
    return -1



def InsertionSort(arr):

    for i in range (1,len(arr),1):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        

def CountingSort(arr):
    size = len(arr)
    output = [0] * size-1
    count = [0] * 10
    for i in range(0, size):
        count[arr[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(0, size):
        arr[i] = output[i]



def BinarySearch(arr,element,start,end):

    if start>end:
        print("Not Found!")
        return -1

    mid=int(start + (end-start)/2 )
    
    if element==arr[mid-1]:
        print("Found!")
        return mid-1

    elif element<arr[mid-1]:
        return BinarySearch(arr,element,start,mid-1)

    elif element>arr[mid-1]:
        return BinarySearch(arr,element,mid+1,end)


arr=[10,2,3,11,222,113,1,-1]



"""BubbleSort(arr)

print(arr)

random.shuffle(arr)


print(arr)


SelectionSort(arr)


print(arr)


print(arr)


print(BinarySearch(arr,10,0,len(arr)))


BubbleSort(arr)

BinarySearch(arr,-1000,0,len(arr))
"""

CountingSort(arr)

print(arr)
 
list = [1,2,3,5,4,6,7]

def findMedian(arr):
    arr.sort()
    print(arr[int(len(arr)/2)])


findMedian(list)

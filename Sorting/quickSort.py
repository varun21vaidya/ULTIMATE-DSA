arr = [3,7,2,8,4,9,1]
print("quick sort input",(arr))
def quickSortAlgo(arr):
    n=len(arr)
    return quickSort(arr, 0 , n-1)

def partition(arr, left, right,pivot):
    while left<=right:
        while arr[left]<pivot:
            left+=1
        while arr[right]>pivot:
            right-=1
        if left<=right:
            arr[left],arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    return left

def quickSort(arr, start, end):
    if start<end:
        mid = (end+start)//2
        pivot = arr[mid]
        index = partition(arr, start, end,pivot)
        quickSort(arr, start, index-1)
        quickSort(arr, index, end)
    return arr


print("quick sort output",quickSortAlgo(arr))





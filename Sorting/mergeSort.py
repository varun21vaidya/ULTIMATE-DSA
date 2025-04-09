arr = [3,7,2,8,4,9,1]
print("merge sort input",(arr))
n = len(arr)
def mergeSortAlgo(arr):
    return mergeSort(arr, 0, n-1)

def mergeSort(arr, start,end):
    if start<end:
        mid = (end+start)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        return merge(arr, start ,mid, end)

def merge(arr, start,mid,end):
    temp = []
    i,j,k= start, mid+1, 0
    while i<=mid and j<=end:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=end:
        temp.append(arr[j])
        j+=1
    while k<len(temp):
        arr[start+k]=temp[k]
        k+=1
    return arr

print("merge sort output",mergeSortAlgo(arr))





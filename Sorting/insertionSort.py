arr = [3,7,2,8,4,9,1]
print("insertion sort input",(arr))
def insertionSort(arr):
    n=len(arr)
    for a in range(1, n):
        b=a
        while b>0 and arr[b]<arr[b-1]:
            arr[b],arr[b-1]= arr[b-1],arr[b]
            b-=1
    return arr
        


print("insertion sort output",insertionSort(arr))





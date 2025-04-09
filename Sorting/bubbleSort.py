arr = [3,7,2,8,4,9,1]
print("bubble sort input",(arr))
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swapped =True
        if not swapped:
            break
    return arr

print("bubble sort output",bubbleSort(arr))





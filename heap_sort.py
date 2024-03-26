def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[left]>arr[largest]:
        largest=left

    if right<n and arr[right]>arr[largest]:
        largest=right

    if largest !=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n=len(arr)

    #build a max heap
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    #extract elements from the heap one by one
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i] #swap the root (maximum) elements with the elements
        heapify(arr,i,0)

    return arr

arr=[5,2,4,3,1,9,6,7,8]
sorted_arr=heap_sort(arr)
print(sorted_arr)
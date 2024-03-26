def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        #find the index of the minimum elemnts in the unsorted part of the array
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        # swap the minimum elements with the first unsorted element
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

arr=[5,2,9,1,7,6,4,8,3]
sorted_arr=selection_sort(arr)
print(sorted_arr)
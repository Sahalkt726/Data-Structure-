def binary_search(arr,target):
    left,right=0,len(arr)-1

    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1   #return -1 if the target element is not found

my_list=[2,4,6,8,10,12,14,16,18,20]
target_element=4

result=binary_search(my_list,target_element)

if result !=-1:
    print(f"Element {target_element} found at index {result}")
else:
    print("Element not found in the list")

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
    
my_list=[4,2,7,1,9,5]
target=9

result=linear_search(my_list,target)

if result!=-1:
    print(f"Element {target} found at index:{result}")

else:
    print(f"Element {target} not found in the list")

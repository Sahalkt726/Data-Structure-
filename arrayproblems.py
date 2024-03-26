# #in another way we can use hash set

def find_pairs(arr,target_sum):
    pairs =[]
    complements = set()

    for num in arr:
        complement=target_sum-num
        if complement in complements:
            pairs.append((num,complement))
        complement.add(num)

    return pairs

arr=[6,2,3,9,0,4,5,8]
target_sum=10


# #in an array arr=[6,9,0,1,2,6,5,10,8,6,7,15,6] i need to make all 6 in the right side and all others left

def move_six_to_right(arr):
    left = 0 
    right = len(arr)-1

    while left<right:
        if arr[left]==6:
            if arr[right] != 6:
                arr[left],arr[right] = arr[right], arr[left]
                right -=1
            else:
                right -=1
        else:
            left +=1

    return arr

arr=[6,9,0,1,2,6,5,10,8,6,7,15,6]
result =move_six_to_right(arr)
print(result)



def find_max_repeat_element(arr):
    element_count = {}

    #counut the occurence of each element in the array 
    for element in arr:
        if element in element_count:
            element_count[element]+=1
        else:
            element_count[element]=1

    max_repeating_element =None
    max_count=0

    #find the element with the maximum count
    for element, count in element_count.items():
        if count>max_count:
            max_count=count
            max_repeating_element=element

    return max_repeating_element
    #example usage:
string_array=['apple','banana','apple','orange','banana','apple','apple']
result=find_max_repeat_element(string_array)
print("The element repeating the maximum number of items is:",result)
# def merge(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     left=merge(left)
#     right=merge(right)
#     return merge_sort(left,right)

# def merge_sort(a,b):
#     sorted_list=[]
#     len_a=len(a)
#     len_b=len(b)
#     i=j=0

#     while i<len_a and j<len_b:
#         if a[i]<=b[j]:
#             sorted_list.append(a[i])
#             i+=1
#         else:
#             sorted_list.append(b[j])
#             j+=1
#     while i<len_a:
#         sorted_list.append(a[i])
#         i+=1
#     while j<len_b:
#         sorted_list.append(b[j])
#         j+=1
#     return sorted_list

# if __name__=='__main__':
#     arr=[10,34,12,49,56,100,21,9,32,67,101]
#     print(merge(arr))





# #reduce space
def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge(left)
    right=merge(right)
    return merge_sort(left,right,arr)

def merge_sort(a,b,arr):
    len_a=len(a)
    len_b=len(b)
    i=j=k=0

    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k]=b[j]
        j+=1
        k+=1
    return arr

if __name__ =='__main__':
    arr=[10,34,12,49,56,100,21,9,32,67,101]
    print(merge(arr))

        
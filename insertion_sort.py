def insertion_sort(A):
    for i in range(1,len(A)):
        anchor=A[i]
        j=i-1
        while j>=0 and anchor<A[j]:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=anchor

A=[11,9,29,7,2,15,28]
insertion_sort(A)
print(A)

test=[
    [11,9,29,7,2,15,28],
    [2,30,1,10],
    [],
    [3]
]
for elements in test:
    insertion_sort(elements)
    print(elements)

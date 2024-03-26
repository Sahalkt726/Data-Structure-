#write the same programme to get the same answer in different way to know what is big O notation.
def fun(n):
    total_sum= 0 #0(1)
    for i in range(1,n+1):
        total_sum +=i #O(1)
    return total_sum #O(1) so the total time complexity=O(n) bcz others are negotiable bcz they are constant

print(fun(5))

#in this programme the time complexity is O(n)

def fun(n):
    total_sum = n*(n+1)/2 #O(1)
    return total_sum #O(1)
x=5
print(fun(x)) #O(1)

#in this programme the time compelexity is O(1)+O(1)+O(1)+ so O(3) it is a constant and considered as O(1)

#O(1) is the most efficient algorithms


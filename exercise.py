def longest_switching_slice(A):
    max_length = 1
    current_length = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]
        current_length +=1
    else:
        current_length=1
    max_length = max(max_length, current_length)
    return max_length
A=[7,8,7,8]
longest_slice = (longest_switching_slice)
print(longest_slice)
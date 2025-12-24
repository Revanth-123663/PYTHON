A = [-10, -5, 0, 5, 10]

def binary_search(arr, target):
    N = len(A)
    L = 0
    R = N - 1
    
    while L <= R:
        M = L + ((R - L) // 2)
        if arr[M] == target:
            return True
        elif target > arr[M]:
            L = M + 1
        else:
            R = M - 1
    return False
print(binary_search(A, 10))

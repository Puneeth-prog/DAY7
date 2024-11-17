# Function to find the minimum value
def findMin(arr):
    res = arr[0]

    for i in range(1, len(arr)):
        res = min(res, arr[i])

    return res

# Driver code
arr = [120, 25, 31, 42, 33, 54]
print(findMin(arr))

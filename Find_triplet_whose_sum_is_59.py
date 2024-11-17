# Python program to find triplet with sum zero
# using three nested loops

def findTriplets(arr):
    res = []
    n = len(arr)

    # Generating all triplets
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):

                # If the sum of triplet equals to zero
                # then add it's indexes to the result
                if arr[i] + arr[j] + arr[k] == 59:
                    res.append([i, j, k])
    return res


arr = [10, 20, 30, 9]
res = findTriplets(arr)
for triplet in res:
    print(triplet[0], triplet[1], triplet[2])

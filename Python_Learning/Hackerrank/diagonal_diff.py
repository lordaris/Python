def diagonalDifference(arr):
    a, b, c = 0, 0, len(arr)
    for x, row in enumerate(arr):
        y= c - x - 1
        a+=arr[x][x]
        b+=arr[x][y]
    return abs(a - b)


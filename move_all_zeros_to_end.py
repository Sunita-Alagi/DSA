def move_zero_to_end(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    print(arr)


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

move_zero_to_end(arr)

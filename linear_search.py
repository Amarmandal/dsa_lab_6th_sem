def linear_search(arr, x):

    for i in range(0, len(arr)):
        if(arr[i] == x):
            return i
    return -1


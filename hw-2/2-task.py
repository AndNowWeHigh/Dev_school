def task_2(arr):
    sum_arr = sum(arr)
    left_sum = 0

    for index in range(len(arr)):
        sum_arr -= arr[index]
        if left_sum == sum_arr:
            return index
        left_sum += arr[index]
    else:
        return -1

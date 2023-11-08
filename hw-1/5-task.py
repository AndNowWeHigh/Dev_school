def task_5(string):
    list_num = [int(num) for num in string.split()]

    min_num = 0
    max_num = 0

    for i in list_num:
        if max_num < i:
            max_num = i
        elif min_num > i:
            min_num = i
        else:
            continue
    return max_num, min_num

print(task_5("1 9 3 4 -5"))

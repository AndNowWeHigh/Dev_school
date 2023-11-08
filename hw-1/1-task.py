def task_1(num):
    if num < 0:
        return 0
    result = 0
    for x in range(num):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    else:
        return result

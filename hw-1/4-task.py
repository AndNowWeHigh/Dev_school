def task_4(n):
    # якщо число(n = a * b) можна розкласти на два нетривіальні дільник, то min{a, b} =< n**(1/2)*Лема із т."Сито Ератосфена"*
    a = int(n**(1/2))

    if n == 1:
        return False
    if n == 2:
        return True
    elif n > 1:
        for num in range(2, a+1):
            if n % num == 0:
                return False
            else:
                continue
    return True

print(task_4(169))


def task_1(list1, d):
    tuple_for_groups = {}
    for i, value in enumerate(list1):
        group_index = i % d             # Обчислили індекс групи за допомогою поточної позиції
        if group_index not in tuple_for_groups:
            tuple_for_groups[group_index] = []
        tuple_for_groups[group_index].append(value)

    summed_honor = 0
    for key in tuple_for_groups.keys():
        group_sum = sum(tuple_for_groups[key])
        if group_sum > summed_honor:
            summed_honor = group_sum

    return summed_honor



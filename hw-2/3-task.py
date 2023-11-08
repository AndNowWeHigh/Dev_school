def task_3(array):
    tuple1 = {}

    for word in array:
        sorted_word = ''.join(sorted(word))

        if sorted_word in tuple1:
            tuple1[sorted_word].append(word)
        else:
            tuple1[sorted_word] = [word]

    return print(*(list(tuple1.values())))









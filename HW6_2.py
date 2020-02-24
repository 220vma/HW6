def ap1():
    some_list = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]

    count =[]
    result = []
    
    for i in range(len(some_list)-1):
        if some_list[i] == some_list[i + 1]:
            count.append(some_list[i])
        else:
            result.append((some_list[i], len(count) + 1))
            count = []
    if not count:
        result.append((some_list[-1], 1))
    else:
        result.append((some_list[-1], len(count)+1))

    return result
    
print(ap1())
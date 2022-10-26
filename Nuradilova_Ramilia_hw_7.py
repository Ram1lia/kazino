def binary_search(val, lst):
    first = 0
    N = (len(lst))
    found = False
    while first + 1 < N:
        middle = int((first + N) / 2)
        if lst[middle] == val:
           first  = N = middle
           found = True
        elif lst[middle] > val:
            N = middle
        else:
            first = middle + 1
    if found:
        print(f'элемент по индексом: {first}')
    else:
        print('такого элемента нет')

def bubble_sort(lst):
    for k in range(1, len(lst)):
        for i in range(1, len(lst) - k + 1):
            if lst[i] < lst[i - 1]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
    return lst

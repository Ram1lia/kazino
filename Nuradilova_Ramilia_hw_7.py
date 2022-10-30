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


    def create_products(conn):
        create_product(conn, ('dirol', 35.50, 5))  # 1
        create_product(conn, ('гномик', 25.00, 10))  # 2
        create_product(conn, ('кола 2л', 120.00, 8))  # 3
        create_product(conn, ('NITRO', 62.40, 12))  # 4
        create_product(conn, ('хлеб', 20, 5))  # 5
        create_product(conn, ('тоналка', 600.99, 2))  # 6
        create_product(conn, ('Мыло', 108.60, 7))  # 7
        create_product(conn, ('mascakara', 400, 20))  # 8
        create_product(conn, ('lipstick', 250.00, 6))  # 9
        create_product(conn, ('mackbook', 105000.00, 3))  # 10
        create_product(conn, ('Alpen Gold', 114.59, 4))  # 11
        create_product(conn, ('water', 19.40, 8))  # 12
        create_product(conn, ('Моющее средство', 73.70, 4))  # 13
        create_product(conn, ('Порошок', 250.00, 3))  # 14
        create_product(conn, ('Подсолнечное Масло', 240.00, 5))  # 15
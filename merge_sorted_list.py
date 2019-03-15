def merge_lists(list_a, list_b):
    """

    :rtype: object
    """
    list_c = []
    while list_a and list_b:
        if list_a[len(list_a) - 1] > list_b[len(list_b) - 1]:
            list_c.append(list_a.pop())
        elif list_a[len(list_a) - 1] < list_b[len(list_b) - 1]:
            list_c.append(list_b.pop())
        else:
            list_b.pop()
    return (list_c + list_a[::-1] + list_b[::-1])[::-1]


a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 4, 5]

print(merge_lists(a, b))

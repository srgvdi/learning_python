# Given an integer array, output all the unique pair that sum up to a specific value k


def array_pair_num(array, k):

    if len(array) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for number in array:
        target = k - number
        if target not in seen:
            seen.add(number)
        else:
            output.add(((min(number, target)), max(number, target)))

    print('\n'.join(map(str, list(output))))


array_pair_num([1, 2, 3, 5, 6, -2, 4, 3, 0, 2, 1], 4)

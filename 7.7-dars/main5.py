# misol linki   https://www.codewars.com/kata/5a043724ffe75fbab000009f/train/python


def reverse_middle(lst):
    if len(lst) < 4:
        raise ValueError("List must have at least four elements")

    if len(lst) % 2 == 0:
        middle_indices = [len(lst) // 2 - 1, len(lst) // 2]
    else:
        middle_indices = [len(lst) // 2 - 1, len(lst) // 2, len(lst) // 2 + 1]

    reversed_middle = lst[middle_indices[0]:middle_indices[-1] + 1][::-1]

    return reversed_middle

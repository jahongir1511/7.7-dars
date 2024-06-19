#  misol linki  https://www.codewars.com/kata/5809c661f15835266900010a/train/python

def double_every_other(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    result = []
    for i, num in enumerate(lst):
        if i % 2 == 1:
            result.append(num * 2)
        else:
            result.append(num)

    return result


print(double_every_other([1, 2, 3, 4]))
print(double_every_other([5, 6, 7, 8, 9]))
print(double_every_other([0, 1]))
print(double_every_other([1]))
print(double_every_other([]))

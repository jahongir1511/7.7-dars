# misol linki https://www.codewars.com/kata/586ec0b8d098206cce001141/train/python


def inverse_slice(items, a, b):
    b = min(b, len(items))
    return items[:a] + items[b:]

print(inverse_slice([12, 14, 63, 72, 55, 24], 2, 4))
print(inverse_slice([1, 2, 3, 4, 5], 1, 3))
print(inverse_slice([10, 20, 30, 40, 50], 0, 2))
print(inverse_slice([10, 20, 30, 40, 50], 3, 10))
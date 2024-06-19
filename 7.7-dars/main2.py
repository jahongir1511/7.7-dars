# misol linki https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    return [item for item in lst if isinstance(item, int)]


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))

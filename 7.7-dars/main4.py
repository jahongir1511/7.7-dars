# misol linki  https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef/train/python


def find_children(santas_list, children):
    unique_children = set()

    for child in santas_list:
        if child in children:
            unique_children.add(child)

    return sorted(unique_children)


santas_list = ["Sam", "Joe", "Jane", "Bob", "Sam"]
children = ["Jane", "Joe", "Sam", "Bob", "Mary", "John"]

result = find_children(santas_list, children)
print(result)

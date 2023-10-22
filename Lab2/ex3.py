def operations(a, b):
    intersection = [item for item in a if item in b]
    union = a + [item for item in b if item not in a]
    a_minus_b = [item for item in a if item not in b]
    b_minus_a = [item for item in b if item not in a]

    return intersection, union, a_minus_b, b_minus_a


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result = operations(list_a, list_b)
intersection, union, a_minus_b, b_minus_a = result

print(f"intersection: {intersection}")
print(f"union: {union}")
print(f"a-b: {a_minus_b}")
print(f"b-a: {b_minus_a}")

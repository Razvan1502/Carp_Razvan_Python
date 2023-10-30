def function10(*lists):
    max_length = max(len(lst) for lst in lists)
    result = []

    for i in range(max_length):
        tuple_items = tuple(lst[i] if i < len(lst) else None for lst in lists)
        result.append(tuple_items)

    return result

def main():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c"]

    result = function10(list1, list2, list3)
    print(result)


if __name__ == "__main__":
    main()

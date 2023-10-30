
def function6( count, *lists,):

    all_lists = []
    return_list = []
    for i in lists:
        all_lists += i
    for item in all_lists:
        if all_lists.count(item) == count and item not in return_list:
            return_list.append(item)

    return return_list

list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 4, 4, 5]
list3 = [4, 5, 6, 6, 7]
x = 2

print(function6(x, list1, list2, list3))


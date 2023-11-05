def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False

    for key in dict1:
        if key not in dict2:
            return False

        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            #nested dict
            if not compare_dicts(value1, value2):
                return False
        elif isinstance(value1, (list, tuple, set)) and isinstance(value2, (list, tuple, set)):
            if len(value1) != len(value2):
                return False

            if sorted(value1) != sorted(value2):
                return False
        else:
            if value1 != value2:
                return False

    return True

def main():
 dict_1 = {'a': 1, 'b': [1, 2, 3], 'c': {'x': 10, 'y': [5, 6]}}
 dict_2 = {'a': 1, 'b': [3, 2, 1], 'c': {'y': [6, 5], 'x': 10}}

 result = compare_dicts(dict_1, dict_2)
 print(result)

if __name__ == "__main__":
    main()
def count_unique_and_duplicates(input_list):
    unique = len(set(input_list))
    duplicate = len(input_list) - unique
    return unique, duplicate


def main():
 my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
 result = count_unique_and_duplicates(my_list)
 print(result)


if __name__ == "__main__":
    main()
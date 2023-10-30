def generate_ascii_lists(x=1, strings=None, flag=True):
    if strings is None:
        return []

    result = []
    for string in strings:
        char_list = []
        for char in string:
            if (flag and ord(char) % x == 0) or (not flag and ord(char) % x != 0):
                char_list.append(char)
        result.append(char_list)

    return result

def main():
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False

    result = generate_ascii_lists(x, strings, flag)
    print(result)

if __name__ == "__main__":
    main()

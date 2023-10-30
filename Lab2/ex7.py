def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]


def find_palindromes(numbers):
    palindromes = [num for num in numbers if is_palindrome(num)]

    if palindromes:
        max_palindrome = max(palindromes)
        return len(palindromes), max_palindrome
    else:
        return 0, None

def main():
    number_list = [121, 123, 1331, 454, 78987]
    x = find_palindromes(number_list)
    print(x)


if __name__ == "__main__":
    main()

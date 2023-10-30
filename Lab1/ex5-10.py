#ex 5
def spiral_traversal(matrix):
    m = len(matrix)
    n = len(matrix[0])
    k = 0
    l = 0

    while (k < m and l < n):
        #top row
        for i in range(l, n):
            print(matrix[k][i], end=" ")

        k += 1

        #rightmost column
        for i in range(k, m):
            print(matrix[i][n - 1], end=" ")

        n -= 1

        if (k < m):
            #bottom row
            for i in range(n - 1, (l - 1), -1):
                print(matrix[m - 1][i], end=" ")

            m -= 1

        if (l < n):
            #leftmost column
            for i in range(m - 1, k - 1, -1):
                print(matrix[i][l], end=" ")

            l += 1

matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

spiral_traversal(matrix)

#ex6
def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

#ex7
def extract_first_number(text):
    num_str = ""
    found_digit = False

    for char in text:
        if char.isdigit():
            num_str += char
            found_digit = True
        elif found_digit:
            break

    if num_str:
        return int(num_str)
    else:
        return None


text1 = "An apple is 123 USD"
print(extract_first_number(text1))

#ex8
def count_ones_bits(number):
    # convert nr binary and remove the '0b'
    binary_str = bin(number)[2:]
    count = 0

    for digit in binary_str:
        if digit == '1':
            count += 1
    return count

#print(count_ones_bits(24))

#ex9
def most_common_(s):
    s1 = ''.join(char.lower() for char in s if char.isalpha())

    if not s1:
        return None

    letter_counts = {}
    for char in s1:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    most_common = max(letter_counts, key=letter_counts.get)
    count = letter_counts[most_common]

    return most_common, count

#print(most_common_("an apple is not a tomato"))

#ex10
def nr_words(text):

    count = 0
    words = text.split(" ")
    for word in words:
        if word:
            count += 1
    return count

#print(nr_words("I have Python exam"))
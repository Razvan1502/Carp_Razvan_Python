def count_characters(text):
    count = {}

    for char in text:
        count[char] = count.get(char, 0) + 1
        # if char in count:
        #     count[char] += 1
        # else:
        #     count[char] = 1

    return count


def main():
   print(count_characters("Ana has apples."))


if __name__ == "__main__":
    main()
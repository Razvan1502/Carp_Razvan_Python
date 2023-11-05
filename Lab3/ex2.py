def count_characters(text):
    count = {}

    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count


def main():
   print(count_characters("Ana has apples."))


if __name__ == "__main__":
    main()
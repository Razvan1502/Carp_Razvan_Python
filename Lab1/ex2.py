def count_vowels(input_str):
    vowels = set("AEIOUaeiou")
    count = 0

    for char in input_str:
        if char in vowels:
            count += 1

    return count

def main():
    iinput = input("string: ")
    print(count_vowels(iinput))

if __name__ == "__main__":
    main()

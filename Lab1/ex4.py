def main():
 upper_camel_case = input("string: ")
 result = ""

 for char in upper_camel_case:
    if char.isupper():
        result += "_" + char.lower()
    else:

        result += char

 print(result)

if __name__ == "__main__":
    main()
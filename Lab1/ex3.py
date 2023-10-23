
def main():

 s1 = input("s1: ")
 s2 = input("s2: ")
 occurrences = 0

 for i in range(len(s2) - len(s1) + 1):
    if s2[i:i + len(s1)] == s1:
        occurrences += 1

 print(occurrences)


if __name__ == "__main__":
    main()
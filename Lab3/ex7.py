def set_operations(*args):
    result = {}
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            set1 = args[i]
            set2 = args[j]

            union = f"{set1} | {set2}"
            result[union] = set1.union(set2)

            intersection = f"{set1} & {set2}"
            result[intersection] = set1.intersection(set2)

            diff_a_b = f"{set1} - {set2}"
            result[diff_a_b] = set1.difference(set2)

            diff_b_a = f"{set2} - {set1}"
            result[diff_b_a] = set2.difference(set1)

    for key, value in result.items():
        print(f"{key}: {value}")

def main():
 set1 = {1, 2}
 set2 = {2, 3}

 set_operations(set1, set2)

if __name__ == "__main__":
    main()
def order_tuples(lst):
    sorted_list = sorted(lst, key=lambda x: x[1][2] if len(x[1]) > 2 else '')
    return sorted_list

def main():
    tuple_list = [('abc', 'bcd'), ('abc', 'zza')]
    result = order_tuples(tuple_list)
    print(result)

if __name__ == "__main__":
    main()

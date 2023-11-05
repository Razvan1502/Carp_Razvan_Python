def my_function(*arguments, **keywords):
    return sum([1 for el in arguments if el in keywords.values()])

def main():
 print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))

if __name__ == "__main__":
    main()
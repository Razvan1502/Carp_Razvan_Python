def function(a, b):
    return set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b)-set(a)

def main():
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    print(function(a,b))

if __name__ == "__main__":
    main()

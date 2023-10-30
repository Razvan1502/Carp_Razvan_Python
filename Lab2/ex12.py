def group(lista):
    list = lista[:]
    result = []
    for i in list:
        for j in list:

            if i != j and i[-2:] == j[-2:]:
                result.append([i, j])
                list.remove(i)
                list.remove(j)
                break

    for i in list:
        result.append([i])

    return result

def main():
    print(group(['ana', 'banana', 'carte', 'arme', 'parte']))

if __name__ == "__main__":
    main()
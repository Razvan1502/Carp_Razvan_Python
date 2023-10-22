
def calc_cmmdc(a, b):
    while b:
        r = a%b
        a = b
        b = r
    return a

input = input("introduceti numerele: ")
numbers = [int(num) for num in input.split()]

if len(numbers) < 2:
    print("nu sunt suficiente numere")
else:
    cmmdc = numbers[0]
    for n in numbers[1:]:
        cmmdc = calc_cmmdc(cmmdc, n)

    print(f"cmmdc-ul {numbers} este {cmmdc}")



input = input("string: ")

vowels = set("AEIOUaeiou")
count = 0

for char in input:
    if char in vowels:
        count += 1
print(count)

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False

        value = dictionary[key]
        if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value[1:-1]:
            return False

    return True

def main():
 rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
 data = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

 result = validate_dict(rules, data)
 print(result)

if __name__ == "__main__":
    main()
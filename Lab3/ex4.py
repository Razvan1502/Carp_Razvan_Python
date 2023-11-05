def build_xml_element(tag, content, **param):
    attributes = ' '.join([f'{key}="{value}"' for key, value in param.items()])
    element = f"<{tag} {attributes}>{content}</{tag}>"
    return element
def main():
 result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
 print(result)

if __name__ == "__main__":
    main()
class LibraryItem:
    def __init__(self, title, author_or_director, item_id):
        self.title = title
        self.author_or_director = author_or_director
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Item ID: {self.item_id}\nTitle: {self.title}\nAuthor/Director: {self.author_or_director}\n"
              f"Status: {'Checked Out' if self.checked_out else 'Available'}")

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Type: Book\nNumber of Pages: {self.num_pages}")

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Type: DVD\nDuration: {self.duration} minutes")

class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Type: Magazine\nIssue Number: {self.issue_number}")

# Example usage
book = Book(title="Moara cu noroc", author="Ioan Slavici", item_id="123", num_pages=100)
dvd = DVD(title="Inception", director="Christopher Nolan", item_id="456", duration=150)
magazine = Magazine(title="National Geographic", publisher="National Geographic Society", item_id="789", issue_number=245)

book.display_info()
book.check_out()
book.return_item()
print()

dvd.display_info()
dvd.check_out()
dvd.check_out()
dvd.return_item()
print()

magazine.display_info()
magazine.check_out()
magazine.return_item()
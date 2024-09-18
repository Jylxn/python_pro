
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Member: {self.name}, ID: {self.membership_id}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def register_member(self, member):
        self.members.append(member)

    def deregister_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def borrow_book(self, member, book):
        if book in self.books:
            member.borrow_book(book)
            self.books.remove(book)

    def return_book(self, member, book):
        member.return_book(book)
        self.books.append(book)

    def display_books(self):
        return [str(book) for book in self.books]

    def display_members(self):
        return [str(member) for member in self.members]



def main():
    
    library = Library()


    book1 = Book("Wolf Hall", "Hilary Mantel", "12345")
    book2 = Book("Sapiens", "Yuval Noah Harari", "54321")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "67890")    

    

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    
    member1 = Member("Lax", "M001")
    member2 = Member("Jay", "M002")
    member3 = Member("Lee", "K010")

    
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)

    
    print("\nBooks in Library:")
    for book in library.display_books():
        print(book)

    
    print("\nMembers in Library:")
    for member in library.display_members():
        print(member)

    
    print("\nLax borrows 'Wolf Hall':")
    library.borrow_book(member1, book1)
    print("Books in Library after borrowing:")
    for book in library.display_books():
        print(book)

    print("\nJay borrows 'Sapiens':")
    library.borrow_book(member2, book2)
    print("Books in Library after borrowing:")
    for book in library.display_books():
        print(book)

    
    print("\nLee borrows 'To Kill a Mockingbird':")
    library.borrow_book(member3, book3)
    print("Books in Library after borrowing:")
    for book in library.display_books():
        print(book)

    
    print("\nLax returns 'Wolf Hall':")
    library.return_book(member1, book1)
    print("Books in Library after returning:")
    for book in library.display_books():
        print(book)

    
    print("\nJay returns 'Sapiens':")
    library.return_book(member2, book2)
    print("Books in Library after returning:")
    for book in library.display_books():
        print(book)


if __name__ == "__main__":
    main()
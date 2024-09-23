class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []
        self.admins = []  

    def add_admin(self, admin_id):
        self.admins.append(admin_id)

    def is_admin(self, member_id):
        return member_id in self.admins

    def add_book(self, admin_id, book_id, book_name, author, isbn, genre, stock):
        if self.is_admin(admin_id):
            self.books[book_id] = {
                'name': book_name,
                'author': author,
                'isbn': isbn,
                'genre': genre,
                'stock': stock
            }
            print(f'Book "{book_name}" added successfully!')
        else:
            print(f'Member "{self.members[admin_id]["name"]}" is not authorized to add books.')

    def remove_book(self, admin_id, book_id):
        if self.is_admin(admin_id):
            if book_id in self.books:
                removed_book = self.books.pop(book_id)
                print(f'Book "{removed_book["name"]}" removed successfully!')
            else:
                print(f'Book ID {book_id} not found.')
        else:
            print(f'Member "{self.members[admin_id]["name"]}" is not authorized to remove books.')

    def add_member(self, admin_id, member_id, name, phone, email):
        if self.is_admin(admin_id):
            self.members[member_id] = {
                'name': name,
                'phone': phone,
                'email': email
            }
            print(f'Member "{name}" added successfully!')
        else:
            print(f'Member "{self.members[admin_id]["name"]}" is not authorized to add new members.')

    def borrow_book(self, admin_id, member_id, book_id):
        if self.is_admin(admin_id):
            if book_id in self.books and member_id in self.members:
                if self.books[book_id]['stock'] > 0:
                    self.books[book_id]['stock'] -= 1
                    self.loans.append({
                        'member_id': member_id,
                        'book_id': book_id,
                        'borrow_date': 'Today',
                        'return_date': 'Next Week'
                    })
                    print(f'Book "{self.books[book_id]["name"]}" borrowed by {self.members[member_id]["name"]}.')
                else:
                    print("This book is currently out of stock.")
            else:
                print("Invalid member or book ID.")
        else:
            print(f'Member "{self.members[admin_id]["name"]}" is not authorized to borrow books.')

    def display_books(self, category=None):
        print("Available Books:")
        for book_id, details in self.books.items():
            if category is None or details['genre'] == category:
                print(f'ID: {book_id}, Name: {details["name"]}, Author: {details["author"]}, Genre: {details["genre"]}, Stock: {details["stock"]}')

    def display_members(self):
        print("Library Members:")
        for member_id, details in self.members.items():
            print(f'ID: {member_id}, Name: {details["name"]}, Phone: {details["phone"]}, Email: {details["email"]}')

library = Library()

library.add_admin(1)  

library.add_member(1, 2, "Ayşe Kaya", "05333333333", "ayse@example.com")

library.add_book(1, 101, "Chess", "Stefan Zweig", "123456", "Novel", 3)

library.display_books()

library.display_members()

library.borrow_book(1, 2, 101)

library.add_book(2, 102, "War and Peace", "Tolstoy", "654321", "History", 2)

library.remove_book(2, 101)

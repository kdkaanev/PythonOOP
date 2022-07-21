class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = dict({})

    def get_book(self, author, book_name, days_to_return, user):
        if book_name in self.rented_books[user.username]:
            pass

    def return_book(self, author, book_name, user):
        pass

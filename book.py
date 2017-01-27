# create your simple Book class in this file
"""
    class for Book (in book.py). This is a simple class with the required attributes for a book and
    four methods: __init__  Special method for initialization and
    1. Displaying book details in the status bar
    2. Mark the book as completed
    3. Determine if the book is long
"""

class Book:
    def __init__(self, title='', author='', pages=0, status = ''):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __str__(self):
        return ('{} by {}, {} pages'.format(self.title, self.author, self.pages))

    def mark_completed(self):
        self.status = 'c'

    def is_long_book(self):
        if self.pages >= 500:
            True
        False





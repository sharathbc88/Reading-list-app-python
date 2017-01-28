# create your simple Book class in this file
"""
    class for Book (in book.py). This is a simple class with the required attributes for a book and
    four methods: __init__  Special method for initialization and
    1. Displaying book details in the status bar
    2. Mark the book as completed
    3. Determine if the book is long
"""

class Book:
    """
        class with the required attributes for a book
    """

    def __init__(self, title='', author='', pages=0, status = ''):
        """
            Initializing the Book class
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __str__(self):
        """
             String method for the Book class, diaplays the book details
             :return: string statement
        """
        return ('{} by {}, {} pages'.format(self.title, self.author, self.pages))

    def mark_completed(self):
        """
             when a title widget is clicked, then it is marked completed
             :return: None
        """
        self.status = 'c'

    def is_long_book(self):
        """
            to color code the widget, length of the page is calculated
            :return: None
        """
        if self.pages >= 500:
            True
        False





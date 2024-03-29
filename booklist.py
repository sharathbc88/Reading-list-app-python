

"""
    class for BookList (in booklist.py). It contain a single attribute, a list of Book objects, and
    __init__  Special method for initialization
    1. get book by title
    2. add book
    3. get total pages for required books
    4. get total pages for completed books
    5. load books
    6. save books
    7. sort

"""

from book import Book
import operator

class BookList:
    """
        class for BookList (in booklist.py). It contain a single attribute, a list of Book objects
    """

    def __init__(self, books =[]):
        """
            Initializing the Booklist class
        """
        self.books = books

    def get_book_title(self, title=''):
        """
            If the input title matches the book object then return the book
            :param: title of the Book object
            :return: book object
        """
        for book in self.books:
            if book.title == title:
                return book

    def add_book(self,newBook):
        """
           If the input title matches the book object then return the book
           :param: Newbook object
           :return: None
        """
        self.books[0].append(newBook) #to break nested list

    def required_total_pages(self):
        """
            calculates the total pages to read
            :return: total pages to read
        """
        required_total_pages = 0
        for book in self.books:
            if book.status == 'r':
                required_total_pages += int(book.pages)
        return required_total_pages

    def completed_total_pages(self):
        """
            calculates the total pages completed
            :return: total pages completed
        """
        completed_total_pages = 0
        for book in self.books:
            if book.status == 'c':
                completed_total_pages += int(book.pages)
        return completed_total_pages

    def load_csv(self, filename=''):
        """
            reads the csv file
            :param: filename to read
            :return: None
         """
        itemlist = []
        with open(filename, 'r') as f:
            # open file
            for line in f:
                fields = line.rstrip('\n').split(',')
                temp_book = Book()
                itemlist.append([fields[0], fields[1], fields[2], fields[3]])
        import operator
        itemlist = sorted(itemlist, key=operator.itemgetter(1, 2))
        self.books.append(itemlist)

    def save_csv(self, filename='',itemlist=''):
        """
            saves itemlist or objects to csv file
            :param: filename to save
            :param: itemlist to save in the file
            :return: None
        """
        itemlist= itemlist[0]
        try:
            with open(filename, 'w') as f:  # write file
                for i in range(len(itemlist)):
                    line = '{},{},{},{}\n'.format(itemlist[i][0], itemlist[i][1], itemlist[i][2], itemlist[i][3])
                    f.write(line)
        except FileNotFoundError:  # error handling
            print('Error occurred while saving details back to {} file.\n'.format(filename))


    def sort_books(self):
        """
            sorts book object by first author then by pages
            :return: None
        """
        self.books.sort(key=operator.itemgetter(1, 2))

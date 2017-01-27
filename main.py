"""
name: Sharath Basappa Chandranna
date: 1/26/2017
brief program details: This program is a simple reading list that allows a user to track books they wish to read and books
                        they have completed reading. The program maintains a list of books in a file, and each book has:
                        •	title, author, number of pages, whether it is required or completed (r or c)
                        Users can choose to see the list of required books or completed books, including a total of the number
                         of pages of the book list. The lists will be sorted by author then by number of pages (increasing).
                        Users can add new books and mark books as completed.
                        They cannot change books from completed to required.
link to my project on GitHub: https://github.com/sharathbc88/Assignment2
"""


#import Libraries and files
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from booklist import Booklist
from book import Book


""" name of the CSV file stored in a constant """
FILENAME = 'books.csv'

class ReadingList(App):
    """
        Kivy app uses reading list Class to run, String property is used to display messages on top and bottom
        of the screen.
    """
    bottom_status_text = StringProperty()
    top_status_text = StringProperty()


    # Initializing the class
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.book_list = Booklist()
        self.book_list.load_csv(FILENAME)

    def build(self):
        """
        Builds Kivy Graphical User Interface
        :return: reference to the root Kivy widget
        """
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('trail.kv')
        self.required_books()
        return self.root

    def required_books(self):
        """
                Reads the required book and pass it to buttons method
                Status widget gets the string message
                :return: None
        """
        self.bottom_status_text = 'Click books to mark them as completed'
        x = self.book_list.books[0] # import from booklist caused nested lists, hence broken down
        temp = []
        total = 0
        for i in range(len(x)):
            if 'r' in x[i][3]:
                temp.append(x[i])
                total = total + int(x[i][2])
        self.itemlist = temp
        self.top_status_text = ('Total pages to read: {}'.format(total))
        self.required_entry_buttons()

    def required_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """

        self.root.ids.entriesBox.clear_widgets()
        for status in self.itemlist:
            # create a button for each book entry
            temp_button = Button(text=str(status[0]))
            if int(status[2]) > 500:
                temp_button.background_color = .65,.5,1,1
            else:
                temp_button.background_color = .65,1,1,1
            temp_button.bind(on_release=self.remove_buttons)
            temp_button.bind(on_release=self.mark_item)
            self.root.ids.entriesBox.add_widget(temp_button)

    def completed_books(self):
        """
             Reads the required book and pass it to buttons method
             Status widget gets the string message
        """
        x = self.book_list.books[0]  # import from booklist caused nested lists, hence broken down
        temp = []
        total = 0
        for i in range(len(x)):
            if 'c' in x[i][3]:
                temp.append(x[i])
                total = total + int(x[i][2])
        self.itemlist = temp
        self.top_status_text = ('Total pages completed: {}'.format(total))
        self.completed_entry_buttons()


    def completed_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        self.root.ids.entriesBox.clear_widgets()
        for each in self.itemlist:

            # create a button for each book entry
            temp_button = Button(text=str(each[0]))
            temp_button.bind(on_release=self.item_details)
            self.bottom_status_text = ''
            self.root.ids.entriesBox.add_widget(temp_button)

    def add_item(self,bookTitle, bookAuthor, bookPages):
        """
                Add new Book method checks the requirement and saves it
                :param bookTitle: Takes title text
                :param bookAuthor: Takes author text
                :param bookPages: Takes pages text
                :return: None
        """
        try:
            if str(bookTitle) == '' or str(bookAuthor) == '' or (bookPages) == '':
                self.bottom_status_text = 'All fields must be completed'
            elif bookPages.isalpha():
                self.bottom_status_text = 'Please enter a valid number'
            elif int(bookPages) <0:
                self.bottom_status_text = 'Number must be >= 0'
            else:
                new_Item = [bookTitle, bookAuthor, int(bookPages), 'r']
                self.book_list.add_book(new_Item)
                itemlist = self.book_list.books
                self.book_list.save_csv(FILENAME, itemlist)
                self.required_books()
                self.clear_text()
        except ValueError:
            self.bottom_status_text = ' Enter a Valid Number'


    def clear_text(self):
        """
            clears text in the input text field
            :return: None
        """
        self.root.ids.inputTitle.text = ''
        self.root.ids.inputAuthor.text = ''
        self.root.ids.inputPages.text = ''


    def item_details(self, instance):
        """
            for completed list, Total pages is calculated
            :return: None
        """
        title = instance.text
        x = self.book_list.books[0]  # import from booklist caused nested lists, hence broken down
        for i in range(len(x)):
            if title in x[i][0]:
                self.bottom_status_text = ('{} by {}, {}pages(completed)'.format(x[i][0],x[i][1], x[i][2]))



    def mark_item(self, instance):
        """
            clear text in the input text field
            :return: None
        """
        title = instance.text
        x = self.book_list.books[0]  # import from booklist caused nested lists, hence broken down
        for i in range(len(x)):
            if title in x[i][0]:
                x[i][3] = 'c'
        self.book_list.save_csv(FILENAME, self.book_list.books)
        self.required_books()


    def remove_buttons(self, instance):
        """
            Removes Widgets from the required list
            :return: None
        """
        self.root.ids.entriesBox.remove_widget(widget=instance)

ReadingList().run()
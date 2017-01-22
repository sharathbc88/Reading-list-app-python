"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from book import Book
from booklist import Booklist
BOOK_FILE = 'books.csv'
import string
# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    top_status_text = StringProperty()
    bottom_status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.book_list = Booklist
        self.book_list.load_books(BOOK_FILE)

    def on_start(self):
        print('on start is called')

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        self.press_List_Required()
        return self.root


    def create_entry_buttons(self):
        for name in self.itemlist:
            # create a button for each phonebook entry
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_List_Required(self):
       for book in self.book_list.books:
           if book.status == 'required':
               temp_button = Button(text=Book.title)
               temp_button.bind(on_release=self.handle_required_entry)
               self.root.ids.entriesBox.add_widget(temp_button)

    def press_list_completed(self):
        for book in self.book_list.books:
            if book.status == 'c':
                temp_button = Button(text=Book.title)
                temp_button.bind(on_release=self.handle_completed_entry)
                self.root.ids.entriesBox.add_widget(temp_button)

    def handle_required_entry(self, instance):
        title = instance.text
        marked_book = self.book_list.get_book(title)
        marked_book.mark_completed()
        self.book_list.save_books('books.csv')

        self.root.ids.entriesBox.remove_widget(widget=instance)

    def handle_completed_entry(self,instance):
        title= instance.text
        complete_string = 'completed'
        selected_book = self.book_list.get_book(title)


    def clear_fields(self):
        self.root.ids.addedTitle.text = ''
        self.root.ids.addedAuthor.text = ''
        self.root.ids.addedpages = ''

    def press_add_item(self, added_title,added_author,added_pages):
        try:
            not_letter_count = 0
            for i in str(added_author):
                if i not in string.ascii_letters and i != '':
                    not_letter_count += 1
            if added_title == '' or added_author == '' or added_pages == '':
                self.bottom_status = 'Author name should contain letter only'
            elif not_letter_count >0:
                self.bottom_status_text = 'Author name should contain letter only'
            elif int(added_pages) <0:
                self.bottom_status_text = 'number of pages must be >= 0'
            else:
                new_book = Book(added_title, added_author, added_pages, 'r')
                self.book_list.save_books('books.csv')
                self.press_List_Required()
                self.clear_fields()
        except ValueError:
            self.bottom_status_text = ' please enter a valid number'

    def on_stop(self):
        print('calling on stop')
        self.book_list.save_books('books.csv')

    def handle_calculate(self):
        pass


ReadingListApp().run()
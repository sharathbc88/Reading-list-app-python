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

# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(object).__init__(**kwargs)
        self.itemlist = Booklist
        self.book_list.load_books('books.csv')

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root


    def create_entry_buttons(self):
        for name in self.itemlist:
            # create a button for each phonebook entry
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

    def pressListRequired (self):
       for item in self.itemlist.book:
           if book.status == 'required'


    def handle_calculate(self):
        pass

ReadingListApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from booklist import Booklist
from kivy.uix.togglebutton import ToggleButton
from book import Book

FILENAME = 'books.csv'
class PhonebookApp(App):
    bottom_status_text = StringProperty()
    itemlist = []
    filename = "books.csv"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.book_list = Booklist()
        self.book_list.load_csv(FILENAME)

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('trail.kv')
        self.required_books()
        return self.root

    def required_books(self):
        x = self.book_list.books[0] # import from booklist caused nested lists, hence broken down
        temp = []
        for i in range(len(x)):
            if 'r' in x[i][3]:
                temp.append(x[i])
        self.itemlist = temp
        print(self.itemlist)
        self.create_entry_buttons()

    def add_item(self,bookTitle, bookAuthor, bookPages):
        try:

            if str(bookTitle) == '' or str(bookAuthor) == '' or int(bookPages) == '':
                self.bottom_status_text = 'All fields must be completed'
            elif bookPages.isalpha():
                self.bottom_status_text = 'Please enter a valid number'
            elif int(bookPages) <0:
                self.bottom_status_text = 'Number must be >= 0'
            else:
                new_Item = Book(bookTitle, bookAuthor, int(bookPages), 'r')  # create a Book object
                self.book_list.add_book(new_Item)  # add the Book object to the book_list attribute
                # save book file when a new book is added
                self.book_list.add_book('books.csv')
                # add button for new entry by clearing the book buttons and update
                self.press_list_required()
        except:
            pass


    def completed_books(self):
        #self.load_csv()
        x = self.book_list.books[0]  # import from booklist caused nested lists, hence broken down
        temp = []
        for i in range(len(x)):
            if 'c' in x[i][3]:
                temp.append(x[i])
        self.itemlist = temp
        print(self.itemlist)
        self.create_entry_buttons()

    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        self.root.ids.entriesBox.clear_widgets()
        for status in self.itemlist:

            # create a button for each phonebook entry
            temp_button = Button(text=str(status[0]))
            #print(name)
            temp_button.bind(on_release=self.create_entry_buttons)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.phonebook[name])
        # set button state
        # print(instance.state)
        instance.state = 'down'

    def handle_calculate(self):
        pass

PhonebookApp().run()
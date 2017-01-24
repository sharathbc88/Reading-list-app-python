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
    top_status_text = StringProperty()
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

    def add_item(self,bookTitle, bookAuthor, bookPages):
        print(bookPages,bookTitle,bookAuthor)
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
        except:
            pass

    def clear_text(self):
        self.root.ids.inputTitle.text = ''
        self.root.ids.inputAuthor.text = ''
        self.root.ids.inputPages.text = ''



    def completed_books(self):

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



    def required_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        self.root.ids.entriesBox.clear_widgets()
        for status in self.itemlist:

            # create a button for each phonebook entry
            temp_button = Button(text=str(status[0]))

            if int(status[2]) > 500:
                temp_button.background_color = .4,1,1,1
            else:
                temp_button.background_color = .8,1,1,1
            temp_button.bind(on_release=self.remove_buttons)
            temp_button.bind(on_release=self.mark_item)
            self.root.ids.entriesBox.add_widget(temp_button)

    def completed_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        self.root.ids.entriesBox.clear_widgets()
        for status in self.itemlist:

            # create a button for each phonebook entry
            temp_button = Button(text=str(status[0]))
            temp_button.bind(on_release=self.item_details)

            self.bottom_status_text = ''
            self.root.ids.entriesBox.add_widget(temp_button)

    def item_details(self, instance):
        title = instance.text
        x = self.book_list.books[0]  # import from booklist caused nested lists, hence broken down
        for i in range(len(x)):
            if title in x[i][0]:
                self.bottom_status_text = ('{} by {}, {}pages(completed)'.format(x[i][0],x[i][1], x[i][2]))

    def remove_buttons(self, instance):
        self.root.ids.entriesBox.remove_widget(widget=instance)



    def mark_item(self, instance):
        title = instance.text
        x = self.book_list.books[0]  # import from booklist caused nested lists, hence broken down
        for i in range(len(x)):
            if title in x[i][0]:
                x[i][3] = 'c'
        self.book_list.save_csv(FILENAME, self.book_list.books)
        self.required_books()

    def handle_calculate(self):
        pass

PhonebookApp().run()
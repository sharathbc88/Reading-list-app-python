from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from booklist import Booklist
from book import Book

FILENAME = 'books.csv'
class PhonebookApp(App):
    status_text = StringProperty()
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


    def completed_books(self):
        #self.load_csv()
        temp = []
        for i in range(len(self.book_list.books)):
            if 'c' in self.book_list.books[i][3]:
                temp.append(self.book_list.books[i])
        self.itemlist = temp

    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        for name in self.itemlist:

            # create a button for each phonebook entry
            temp_button = Button(text=str(name[0]))
            #print(name)
            #temp_button.bind(on_release=self.press_entry)
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
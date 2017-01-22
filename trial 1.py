from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class PhonebookApp(App):
    status_text = StringProperty()
    itemlist = []
    filename = "books.csv"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.completed_books()

    def load_csv(self):
        with open(self.filename, 'r') as f:
            # open file
            for line in f:
                fields = line.rstrip('\n').split(',')
                self.itemlist.append([fields[0], fields[1], fields[2], fields[3]])
        import operator
        self.itemlist = sorted(self.itemlist, key=operator.itemgetter(1, 2))

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('trail.kv')
        self.create_entry_buttons()
        return self.root

    def required_books(self):
        self.load_csv()
        temp = []
        for i in range(len(self.itemlist)):
            if 'r' in self.itemlist[i][3]:
                temp.append(self.itemlist[i])
        self.itemlist = temp

    def completed_books(self):
        self.load_csv()
        temp = []
        for i in range(len(self.itemlist)):
            if 'c' in self.itemlist[i][3]:
                temp.append(self.itemlist[i])
        self.itemlist = temp




    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        for name in self.itemlist:
            # create a button for each phonebook entry
            temp_button = Button(text=str(name[0]))
            temp_button.bind(on_release=self.press_entry)
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
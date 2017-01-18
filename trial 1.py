from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class PhonebookApp(App):
    """
    Main program - Kivy app to demo phonebook system
    """
    status_text = StringProperty()
    itemlist = []
    filename = "books.csv"
    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super(PhonebookApp, self).__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        with open(self.filename, 'r') as f:  # open file
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
        self.root = Builder.load_file('trail1.kv')
        self.create_entry_buttons()
        return self.root

    def required_books(self, phonebook):
        print("Required books:")
        total = 0
        count = 0
        # store item list to a varaible

        # Display requiredbooks
        for i in range(len(phonebook)):
            if 'r' in phonebook[i][3]:
                record = ' {}. {} by {} {} pages'.format(i, (phonebook[i][0]).ljust(40), (phonebook[i][1]).ljust(20),
                                                         phonebook[i][2])
                print(record)
                total = total + int(phonebook[i][2])
                count = count + 1
        return self.itemlist


    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        for name in self.itemlist[1]:
            # create a button for each phonebook entry
            temp_button = Button(text=name)
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
        self.status_text = "{}'s number is {}".format(name, self.itemlist[name])
        # set button state
        # print(instance.state)
        instance.state = 'down'

PhonebookApp().run()
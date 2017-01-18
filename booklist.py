# create your BookList class in this file
import csv
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class booklist(App):
    itemlist = []
    filename = "books.csv"
    def __init__(self):
        pass

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons()
        return self.root

    def book(self):
        try:
            with open(self.filename, 'r') as f:  # open file
                for line in f:
                    fields = line.rstrip('\n').split(',')
                    self.itemlist.append([fields[0], fields[1], fields[2], fields[3]])
        except FileNotFoundError:  # error handling
            print('Missing {} file, or missmatching file format.'.format(self.filename))
        import operator
        self.itemlist = sorted(self.itemlist, key=operator.itemgetter(1, 2))
        return self.itemlist

    # display R - List required books
    def handle_calculate(self):
        pass

    def required_books(self,itemlist):
        print("Required books:")
        total = 0
        count = 0
        # store item list to a varaible

        # Display requiredbooks
        for i in range(len(itemlist)):
            if 'r' in itemlist[i][3]:
                record = ' {}. {} by {} {} pages'.format(i, (itemlist[i][0]).ljust(40), (itemlist[i][1]).ljust(20),
                                                         itemlist[i][2])
                print(record)
                total = total + int(itemlist[i][2])
                count = count + 1

        if count > 0:
            # if there is atleast 1 required book, then print
            print("Total pages for {} books: {}".format(count, total))
        else:
            # if there is no required books in the itemlist
            print("No books")

data = booklist()
c = data.book()
print(c)

data.run()



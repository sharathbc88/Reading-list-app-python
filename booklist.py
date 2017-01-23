# create your BookList class in this file
import csv
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from book import Book
from operator import attrgetter

class Booklist:

    def __init__(self, books =[]):
        self.books = books

    def load_csv(self, filename=''):
        itemlist = []
        with open(filename, 'r') as f:
            # open file
            for line in f:
                fields = line.rstrip('\n').split(',')
                itemlist.append([fields[0], fields[1], fields[2], fields[3]])
                print(itemlist)
        import operator
        itemlist = sorted(itemlist, key=operator.itemgetter(1, 2))
        print(itemlist)
        self.books.append(itemlist)

    def add_book(self,newBook):
        #self.books= (self.books[0]) #to break nested list
        self.books[0].append(newBook)

    def save_csv(self, filename='',itemlist=''):
        print(itemlist)

        try:
            with open(filename, 'w') as f:  # write file
                for i in range(len(itemlist)):
                    line = '{},{},{},{}\n'.format(itemlist[i][0], itemlist[i][1], itemlist[i][2], itemlist[i][3])
                    f.write(line)
        except FileNotFoundError:  # error handling
            print('Error occurred while saving details back to {} file.\n'.format(filename))




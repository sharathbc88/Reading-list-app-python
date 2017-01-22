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
        self.books.append(newBook)

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

    def add_book(self,book= Book()):
        self.books.append(book)
        self.sort_books()


    def load_books(self, file_name=''):
        file_pointer = open(file_name, 'r')
        for index, data in enumerate(file_pointer.readlines()):
            datum= data.strip().split(',')
            self.books.append(Book(datum[0],datum[1],int[datum[2]],datum[3]))
        file_pointer.close()

    def get_book(self,title=''):
        for book in self.books:
            if book.title == title:
                return book

    def get_total_pages(self,status):
        total_pages = 0
        for book in self.books:
            if book.status == status:
                total_pages +=int(book.pages)
        return total_pages


    def build(self):
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons()
        return self.root





    def handle_calculate(self):
        pass







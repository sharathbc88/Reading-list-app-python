# create your simple Book class in this file
from kivy.app import App


import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button

class Book:
    def __init__(self, title='', author='', pages=0, status = ''):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __str__(self):
        return 'to be decided'

    def mark_completed(self):
        self.status = 'completed'

    def is_long_book(self):
        if self.pages >= 500:
            return True
        else:
            return False





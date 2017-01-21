# create your simple Book class in this file
from kivy.app import App


import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return '{} by {}, {} pages'.format(self.title, self.author, self.pages)







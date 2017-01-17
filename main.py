"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root

    def handle_calculate(self):
        pass

ReadingListApp().run()

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("screen.kv")

class MeuApp(App):
    def build(self):
        return GUI

    def on_start(self):
        """self.root.ids"""

MeuApp().run()
import kivy
from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

class Tile (ToggleButtonBehavior, Image):

    def __init__(self):
        super().__init__()
        self.source='MINESWEEPER_0.png'
        self.allow_stretch=True
        self.keep_ratio=False

    def on_state(self, widget, value):
        if value=='down' and self.source=='MINESWEEPER_0.png':
            self.source = 'MINESWEEPER_X.png'
        elif value=='down' and self.source=='MINESWEEPER_F.png':
            self.source = 'MINESWEEPER_X.png'
        else:
            self.source = 'MINESWEEPER_F.png'

class MyApp(App):
    def build(self):
        layout = GridLayout(rows=8)
        for a in range (64):
            layout.add_widget(Tile())
        return layout


if __name__ == '__main__':
    MyApp().run()
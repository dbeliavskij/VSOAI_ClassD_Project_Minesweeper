import kivy
from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout


flagmode = False

def changemode():

    global flagmode

    flagmode=not flagmode

class Tile (ToggleButtonBehavior, Image):

    def __init__(self):
        super().__init__()
        self.source='MINESWEEPER_X.png'
        self.allow_stretch=True
        self.keep_ratio=False
        
    def on_state(self, widget, value):
        if self.source=='MINESWEEPER_X.png' and flagmode==True:
            self.source = 'MINESWEEPER_F.png'
        elif self.source=='MINESWEEPER_F.png':
            self.source = 'MINESWEEPER_X.png'
        elif self.source=='MINESWEEPER_X.png' and flagmode==False:
            self.source = 'MINESWEEPER_0.png'

class StateButton (ToggleButtonBehavior, Image):

    def __init__(self):
        super().__init__()
        self.source = 'MINESWEEPER_0.png'
        self.allow_stretch = True
        self.size = (90, 50)
        self.size_hint = (None, None)
        self.pos_hint = {'center_y':0.5}
        
    
    def on_state (self, widget, value):
        if value=='down':
            self.source = 'MINESWEEPER_F.png'
            changemode()
        else:
            changemode()
            self.source = 'MINESWEEPER_0.png' 


class MinesweeperApp(App):

    icon='Minesweeper_icon.png'

    def build(self):

        layout = BoxLayout(orientation='horizontal', spacing = 10)

        playfield = GridLayout(rows=8, size_hint=(0.8, 1))
        for a in range (64):
            playfield.add_widget(Tile())
        
        btmode = StateButton()
        layout.add_widget(playfield)
        layout.add_widget(btmode)

        return layout


if __name__ == '__main__':
    MinesweeperApp().run()
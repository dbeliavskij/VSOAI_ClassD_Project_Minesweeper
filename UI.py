from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import DictProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import config
from field_gen import check_tile

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '500')
Config.write()

Window.clearcolor = (0.66, 0.87, 0.96, 1)

flagmode = False

sm = ScreenManager()


class Restart(Button):
    def on_press(self):
        sm.current = 'menu'


class Win(Widget):
    def __init__(self):
        self.layout = BoxLayout(orientation='vertical', padding=70, spacing=20)
        self.title = Label(text = 'You won! Congratulations!')
        self.exit = (Button(text='Exit', size_hint=(None, None), width=200, height=50, pos_hint={'center_x': 0.5}))
        ## NEVEIKIA BIND EXIT 
        #self.exit.bind(on_press = App.get_running_app().stop())
        self.layout.add_widget(self.exit)
        self.pop = Popup(content=self.layout, title='CONGRATULATIONS!', separator_height=0, size_hint=(None, None), size=(400, 400), 
                         auto_dismiss=False, background='win.jpg') #WIN nuotrauka reikia pakeisti :D
        
    def show(self):
        self.pop.open()

class Gameover(Widget):
    def __init__(self):
        self.layout = BoxLayout(orientation='vertical', padding=70, spacing=20)

        self.restart = (Restart(text='Play again!', size_hint=(None, None), width=200, height=50, pos_hint={'center_x': 0.5}))
        self.layout.add_widget(self.restart)

        self.menu = (Button(text='Menu', size_hint=(None, None), width=200, height=50, pos_hint={'center_x': 0.5}))
        self.layout.add_widget(self.menu)

        self.exit = (Button(text='Exit', size_hint=(None, None), width=200, height=50, pos_hint={'center_x': 0.5}))
        self.layout.add_widget(self.exit)

        self.pop = Popup(content=self.layout, title='', separator_height=0, size_hint=(None, None), size=(400, 400), 
                         auto_dismiss=False, background='MINESWEEPER_-1.png')
        
        self.restart.bind(on_press=self.pop.dismiss)

    def show(self):
        self.pop.open()


def changemode():
    global flagmode
    flagmode = not flagmode


class Tile (ToggleButtonBehavior, Image):

    coord = DictProperty({'x': 0, 'y': 0})

    def __init__(self, cols=0, rows=0):
        super().__init__()
        self.source = 'MINESWEEPER_X.png'
        self.allow_stretch = True
        self.keep_ratio = False
        self.coord['x'] = cols
        self.coord['y'] = rows

    def on_state(self, widget, value):
        if self.source == 'MINESWEEPER_X.png' and flagmode:
            self.source = 'MINESWEEPER_F.png'
            print(self.coord)
        elif self.source == 'MINESWEEPER_F.png':
            self.source = 'MINESWEEPER_X.png'
            print(self.coord)
        elif self.source == 'MINESWEEPER_X.png' and not flagmode:
            self.source = 'MINESWEEPER_' + str(check_tile(self.coord, config.field)) + '.png'
            print(self.coord)
            
            if check_tile(self.coord, config.field) == -1 and not flagmode:
                print('you lose')
                Gameover.show(Gameover())
            else:
                config.tiles_opened = config.tiles_opened + 1
                print(config.tiles_opened)
            if config.tiles_opened == ((config.size ** 2) - config.bomb_amount):
                print('You WIN!')
                Win.show(Win())


class StateButton (ToggleButtonBehavior, Image):
    def __init__(self):
        super().__init__()
        self.source = 'MINESWEEPER_0.png'
        self.allow_stretch = True
        self.size = (90, 50)
        self.size_hint = (None, None)
        self.pos_hint = {'center_y': 0.5}

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'MINESWEEPER_F.png'
            changemode()
        else:
            changemode()
            self.source = 'MINESWEEPER_0.png'


layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)
playfield = GridLayout(rows=config.size, size_hint=(0.8, 1))
for cols in range(config.size):
    for rows in range(config.size):
        playfield.add_widget(Tile(rows, cols))
btmode = StateButton()
layout.add_widget(playfield)
layout.add_widget(btmode)
gamefield = Screen()
gamefield.add_widget(layout)

menu = Screen(name='menu')


class MinesweeperApp(App):
    icon = 'Minesweeper_icon.png'
    
    def build(self):
        sm.add_widget(gamefield)
        sm.add_widget(menu)
        return sm




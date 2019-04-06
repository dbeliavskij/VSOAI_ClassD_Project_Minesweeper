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
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.label import Label
import config
from field_gen import check_tile
from field_gen import field_gen

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '500')
Config.write()

Window.clearcolor = (0.66, 0.87, 0.96, 1)

flagmode = False

sm = ScreenManager(transition=SwapTransition())


class Gamefield(Widget):
    def __init__(self):
        super(Gamefield, self).__init__()
        self.layout = BoxLayout(orientation='horizontal', spacing=10,
                                padding=10)
        self.playfield = GridLayout(rows=config.size, size_hint=(0.8, 1))
        for cols in range(config.size):
            for rows in range(config.size):
                self.playfield.add_widget(Tile(rows, cols))
        self.btmode = StateButton()
        self.layout.add_widget(self.playfield)
        self.layout.add_widget(self.btmode)


gamefield = Screen(name='gamefield')


class Play(Button):
    def __init__(self):
        super(Play, self).__init__()
        self.text = "Play the game!"
        self.size_hint = (None, None)
        self.width = 200
        self.height = 50
        self.pos_hint = {'center_x': 0.5}

    def on_press(self):
        if config.level == 3:
            config.bomb_amount = int(config.size**2*0.5)
        elif config.level == 2:
            config.bomb_amount = int(config.size**2*0.3)
        else:
            config.bomb_amount = int(config.size**2*0.15)
        config.field = field_gen(config.size)
        gamefield.add_widget(Gamefield().layout)
        config.tiles_opened = 0
        sm.current = 'gamefield'


class Difficulty(Button):
    def __init__(self):
        super(Difficulty, self).__init__()
        self.text = 'Difficulty: Easy'
        self.size_hint = (None, None)
        self.width = 200
        self.height = 50
        self.pos_hint = {'center_x': 0.5}

    def on_press(self):
        if self.text == 'Easy' or self.text == 'Difficulty: Easy':
            self.text = 'Normal'
            config.level = 2

        elif self.text == 'Normal':
            self.text = 'Hard'
            config.level = 3

        else:
            self.text = 'Easy'
            config.level = 1


class Size(Button):
    def __init__(self):
        super(Size, self).__init__()
        self.text = 'Size: Small'
        self.size_hint = (None, None)
        self.width = 200
        self.height = 50
        self.pos_hint = {'center_x': 0.5}

    def on_press(self):
        if self.text == 'Small' or self.text == 'Size: Small':
            self.text = 'Normal'
            config.size = 8

        elif self.text == 'Normal':
            self.text = 'Big'
            config.size = 16

        else:
            self.text = 'Small'
            config.size = 4


layoutf = BoxLayout(orientation='vertical', spacing=20, padding=100)
layoutf.add_widget(Play())
layoutf.add_widget(Difficulty())
layoutf.add_widget(Size())
welcome = Screen(name='welcome')
welcome.add_widget(layoutf)


class Restart(Button):
    def on_press(self):
        sm.current = 'welcome'


class Win(Widget):
    def __init__(self):
        super(Win, self).__init__()
        self.layout = BoxLayout(orientation='vertical', padding=70, spacing=20)

        self.title = Label(text="You WIN!", bold=True, font_size=35,
                           outline_width=5, outline_color=(125, 125, 125))
        self.layout.add_widget(self.title)

        self.restart = (Restart(text='Play again!', size_hint=(None, None),
                        width=200, height=50, pos_hint={'center_x': 0.5}))

        self.layout.add_widget(self.restart)

        self.exit = (Button(text='Exit', size_hint=(None, None), width=200,
                     height=50, pos_hint={'center_x': 0.5}))
        self.exit.bind(on_press=self.close)
        self.layout.add_widget(self.exit)

        self.pop = Popup(content=self.layout, title='CONGRATULATIONS!',
                         separator_height=0, size_hint=(None, None),
                         size=(400, 400), auto_dismiss=False)
        self.restart.bind(on_press=self.pop.dismiss)

    def show(self):
        self.pop.open()

    def close(self, obj):
        App.get_running_app().stop()
        Window.close()


class Gameover(Widget):
    def __init__(self):
        super(Gameover, self).__init__()
        self.layout = BoxLayout(orientation='vertical', padding=100,
                                spacing=20)

        self.restart = (Restart(text='Play again!', size_hint=(None, None),
                        width=200, height=50, pos_hint={'center_x': 0.5}))
        self.layout.add_widget(self.restart)

        self.exit = (Button(text='Exit', size_hint=(None, None), width=200,
                     height=50, pos_hint={'center_x': 0.5}))
        self.exit.bind(on_press=self.close)
        self.layout.add_widget(self.exit)

        self.pop = Popup(content=self.layout, title='',
                         separator_height=0, size_hint=(None, None),
                         size=(400, 400), auto_dismiss=False,
                         background='Textures/MINESWEEPER_-1.png')

        self.restart.bind(on_press=self.pop.dismiss)

    def show(self):
        self.pop.open()

    def close(self, obj):
        App.get_running_app().stop()
        Window.close()


def changemode():
    global flagmode
    flagmode = not flagmode


class Tile (ToggleButtonBehavior, Image):

    coord = DictProperty({'x': 0, 'y': 0})

    def __init__(self, cols=0, rows=0):
        super(Tile, self).__init__()
        self.source = 'Textures/MINESWEEPER_X.png'
        self.allow_stretch = True
        self.keep_ratio = False
        self.coord['x'] = cols
        self.coord['y'] = rows

    def on_state(self, widget, value):
        if self.source == 'Textures/MINESWEEPER_X.png' and flagmode:
            self.source = 'Textures/MINESWEEPER_F.png'
        elif self.source == 'Textures/MINESWEEPER_F.png':
            self.source = 'Textures/MINESWEEPER_X.png'
        elif self.source == 'Textures/MINESWEEPER_X.png' and not flagmode:
            self.source = 'Textures/MINESWEEPER_' + str(check_tile(self.coord,
                                                        config.field)) + '.png'

            if check_tile(self.coord, config.field, True) == -1 and not flagmode:
                Gameover.show(Gameover())
            elif config.tiles_opened == ((config.size ** 2)
                                         - config.bomb_amount):
                Win.show(Win())


class StateButton (ToggleButtonBehavior, Image):
    def __init__(self):
        super(StateButton, self).__init__()
        self.source = 'Textures/MINESWEEPER_0.png'
        self.allow_stretch = True
        self.size = (90, 50)
        self.size_hint = (None, None)
        self.pos_hint = {'center_y': 0.5}

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'Textures/MINESWEEPER_F.png'
            changemode()
        else:
            changemode()
            self.source = 'Textures/MINESWEEPER_0.png'


class MinesweeperApp(App):
    icon = 'Textures/Minesweeper_icon.png'

    def build(self):
        sm.add_widget(welcome)
        sm.add_widget(gamefield)

        return sm

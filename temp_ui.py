from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

level_names = {'Easy': 1, 'Normal': 2, 'Hard': 3, 'Waaay harder': 4}
field_options ={'8x8': 8, '7x7': 7, '6x6': 6}

dropdown = DropDown()

class DrDownButton(Button):

    value = 0 
    
    def __init__(self, name, val):
        super().__init__()
        self.text = name
        self.value = val
        self.size_hint_y = None
        self.height = 40



def create_dropdown(main_name, selections):
    
    for name, value in selections.items():
        btn = DrDownButton(name, value)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
    mainbutton = Button(text=main_name, size_hint=(None, None))
    mainbutton.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    return mainbutton


class TestApp(App):

    def build(self):
        layout_rows = GridLayout(rows = 2, padding=20)
        layout_columns = BoxLayout(spacing=20)
        first = create_dropdown('Select level', level_names)
        second = create_dropdown('Select\nfield size', field_options)
        title = Label(text='Welcome to Minesweeper!')
        layout_columns.add_widget(first)
        layout_columns.add_widget(second)
        layout_rows.add_widget(title)
        layout_rows.add_widget(layout_columns)

        return layout_rows

if __name__ == '__main__':
    TestApp().run()

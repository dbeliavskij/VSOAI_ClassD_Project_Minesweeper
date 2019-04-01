from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout

level_names = ['Easy', 'Normal', 'Hard', 'Waaay harder']
dropdown = DropDown()

def 

class TestApp(App):
    
    def build(self):
        layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        for index in range(len(level_names)):
            btn = Button(text=level_names[index], size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # create a big main button
        mainbutton = Button(text='Select level', size_hint=(0.2, 0.2),
                            pos_hint = {'center_y': 0.5})

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        bt = Button()
        layout.add_widget(mainbutton)
        layout.add_widget(bt)
        
        return layout

if __name__ == '__main__':
    TestApp().run()
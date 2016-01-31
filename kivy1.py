import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        f = BoxLayout()
        for column in [1,2,3]:
            b2 = BoxLayout(orientation='vertical')
            for i in [1,2,3]:                
                b2.add_widget(Button(text='X', font_size=80))
            f.add_widget(b2)
        return f
if __name__ == '__main__':
    MyApp().run()

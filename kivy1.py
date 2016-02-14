import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

def are_equal(btn1, btn2, btn3):
    print '-----------------------------'
    print btn1.text
    print btn2.text
    print btn3.text
    print '----------------------------'
    if btn1.text == '' or btn2.text == '' or btn3.text == '':
        return False
    return btn1.text == btn2.text and btn1.text == btn3.text

def declare_victory():
    print "Victory"

def has_anyone_won(l):
    for lis in l:
        if are_equal(lis[0],lis[1],lis[2]) == True:
            return True
    for num in [0,1,2]:
        if are_equal(l[0][num],l[1][num],l[2][num]) == True:
            return True
    if are_equal(l[0][0],l[1][1],l[2][2]) == True:
        return True

    if are_equal(l[0][2],l[1][1],l[2][0]) == True:
        return True

def my_click(instance):
    if instance.text == '':
        instance.text = MyApp.next_string
        if has_anyone_won(MyApp.buttons)== True:
            declare_victory()
        if MyApp.next_string == 'X':
            MyApp.next_string = 'O'
            instance.color = [0,1,0,1]
        else:
            MyApp.next_string = 'X'
            instance.color = [1,0,0,1]
        
        


class MyApp(App):
    next_string = 'X'
    buttons = [[None, None, None],
               [None, None, None],
               [None, None, None]]
    def build(self):
        f = BoxLayout()
        for column in [0,1,2]:
            b2 = BoxLayout(orientation='vertical')
            for i in [0,1,2]:
                btn = Button(text='', font_size=80)
                MyApp.buttons[i][column] = btn
                btn.bind(on_press=my_click)
                b2.add_widget(btn)
                
            f.add_widget(b2)
        return f








        
if __name__ == '__main__':
    next_string = 'X'
    MyApp().run()

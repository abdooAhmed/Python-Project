import kivy
from docutils.nodes import definition_list

kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.graphics import Color,Rectangle
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.graphics import *
from kivy.uix.popup import Popup
from kivy.lang import Builder

class MainScreen(Screen):
    pass
class secondScreen(Screen):
    def btn(self):
        print('hi')
        pop()
class manager(ScreenManager):
    pass
class p(FloatLayout):
    pass
def pop():
    show=p()
    popw=Popup(title='error',content=show,size_hint=(None,None),size=(400,400))
    popw.open()

kv=Builder.load_file('drawall.kv')
class label(App):
    def build(self):
        return kv
lab=label()
lab.run()
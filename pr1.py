from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line
from kivy.properties import ListProperty,NumericProperty,ObjectProperty
import math
Builder.load_file('tool2.kv')
Builder.load_file('general2.kv')
Builder.load_file('drawing.kv')
Builder.load_file('status2.kv')
Builder.load_file('stick.kv')
Builder.load_file('main.kv')
class Stickw(RelativeLayout):
    def __init__(self, **kwargs):
        self.selected = None
        self.touched = False
        super(Stickw, self).__init__(**kwargs)
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.touched = True
            self.select()
            return True
        return super(Stickw, self).on_touch_down(touch)
    def select(self):
        if not self.selected:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
               self.selected = Line(rectangle=(0, 0, self.width, self.height), dash_offset=2)
    def on_touch_move(self, touch):
        (x, y) = self.parent.to_parent(touch.x, touch.y)
        if self.selected and self.touched and self.parent.collide_point(x - self.width / 2, y - self.height / 2):
            go = self.parent.general_options
            go.translation = (touch.x-self.ix, touch.y-self.iy)
            return True
        return super(Stickw, self).on_touch_move(touch)
    def translate(self, x, y):
        self.center_x = self.xi = x+self.ix
        self.center_y = self.xi = y+self.iy
    def on_touch_up(self, touch):
        self.touched = False
        if self.selected:
            if not self.parent.general_options.group_mode:
                self.unselect()
        return super(Stickw, self).on_touch_up(touch)
    def unselect(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected = None
class Stick(Stickw):
    pass
class Toolb(ToggleButton):
    def on_touch_down(self, touch):
        ds=self.parent.draw_space
        if self.state=='down' and ds.collide_point(touch.x,touch.y):
            (x,y)=ds.to_widget(touch.x,touch.y)
            self.draw(ds,x,y)
            return True
        return super(Toolb, self).on_touch_down(touch)
def draw(self, ds, x, y):
    pass
class ToggleStick(Toolb):
    def draw(self, ds, x, y):
        sm=Stick(width=48,height=48)
        sm.center=(x,y)
        ds.add_widget(sm)
class ToolFigur(Toolb):
    def draw(self,ds,x,y):
        (self.ix,self.iy)=(x,y)
        with ds.canvas:
            print('hi')
            self.figur=self.create_f(x,y,x+1,y+1)
            ds.bind(on_touch_move=self.figur_upd)
            ds.bind(on_touch_up=self.figur_end)
    def figur_upd(self,ds,touch):
        if ds.collide_point(touch.x,touch.y):
            (x,y)=ds.to_widget(touch.x,touch.y)
            ds.canvas.remove(self.figur)
            with ds.canvas:
                self.figur=self.create_f(self.ix,self.iy,x,y)
    def figur_end(self,ds,touch):
        ds.unbind(on_touch_move=self.figur_upd)
        ds.unbind(on_touch_up=self.figur_end)
        ds.canvas.remove(self.figur)
        (fx,fy)=ds.to_widget(touch.x,touch.y)
        self.widgetsize(ds,self.ix,self.iy,fx,fy)
    def widgetsize(self,ds,ix,iy,fx,fy):
        w=self.create_widget(ix,iy,fx,fy)
        (ix,iy)=w.to_local(ix,iy,relative=True)
        (fx,fy)=w.to_local(fx,fy,relative=True)
        w.canvas.add(self.create_f(ix,iy,fx,fy))
        ds.add_widget(w)
    def create_f(self,ix,iy,fx,fy):
        pass
    def create_widget(self,ix,iy,fx,fy):
        pass
class ToolCircle(ToolFigur):
    def create_f(self,ix,iy,fx,fy):
        print([ix,iy,math.hypot(ix-fx,iy,fy)])
        return Line(circle=[ix,iy,math.hypot(ix-fx,iy-fy)])

    def create_widget(self, ix, iy, fx, fy):
        r = math.hypot(ix - fx, iy - fy)
        pos = (ix - r, iy - r)
        size = (2 * r, 2 * r)
        return Stickw(pos=pos, size=size)
class ToolL(ToolFigur):
    def create_f(self,ix,iy,fx,fy):
        return Line(points=[ix,iy,fx,fy])
    def create_widget(self,ix,iy,fx,fy):
        pos=(min(ix,fx),min(iy,fy))
        size=(abs(ix-fx),abs(iy-fy))
        return Stickw(pos=pos,size=size)

class General(BoxLayout):
    group_mode=False
    translation=ListProperty(None)
    def clear(self,instance):
        self.drawing_space.clear_widgets()
    def remove(self,instance):
        ds=self.drawing_space
        if len(ds.children)>0:
            ds.remove_widget(ds.children[0])
    def group(self,instanse,value):
        if value=='down':
            self.group_mode=True
            print(self.group_mode)
            return self.group_mode
        else:
            print('hi')
            self.group_mode=False
            self.unselect_all()
            return self.group_mode
    def unselect_all(self):
        ds = self.drawing_space
        for child in ds.children:
            print(child)
            child.unselect()
    def on_translation(self,instance,value):
        ds = self.drawing_space
        print('trans')
        for child in ds.children:
            if child.selected:
                print(*self.translation)
                child.translate(*self.translation)
    def select(self):
        ds=self.drawing_space
        for child in ds.children:
            with child.canvas:
                Line(rectangle=(0,0,child.width,child.height))
class Status(BoxLayout):
    counter=NumericProperty(0)
    previos_c=1
    def on_counter(self,instance,value):
        print('ss')
        if value==0:
            self.msg_lebal.text = "Drawing space cleared"
        elif value - 1 == self.__class__.previos_c:
            self.msg_lebal.text = "Widget added"
        elif value + 1 == Status.previous_c:
            self.msg_lebal.text ="Widget removed"
        self.__class__.previous_c=value
        print(self.__class__.previos_c)
class Draw(RelativeLayout):
    def on_children(self,instance,value):
        print('dd')
        self.status_bar.counter = len(self.children)
class Main(AnchorLayout):
    pass
class app(App):
    def build(self):
        return Main()
app().run()
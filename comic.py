from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import BuilderBase
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.graphics import Line
class Drag(RelativeLayout):
    def __init__(self, **kwargs):
        self.selected=None
        self.ix=self.center_x
        self.iy=self.center_y
        super(Drag, self).__init__(**kwargs)
    def on_touch_down(self, touch):
        if self.collide_point(touch.x,touch.y):
            self.select()
            return True
        return super(Drag, self).on_touch_down(touch)
    def select(self):
        if not self.selected:
          print(self.center_x)
          self.ix = self.center_x
          self.iy = self.center_y
          with self.canvas:
             self.selected = Line(rectangle=
             (0, 0, self.width, self.height), dash_offset=2)
    def on_touch_move(self, touch):
        (x, y) = self.parent.to_parent(touch.x, touch.y)
        if self.select and  self.parent.collide_point(x - self.width/2, y - self.height/2):
            self.translate(touch.x-self.center_x,touch.y-self.center_y)
            return True
        return super(Drag, self).on_touch_move(touch)
    def translate(self,x,y):
        self.center_x = x+self.ix
        self.ix=self.center_x
        self.center_y = y+self.iy
        self.iy=self.center_y
    def on_touch_up(self, touch):
        if self.selected:
           self.unselect()
           return True
        return super(Drag, self).on_touch_up(touch)

    def unselect(self):
        if self.selected:
           self.canvas.remove(self.selected)
           self.selected = None
class StickMan(Drag):
    pass
class comic(AnchorLayout):
    pass
class comic1(App):
    def build(self):
        self.load_kv('stickman.kv')
        self.load_kv('comic.kv')
        self.load_kv('draw.kv')
        self.load_kv('tool.kv')
        self.load_kv('general.kv')
        self.load_kv('status.kv')
        return comic()
if __name__=="__main__":
    comic1().run()
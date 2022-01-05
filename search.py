import kivy
kivy.require('1.10.0')
print(kivy.version)
from kivy.app import App
from kivy.clock import Clock
from plyer import accelerometer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
class Accel(Widget):
    def __init__(self):
        super(Accel, self).__init__()
        self.sensorEnabled = False

    def get_acceleration(self, dt):
        val = accelerometer.acceleration
        self.ids.label1.text = "X: " + str(val[0])
        self.ids.label2.text = "Y: " + str(val[1])
        self.ids.label3.text = "Z: " + str(val[2])

    def pressed1(self):
        try:
            if not self.sensorEnabled:
                accelerometer.enable()
                Clock.schedule_interval(self.get_acceleration,1 / 20.)
                self.sensorEnabled = True
                self.ids.button1.text = "Stop"
            else:
                accelerometer.disable()
                Clock.unschedule(self.get_acceleration)
                self.sensorEnabled = False
                self.ids.button1.text = "Start"
        except NotImplementedError:
             import traceback;
             traceback.print_exc()
             self.ids.status.text ="Accelerometer is not supported for your platform"
class app(App):
    def build(self):
        self.load_kv('addlocation.kv')
        return Accel()
app().run()
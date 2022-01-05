from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
import screen
from kivymd.uix.label import MDLabel
f_n=[]
l_n=[]
i_d=[]
p_w=[]
email=[]
dep=[]
num=0
num1=0
kv='''
<MDLabel>:
    color:1,0,0,1
ScreenManager:
    Choice_page:
    AdminScreen:
    ScoundScreen:
    Create_user:
    Updata_con:
    Display_clerk:
    Create_con:
    Create_Admin:
    Create_Admin_con:
    display_con:
    Display:
    Delete_con:
    Delete_clerk:
    Update_clerk1:
    Update_clerk2:
    Creat_product:
    Creat_product_con:
<Choice_page>:
    name:'f_p'
    MDLabel:
        text:'Welcome'
        pos_hint:{'center_x':.85,'center_y':0.8}
        font_style:'H2'
        color:1,0,0,1
    MDRectangleFlatButton:
        text:'Admin'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:root.switch('a_p') 
        size_hint:(.2,None)
<AdminScreen>:
    name:'a_p'
    MDLabel:
        text:'Login'
        pos_hint:{'center_x':.9,'center_y':0.8}
        font_style:'H2'
        color:1,0,0,1
    MDTextField:
        id:username
        hint_text:'Enter Email'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDTextField:
        id:password
        hint_text:'Enter Password'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'submit'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.switch()
<Create_Admin_con>:
    name:'Create_Admin_con'
    MDLabel:
        text:'check your authorization'
        pos_hint:{'center_x':.78,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDTextField:
        id:username
        hint_text:'Enter Email'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDTextField:
        id:password
        hint_text:'Enter Password'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'submit'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.switch() 
<Create_Admin>:
    name:'Create_Admin'
    MDLabel:
        text:'First Name'
        pos_hint:{'center_x':0.55,'center_y':0.8}
    MDTextField:
        id:f_n
        hint_text:'f_n'
        pos_hint:{'center_x':0.27,'center_y':0.8}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDTextField:
        id:l_n
        hint_text:'l_n'
        pos_hint:{'center_x':0.72,'center_y':0.8}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'ID'
        pos_hint:{'center_x':0.55,'center_y':0.7}
    MDTextField:
        id:i_d
        hint_text:'i_n'
        pos_hint:{'center_x':0.27,'center_y':0.7}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'Email'
        pos_hint:{'center_x':0.55,'center_y':0.6}
    MDTextField:
        id:e_m
        hint_text:'e_m'
        pos_hint:{'center_x':0.364,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300
    MDLabel:
        text:'Password'
        pos_hint:{'center_x':0.55,'center_y':0.5}
    MDTextField:
        id:p_w
        hint_text:'p_w'
        pos_hint:{'center_x':0.27,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:150
    MDLabel:
        text:'authorization'
        pos_hint:{'center_x':0.52,'center_y':0.4}
    MDTextField:
        id:a_u
        hint_text:'a_u'
        pos_hint:{'center_x':0.27,'center_y':0.4}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:150  
    MDRectangleFlatButton:
        text:'create'
        pos_hint:{'center_x':0.7,'center_y':0.2}
        on_press:root.save_admin() 
<ScoundScreen>:
    name:'s_p' 
    MDRectangleFlatButton:
        text:'Create new clerk'
        pos_hint:{'center_x':0.8,'center_y':0.85}
        on_press:root.switch('c_c')
    MDRectangleFlatButton:
        text:'Display clerk info'
        pos_hint:{'center_x':0.8,'center_y':0.65}
        on_press:root.switch('display_cond') 
    MDRectangleFlatButton:
        text:'update clerk info'
        pos_hint:{'center_x':0.8,'center_y':0.45}
        on_press:root.switch('update_cond')  
    MDRectangleFlatButton:
        text:'Delete clerk'
        pos_hint:{'center_x':0.2,'center_y':0.45}
        on_press:root.switch('delete_cond')
    MDRectangleFlatButton:
        text:'new A_account'
        pos_hint:{'center_x':0.2,'center_y':0.65}
        on_press:root.switch('Create_Admin_con') 
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.5,'center_y':0.05}
        on_press:root.switch('f_p')
    MDRectangleFlatButton:
        text:'Create new product'
        pos_hint:{'center_x':0.2,'center_y':0.85}
        on_press:root.switch('create_product_cond')


        
   
<Create_user>:
    name:'c_p'
    MDLabel:
        text:'First Name'
        pos_hint:{'center_x':0.55,'center_y':0.8}
    MDTextField:
        id:f_n
        hint_text:'f_n'
        pos_hint:{'center_x':0.27,'center_y':0.8}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDTextField:
        id:l_n
        hint_text:'l_n'
        pos_hint:{'center_x':0.72,'center_y':0.8}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'ID'
        pos_hint:{'center_x':0.55,'center_y':0.7}
    MDTextField:
        id:i_d
        hint_text:'i_n'
        pos_hint:{'center_x':0.27,'center_y':0.7}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'Email'
        pos_hint:{'center_x':0.55,'center_y':0.6}
    MDTextField:
        id:e_m
        hint_text:'e_m'
        pos_hint:{'center_x':0.364,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300
    MDLabel:
        text:'Password'
        pos_hint:{'center_x':0.55,'center_y':0.5}
    MDTextField:
        id:p_w
        hint_text:'p_w'
        pos_hint:{'center_x':0.27,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:150
    MDLabel:
        text:'Department'
        pos_hint:{'center_x':0.55,'center_y':0.4}
    MDTextField:
        id:d_p
        hint_text:'d_p'
        pos_hint:{'center_x':0.27,'center_y':0.4}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDRectangleFlatButton:
        text:'create'
        pos_hint:{'center_x':0.7,'center_y':0.2}
        on_press:root.save_user()
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.4,'center_y':0.2}
        on_press:root.switch('f_p')
<Creat_product_con>:
    name:'create_product_cond'
    MDLabel:
        text:'check your authorization'
        pos_hint:{'center_x':.78,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDTextField:
        id:username
        hint_text:'Enter Username'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDTextField:
        id:password
        hint_text:'Enter Password'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'submit'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.switch() 
<Display_clerk>:
    name:'display_clerk'
    MDLabel:
        text:'clerk info'
        pos_hint:{'center_x':0.9,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDLabel:
        text:'Email'
        pos_hint:{'center_x':0.78,'center_y':0.6}
    MDTextField:
        id:e_m
        hint_text:'e_m'
        pos_hint:{'center_x':0.565,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDLabel:
        text:'Password'
        pos_hint:{'center_x':0.72,'center_y':0.5}
    MDTextField:
        id:p_w
        hint_text:'p_w'
        pos_hint:{'center_x':0.57,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'GO'
        pos_hint:{'center_x':0.6,'center_y':0.3}
        on_press:root.display()
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.4,'center_y':0.3}
        on_press:root.switch('f_p')
<Create_con>:
    name:'c_c'
    MDLabel:
        text:'check your authorization'
        pos_hint:{'center_x':.78,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDTextField:
        id:username
        hint_text:'Enter Username'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDTextField:
        id:password
        hint_text:'Enter Password'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'submit'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.switch()
<display_con>:
    name:'display_cond'
    MDLabel:
        text:'check your authorization'
        pos_hint:{'center_x':.78,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDTextField:
        id:username
        hint_text:'Enter Username'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDTextField:
        id:password
        hint_text:'Enter Password'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'submit'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.switch() 
<Display>:
    name:'Display'
    MDRectangleFlatButton:
        text:'display'
        pos_hint:{'center_x':0.6,'center_y':0.3}
        on_press:root.display()
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.4,'center_y':0.3}
        on_press:root.switch('f_p') 
    MDLabel:
        id:i_d
        text:'First Name'
        pos_hint:{'center_x':0.55,'center_y':0.8}
    MDLabel:
        id:f_n
        text:'First Name'
        pos_hint:{'center_x':0.55,'center_y':0.7}
    MDLabel:
        id:l_n
        text:'First Name'
        pos_hint:{'center_x':0.55,'center_y':0.6}
    MDLabel:
        id:d_p
        text:'First Name'
        pos_hint:{'center_x':0.55,'center_y':0.5}
<Delete_con>:
    name:'delete_cond'
    MDLabel:
        text:'check your authorization'
        pos_hint:{'center_x':.78,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDTextField:
        id:username
        hint_text:'Enter Username'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDTextField:
        id:password
        hint_text:'Enter Password'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'submit'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.switch()
<Delete_clerk>:
    name:'delete_clerk'
    MDLabel:
        text:'clerk info'
        pos_hint:{'center_x':0.9,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDLabel:
        text:'Email'
        pos_hint:{'center_x':0.78,'center_y':0.6}
    MDTextField:
        id:e_m
        hint_text:'e_m'
        pos_hint:{'center_x':0.565,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDLabel:
        text:'Password'
        pos_hint:{'center_x':0.72,'center_y':0.5}
    MDTextField:
        id:p_w
        hint_text:'p_w'
        pos_hint:{'center_x':0.57,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'Delete'
        pos_hint:{'center_x':0.6,'center_y':0.3}
        on_press:root.delete()
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.4,'center_y':0.3}
        on_press:root.switch('f_p')
<Updata_con>:
    name:'update_cond'
    MDLabel:
        text:'check your authorization'
        pos_hint:{'center_x':.78,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDTextField:
        id:username
        hint_text:'Enter Username'
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDTextField:
        id:password
        hint_text:'Enter Password'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'submit'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.switch()
<Update_clerk1>:
    name:'update_clerk1'
    MDLabel:
        text:'clerk info'
        pos_hint:{'center_x':0.9,'center_y':0.8}
        font_style:'H4'
        color:1,0,0,1
    MDLabel:
        text:'Email'
        pos_hint:{'center_x':0.78,'center_y':0.6}
    MDTextField:
        id:e_m
        hint_text:'e_m'
        pos_hint:{'center_x':0.565,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300 
    MDLabel:
        text:'Password'
        pos_hint:{'center_x':0.72,'center_y':0.5}
    MDTextField:
        id:p_w
        hint_text:'p_w'
        pos_hint:{'center_x':0.57,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:300
    MDRectangleFlatButton:
        text:'Update'
        pos_hint:{'center_x':0.6,'center_y':0.3}
        on_press:root.update()
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.4,'center_y':0.3}
        on_press:root.switch('f_p') 
<Update_clerk2>:
    name:'update_clerk2'
    MDLabel:
        text:'First Name'
        pos_hint:{'center_x':0.55,'center_y':0.8}
    MDTextField:
        id:f_n
        hint_text:'f_n'
        pos_hint:{'center_x':0.27,'center_y':0.8}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDTextField:
        id:l_n
        hint_text:'l_n'
        pos_hint:{'center_x':0.72,'center_y':0.8}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'ID'
        pos_hint:{'center_x':0.55,'center_y':0.7}
    MDTextField:
        id:i_d
        hint_text:'i_n'
        pos_hint:{'center_x':0.27,'center_y':0.7}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'Email'
        pos_hint:{'center_x':0.55,'center_y':0.6}
    MDTextField:
        id:e_m
        hint_text:'e_m'
        pos_hint:{'center_x':0.364,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300
    MDLabel:
        text:'Password'
        pos_hint:{'center_x':0.55,'center_y':0.5}
    MDTextField:
        id:p_w
        hint_text:'p_w'
        pos_hint:{'center_x':0.27,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        password:True
        width:150
    MDLabel:
        text:'Department'
        pos_hint:{'center_x':0.55,'center_y':0.4}
    MDTextField:
        id:d_p
        hint_text:'d_p'
        pos_hint:{'center_x':0.27,'center_y':0.4}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDRectangleFlatButton:
        text:'updata'
        pos_hint:{'center_x':0.7,'center_y':0.2}
        on_press:root.save_user()
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.4,'center_y':0.2}
        on_press:root.switch('f_p')
<Creat_product>:
    name:'create_product'
    MDLabel:
        text:'Product Name'
        pos_hint:{'center_x':0.55,'center_y':0.8}
    MDTextField:
        id:p_n
        hint_text:'p_n'
        pos_hint:{'center_x':0.27,'center_y':0.8}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'ID'
        pos_hint:{'center_x':0.55,'center_y':0.7}
    MDTextField:
        id:i_d
        hint_text:'i_d'
        pos_hint:{'center_x':0.27,'center_y':0.7}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDLabel:
        text:'Price'
        pos_hint:{'center_x':0.55,'center_y':0.6}
    MDTextField:
        id:p_p
        hint_text:'p_p'
        pos_hint:{'center_x':0.364,'center_y':0.6}
        size_hint_x:None
        mode: "rectangle"
        width:300
    MDLabel:
        text:'Department'
        pos_hint:{'center_x':0.55,'center_y':0.5}
    MDTextField:
        id:d_p
        hint_text:'d_p'
        pos_hint:{'center_x':0.27,'center_y':0.5}
        size_hint_x:None
        mode: "rectangle"
        width:150
    MDRectangleFlatButton:
        text:'Create'
        pos_hint:{'center_x':0.7,'center_y':0.2}
        on_press:root.create()
    MDRectangleFlatButton:
        text:'Log out'
        pos_hint:{'center_x':0.4,'center_y':0.2}
        on_press:root.switch('f_p')
   
   
'''
class Choice_page(Screen):
    def switch(self,cl):
        self.manager.current = cl
class AdminScreen(Screen):
    def switch(self):
        if screen.admin.chek(screen.admin,'',self.ids.username.text,self.ids.password.text):
            self.manager.current='s_p'
            self.ids.password.text=''
            self.ids.username.text=''
class Display_clerk(Screen):
    def display(self):
        if screen.user.check(screen.user,self.ids.e_m.text,self.ids.p_w.text) :
            print('innnnnn')
            self.manager.current='Display'
    def switch(self,cl):
        self.manager.current = cl
class ScoundScreen(Screen):
    def switch(self,cl):
        self.manager.current = cl
class Create_user(Screen):
    def switch(self,cl):
        self.manager.current = cl
    def save_user(self):
        if self.ids.f_n.text and self.ids.l_n.text and self.ids.i_d.text and self.ids.d_p.text and self.ids.p_w.text and self.ids.e_m.text:
               screen.user.add(screen.user,self.ids.i_d.text,self.ids.f_n.text,self.ids.l_n.text,self.ids.e_m.text,self.ids.p_w.text,self.ids.d_p.text)
class display_con(Screen):
    def switch(self):
        if screen.admin.chek(screen.admin,'top',self.ids.username.text,self.ids.password.text) or screen.admin.chek(screen.admin,'medium',self.ids.username.text,self.ids.password.text):
            self.manager.current='display_clerk'
class Create_Admin_con(Screen):
    def switch(self):
        if screen.admin.chek(screen.admin,'top',self.ids.username.text,self.ids.password.text):
            self.manager.current='Create_Admin'
            self.ids.password.text=''
            self.ids.username.text=''
class Create_Admin(Screen):
    def save_admin(self):
        if self.ids.f_n.text and self.ids.l_n.text and self.ids.i_d.text and self.ids.a_u.text and self.ids.p_w.text and self.ids.e_m.text:
            screen.admin.add(screen.admin,self.ids.i_d.text,self.ids.f_n.text,self.ids.l_n.text,self.ids.e_m.text,self.ids.p_w.text,self.ids.a_u.text)
            print('in')

class Create_con(Screen):
    def switch(self):
        if screen.admin.chek(screen.admin,'top',self.ids.username.text,self.ids.password.text) or screen.admin.chek(screen.admin,'medium',self.ids.username.text,self.ids.password.text) or screen.admin.chek(screen.admin,'low',self.ids.username.text,self.ids.password.text):
            self.manager.current='c_p'
class Display(Screen):
    def display(self):
        data=screen.user.dispaly(screen.user)
        self.ids.i_d.text = str(data[0])
        self.ids.f_n.text = str(data[1])
        self.ids.l_n.text = str(data[2])
        self.ids.f_n.text = str(data[5])

class Creat_product_con(Screen):
    def switch(self):
        if screen.admin.chek(screen.admin,'top',self.ids.username.text,self.ids.password.text) or screen.admin.chek(screen.admin,'medium',self.ids.username.text,self.ids.password.text):
            self.manager.current='create_product'
class Delete_con(Screen):
    def switch(self):
        if screen.admin.chek(screen.admin,'top',self.ids.username.text,self.ids.password.text):
            self.manager.current='delete_clerk'
class Delete_clerk(Screen):
    def delete(self):
        if screen.user.check(screen.user,self.ids.e_m.text,self.ids.p_w.text):
            screen.user.delete(screen.user,self.ids.e_m.text,self.ids.p_w.text)

class Updata_con(Screen):
    def switch(self):
        if screen.admin.chek(screen.admin,'top',self.ids.username.text,self.ids.password.text) or screen.admin.chek(screen.admin,'medium',self.ids.username.text,self.ids.password.text):
            self.manager.current='update_clerk1'
class Update_clerk1(Screen):
    def update(self):
        if screen.user.check(screen.user,self.ids.e_m.text,self.ids.p_w.text):
            print('innn')
            self.manager.current='update_clerk2'
class Update_clerk2(Screen):
    def save_user(self):
        if self.ids.f_n.text and self.ids.l_n.text and self.ids.i_d.text and self.ids.d_p.text and self.ids.p_w.text and self.ids.e_m.text:
               screen.user.update(screen.user,self.ids.f_n.text,self.ids.l_n.text,self.ids.e_m.text,self.ids.p_w.text,self.ids.d_p.text)
class Creat_product(Screen):
    def create(self):
        if  self.ids.i_d.text and self.ids.p_n.text and self.ids.p_p.text and self.ids.d_p.text:
            screen.product.add(screen.product,self.ids.i_d.text,self.ids.p_n.text,self.ids.p_p.text,self.ids.d_p.text)
s_m=ScreenManager()
s_m.add_widget(Choice_page(name='f_p'))
s_m.add_widget(AdminScreen(name='a_p'))
s_m.add_widget(ScoundScreen(name='s_p'))
s_m.add_widget(Display_clerk(name='display_clerk'))
s_m.add_widget(Create_user(name='c_p'))
s_m.add_widget(Create_con(name='c_c'))
s_m.add_widget(display_con(name='display_cond'))
s_m.add_widget(Display(name='Display'))
s_m.add_widget(Delete_con(name='delete_cond'))
s_m.add_widget(Updata_con(name='update_cond'))
s_m.add_widget(Update_clerk1(name='update_clerk1'))
s_m.add_widget(Update_clerk1(name='update_clerk2'))
s_m.add_widget(Create_Admin_con(name='Create_Admin_con'))
s_m.add_widget(Create_Admin(name='Create_Admin'))
s_m.add_widget(Creat_product_con(name='create_product_cond'))
s_m.add_widget(Creat_product(name='create_product'))
class app(MDApp):
    def build(self):
        self.theme_cls.theme_style='Light'
        self.theme_cls.primary_palette='Red'
        self.s=Builder.load_string(kv)
        return self.s
app().run()
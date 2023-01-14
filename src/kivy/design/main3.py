from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image,AsyncImage
from kivy.uix.behaviors import ButtonBehavior

from kivy.uix.label import Label
from vedio import *

Builder.load_file("design3.kv")

class SignLangInt(Screen):
    def sec_screen(self):
        self.manager.current="Sec_screen"

class SecScreen(Screen):
    def capture(self):
        camera=self.ids['camera']
        # timestr=time.strftime("%Y%m%d_%H%M%S")
        count=1
        camera.export_to_png("./SLI_{}.png".format(count))
        # img=AsyncImage(source='https://miro.medium.com/max/1050/1*kuqOPIyFNy9P-lLR3JiuMQ.png')
        # Image('SLI_1.png').save('/sdcard/DCIM/SLI_1.jpg')
        predict("SLI_1.png")
        print("captured")
        

    def back(self):
        self.manager.current="Sign_lang"

    def third_screen(self):
       # predict("SLI_1.png")
        self.manager.current="Third_sec"    

class ImageButton(ButtonBehavior,Image):
    pass       

class RootWidget(ScreenManager):
    pass

class SLIApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":        
    SLIApp().run()        
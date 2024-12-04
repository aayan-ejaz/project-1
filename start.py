from kivy.core.text import LabelBase
from kivy.animation import Animation
from kivymd.uix.button import MDIconButton
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (310, 580)


class SyncFit(MDApp):
    def toggle_password_visibility(self, text_field, icon_button):
        """
        Toggles the password visibility and updates the icon.

        Args:
            text_field (MDTextField): The password input field.
            icon_button (MDIconButton): The eye icon button.
        """
        if text_field.password:
            text_field.password = False
            icon_button.icon = "eye"  
        else:
            text_field.password = True
            icon_button.icon = "eye-off"  

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("join_now.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("reset.kv"))
        return screen_manager
    
if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular=r"D:\Poppins\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular=r"D:\Poppins\Poppins-SemiBold.ttf")
    
    SyncFit().run()




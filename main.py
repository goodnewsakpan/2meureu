"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
from kivy import platform
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDSharedAxisTransition
from kivymd.uix.progressindicator import MDCircularProgressIndicator
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.utils.set_bars_colors import set_bars_colors

from Components.bar import win_md_bnb
from View.screens import screens
from Model.database import DataBase
from Components.factory import register_factory

register_factory()


class TmeureuApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        self.database = DataBase()
        self.theme_cls.bind(
            theme_style=self.update_colors,
            surfaceColor=Window.setter("clearcolor")
        )

    def build(self):
        Builder.load_file("imports.kv")
        # This is the screen manager that will contain all the screens of your
        # application.
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Black"
        # self.theme_cls.dynamic_scheme_name = "FRUIT_SALAD"
        # self.theme_cls.dynamic_scheme_contrast = -1
        self.root = MDScreenManager(transition=MDSharedAxisTransition())
        spinner = MDCircularProgressIndicator(line_width=dp(1.5))
        self.dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[0] * 4,
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            on_pre_open=lambda _: setattr(spinner, "active", True),
            on_dismiss=lambda _: setattr(spinner, "active", False)
        )
        self.dialog.add_widget(spinner)
        # self.add_screen("home screen", first=True)

    @staticmethod
    def update_colors(instance, value):
        set_bars_colors(
            instance.surfaceColor,
            instance.surfaceColor,
            "Dark" if value == "Light" else "Light"
        )

    def add_screen(self, name_screen, switch=True, first=False):
        if first:
            self.load_screen(name_screen, switch, first)
            return
        if not self.root.has_screen(name_screen):
            self.dialog.open()
            Clock.schedule_once(lambda _: self.load_screen(name_screen, switch, first), 1)
        elif switch:
            self.root.current = name_screen

    def load_screen(self, name_screen, switch, first):
        Builder.load_file(screens[name_screen]["kv"])
        model = screens[name_screen]["model"](self.database)
        controller = screens[name_screen]["controller"](self, model)
        view = screens[name_screen]["view"](self, model=model, controller=controller)
        controller.set_view(view)
        self.root.add_widget(view)
        if switch:
            self.root.current = name_screen
        if not first:
            self.dialog.dismiss()

    def on_start(self):
        Window.clearcolor = self.theme_cls.surfaceColor
        self.update_colors(self.theme_cls, self.theme_cls.theme_style)
        win_md_bnb.create_bnb(
            tabs=[
                {
                    "icon": "finance",
                    "icon_variant": "finance",
                    "text": "Finance",
                    "active": True,
                    "on_release": lambda _: self.add_screen("finance screen")
                },
                {
                    "icon": "book-open-page-variant",
                    "icon_variant": "book-open-page-variant-outline",
                    "text": "Assessment",
                    "active": False,
                    "on_release": lambda _: self.add_screen("assessment screen")
                },
                {
                    "icon": "bell-ring",
                    "icon_variant": "bell-ring-outline",
                    "text": "Activity",
                    "active": False,
                    "on_release": lambda _: self.add_screen("activity screen")
                }
            ],
        )
        if platform == "android" and (user := self.database.user.get_current_user()):
            user.reload()
            if user and user.getDisplayName():
                self.add_screen("finance screen")
            elif user:
                self.add_screen("user screen")
        if platform != "android" or not self.database.user.get_current_user():
            self.add_screen("login screen", first=True)


if __name__ == "__main__":
    TmeureuApp().run()

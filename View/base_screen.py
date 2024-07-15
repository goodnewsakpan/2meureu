from kivy.clock import mainthread
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.utils.set_bars_colors import set_bars_colors

from Components.bar import win_md_bnb
from Utility.observer import Observer
from libs.singleton import screen_extras


class BaseScreenView(MDScreen, Observer):
    """
    A base class that implements a visual representation of the model data.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.controller_screen.ClassScreenControler`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.model_screen.ClassScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, app, **kw):
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = app
        # Adding a view class as observer.
        self.model.add_observer(self)

    @staticmethod
    def put_extra(key, value):
        screen_extras[key] = value

    @staticmethod
    def get_extra(key):
        return screen_extras[key]

    @staticmethod
    def remove_extra(key):
        del screen_extras[key]

    @mainthread
    def switch_screen(self, screen_name):
        self.app.add_screen(screen_name)

    @mainthread
    def toast(self, text):
        from kivymd.toast import toast
        toast(text)
        self.dismiss_dialog()

    @mainthread
    def dismiss_dialog(self):
        self.app.dialog.dismiss()

    @mainthread
    def open_dialog(self):
        self.app.dialog.open()

    def on_pre_enter(self):
        win_md_bnb.push()
        set_bars_colors(
            self.theme_cls.surfaceColor,
            win_md_bnb.bar.md_bg_color
        )

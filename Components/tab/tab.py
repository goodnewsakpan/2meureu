from os.path import join, dirname, basename
from kivy.lang import Builder
from kivy.properties import NumericProperty, VariableListProperty, OptionProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.behaviors import ToggleButtonBehavior

Builder.load_file(join(dirname(__file__), basename(__file__).split(".")[0] + ".kv"))

__all__ = ("TabsBar", "TabsItem", "TabsItemText")


class TabsBar(ThemableBehavior, MDScrollView):
    __events__ = ("on_switch_tabs",)
    previous_active_tab_index = NumericProperty()
    container_padding = VariableListProperty("10dp")

    def switch_tabs(self, tab_item):
        tab_item_container = self.ids.tab_item_container
        current_active_tab_index = tab_item_container.children.index(tab_item)
        if not self.previous_active_tab_index:
            self.previous_active_tab_index = current_active_tab_index
        self.scroll_to(
            tab_item_container.children[
                max(0, current_active_tab_index - 1)
                if current_active_tab_index < self.previous_active_tab_index
                else min(len(tab_item_container.children) - 1, current_active_tab_index + 1)
            ]
        )
        self.previous_active_tab_index = current_active_tab_index
        self.dispatch("on_switch_tabs", tab_item)

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, TabsItem):
            widget.bind(on_release=self.switch_tabs)
            self.ids.tab_item_container.add_widget(widget)
        else:
            return super().add_widget(widget)

    def on_switch_tabs(self, *args):
        pass


class TabsItem(ToggleButtonBehavior, MDCard):
    padding = VariableListProperty(["15dp", "10dp", "15dp", "10dp"])
    radius = VariableListProperty("10dp")

    def add_widget(self, widget, *args, **kwargs):
        if isinstance(widget, TabsItemText):
            widget.state = self.state
            self.bind(state=widget.setter("state"))
            self.ids["tab_item_text"] = widget
        super().add_widget(widget, *args, **kwargs)


class TabsItemText(MDLabel):
    state = OptionProperty('normal', options=('normal', 'down'))

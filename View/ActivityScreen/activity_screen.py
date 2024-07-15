from kivymd.uix.list import MDListItem, MDListItemSupportingText, MDListItemTertiaryText, \
    MDListItemHeadlineText
from kivy.clock import mainthread
from View.base_screen import BaseScreenView


class ActivityScreenView(BaseScreenView):
    def __init__(self, app, **kw):
        super().__init__(app, **kw)
        self.controller.get_child_activity()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    @mainthread
    def populate_data(self, data):
        self.ids.container.add_widget(
            MDListItem(
                MDListItemHeadlineText(
                    text=data["title"]
                ),
                MDListItemSupportingText(
                    text=data["body"],
                    theme_text_color="Custom",
                    text_color=self.theme_cls.disabledTextColor
                ),
                radius="16dp",
                theme_bg_color="Custom",
                md_bg_color=self.theme_cls.surfaceContainerHighestColor
            ),
            index=-1
        )

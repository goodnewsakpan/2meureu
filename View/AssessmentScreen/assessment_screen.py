from kivy.clock import mainthread
from kivymd.uix.list import MDListItem, MDListItemSupportingText, MDListItemTertiaryText, \
    MDListItemTrailingSupportingText

from View.base_screen import BaseScreenView


class AssessmentScreenView(BaseScreenView):
    def __init__(self, app, **kw):
        super().__init__(app, **kw)
        self.controller.get_child_assessments()

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
                MDListItemSupportingText(
                    text=data["subject"]
                ),
                MDListItemTertiaryText(
                    text=data["date"],
                    role="small",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.disabledTextColor
                ),
                MDListItemTrailingSupportingText(
                    text=f"{data['score']}%",
                    bold=True,
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primaryColor
                ),
                radius="16dp",
                theme_bg_color="Custom",
                md_bg_color=self.theme_cls.surfaceContainerHighestColor
            ),
            index=-1
        )

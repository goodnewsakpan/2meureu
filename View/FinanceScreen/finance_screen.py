from jnius import JavaException
from kivy.clock import mainthread
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogIcon, MDDialogHeadlineText, MDDialogSupportingText, \
    MDDialogButtonContainer
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemSupportingText, \
    MDListItemTertiaryText, MDListItemTrailingSupportingText
import asynckivy as ak

from View.base_screen import BaseScreenView
try:
    from android.runnable import run_on_ui_thread
    from libs.paystack import paystack
    from libs.jinterface.paystack import PaystackSheetResultCallback
except (ImportError, JavaException):
    pass


class FinanceScreenView(BaseScreenView):
    def __init__(self, app, **kw):
        super().__init__(app, **kw)
        self.controller.get_upcoming_payments()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_enter(self) -> None:
        self.check_email_verification()

    def check_email_verification(self, dialog=None):
        if dialog:
            dialog.dismiss()
        user = self.model.db.user.get_current_user()
        user.reload()
        if user.isEmailVerified():
            return
        print(user.isEmailVerified())
        print(user.getDisplayName())
        dialog = MDDialog(
            MDDialogIcon(
                icon="email-alert",
            ),
            MDDialogHeadlineText(
                text="Email Verification",
                halign="center",
            ),
            MDDialogSupportingText(
                text="Your email is not verified yet, "
                     "please head over to your email click on the verification link",
                halign="center",
            ),
            MDDialogButtonContainer(
                MDButton(
                    MDButtonText(text="Resend email"),
                    style="text",
                    on_release=lambda *_: self.send_email_verification()
                ),
                Widget(),
                MDButton(
                    MDButtonText(text="I have verified"),
                    style="text",
                    on_release=lambda *_: self.check_email_verification(dialog)
                ),
                spacing="8dp",
            ),
            size_hint_x=.9,
            auto_dismiss=False
        )
        dialog.open()

    def send_email_verification(self):
        self.model.send_email_verification()
        self.toast("Verification email sent")

    @mainthread
    def populate_data(self, data):
        self.ids.container.add_widget(
            MDListItem(
                MDListItemLeadingIcon(
                    icon="arrow-up",
                    theme_icon_color="Custom",
                    icon_color=self.theme_cls.primaryColor
                ),
                MDListItemSupportingText(
                    text=data["title"]
                ),
                MDListItemTertiaryText(
                    text=data["date"],
                    role="small",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.disabledTextColor
                ),
                MDListItemTrailingSupportingText(
                    text=f"₦ {data['amount']:,.2f}",
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

    @mainthread
    def populate_card(self, data):
        data["amount"] = f"₦ {data['amount']:,.2f}"
        self.ids.card.data = data

    async def initiate_payment(self, payment_details):
        self.put_extra("payment_details", payment_details)
        data = {
            "amount": float(
                payment_details["amount"]
                .replace(',', '')
                .replace('.', '')
                .replace("₦ ", '')
            ),
            "email": self.model.db.user.get_current_user().getEmail()
        }
        func = lambda: self.controller.initiate_payment(data)
        access_code = await ak.run_in_thread(func)
        self.make_payment(access_code)
    try:
        @run_on_ui_thread
        def make_payment(self, access_code):
            self.paystack_payment_callback = PaystackSheetResultCallback(
                print, print, print
            )
            print(dir(paystack))
            print(access_code)

            paystack.make_payment(access_code, self.paystack_payment_callback)
    except NameError:
        pass

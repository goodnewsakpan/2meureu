from jnius import autoclass

from sjfirebase.jinterface import OnCompleteListener

from Model.base_model import BaseScreenModel
from libs.decorator import silencer


class UserScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.UserScreen.user_screen.UserScreenView` class.
    """

    def __init__(self, database):
        super().__init__(database)
        self.profile_update_listener = None

    def __android_init__(self):
        self.ref = self.db.firestore.get_db().document(f"parent/{self.db.user.get_current_user().getUid()}")

    @silencer
    def submit_user_details(self, name, phone_number, callback):
        profile_update = self.db.user.profile_change_request_builder().setDisplayName(name).build()
        user = self.db.user.get_current_user()
        self.profile_update_listener = OnCompleteListener(self.send_email_verification)
        user.updateProfile(profile_update).addOnCompleteListener(self.profile_update_listener)

        user_detail = autoclass("java.util.HashMap")()
        user_detail.put("name", name)
        user_detail.put("phone_number", phone_number)

        self.listener = OnCompleteListener(callback)
        self.ref.set(user_detail).addOnCompleteListener(self.listener)

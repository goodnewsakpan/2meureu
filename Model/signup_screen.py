from sjfirebase.jinterface import OnCompleteListener

from Model.base_model import BaseScreenModel
from libs.decorator import silencer


class SignupScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SignupScreen.signup_screen.SignupScreenView` class.
    """

    def __init__(self, database):
        super().__init__(database)

    @silencer
    def signup(self, email, password, callback):
        self.listener = OnCompleteListener(callback)
        auth = self.db.auth.get_instance()
        auth.createUserWithEmailAndPassword(email, password).addOnCompleteListener(self.listener)

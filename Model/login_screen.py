from sjfirebase.jinterface import OnCompleteListener

from Model.base_model import BaseScreenModel
from libs.decorator import silencer


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.LoginScreen.login_screen.LoginScreenView` class.
    """

    def __init__(self, database):
        super().__init__(database)

    @silencer
    def login(self, email, password, callback):
        self.listener = OnCompleteListener(callback)
        auth = self.db.auth.get_instance()
        auth.signInWithEmailAndPassword(email, password).addOnCompleteListener(self.listener)

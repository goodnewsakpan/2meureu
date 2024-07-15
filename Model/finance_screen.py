from sjfirebase.jinterface import EventListener

from Model.base_model import BaseScreenModel
from libs.decorator import silencer


class FinanceScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.FinanceScreen.finance_screen.FinanceScreenView` class.
    """

    def __init__(self, database):
        super().__init__(database)

    def __android_init__(self):
        self.finance_ref = self.db.firestore.get_db().collection(
            f"parent/{self.db.user.get_current_user().getUid()}/finance"
        )

    @silencer
    def get_upcoming_payments(self, callback):
        self.listener = EventListener(callback)
        (
            self.finance_ref
            .whereEqualTo("status", "pending")
            .addSnapshotListener(self.listener)
        )

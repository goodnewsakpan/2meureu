from sjfirebase.jinterface import EventListener

from Model.base_model import BaseScreenModel
from libs.decorator import silencer


class ActivityScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.ActivityScreen.activity_screen.ActivityScreenView` class.
    """

    def __init__(self, database):
        super().__init__(database)

    def __android_init__(self):
        self.finance_ref = self.db.firestore.get_db().collection(
            f"parent/{self.db.user.get_current_user().getUid()}/activities"
        )

    @silencer
    def get_child_activity(self, callback):
        self.listener = EventListener(callback)
        (
            self.finance_ref
            .addSnapshotListener(self.listener)
        )

from jnius import autoclass

from Controller.base_controller import BaseScreenController
from libs.serialize import serialize_map_to_dict


class ActivityScreenController(BaseScreenController):
    """
    The `ActivityScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def get_child_activity(self):
        self.model.get_child_activity(callback=self.on_get_child_activity)

    def on_get_child_activity(self, snapshot, error):
        Objects = autoclass("java.util.Objects")
        Type = autoclass("com.google.firebase.firestore.DocumentChange$Type")
        if not Objects.isNull(error):
            print(error.getLocalizedMessage())
            return

        for document in snapshot.getDocumentChanges():
            document_type = document.getType().ordinal()
            if document_type == Type.ADDED.ordinal():
                self.view.populate_data(
                    serialize_map_to_dict(
                        document.getDocument().getData()
                    )
                )


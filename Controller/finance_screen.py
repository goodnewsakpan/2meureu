from jnius import autoclass

from Controller.base_controller import BaseScreenController
import requests
from libs.serialize import serialize_map_to_dict


class FinanceScreenController(BaseScreenController):
    """
    The `FinanceScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, app, model):
        super().__init__(app, model)
        self.document_count = 0

    def get_upcoming_payments(self):
        self.model.get_upcoming_payments(callback=self.on_get_upcoming_payments)

    def on_get_upcoming_payments(self, snapshot, error):
        Objects = autoclass("java.util.Objects")
        Type = autoclass("com.google.firebase.firestore.DocumentChange$Type")
        if not Objects.isNull(error):
            print(error.getLocalizedMessage())
            return

        for document in snapshot.getDocumentChanges():
            document_type = document.getType().ordinal()
            if document_type == Type.ADDED.ordinal():
                if self.document_count == 0:
                    self.view.populate_card(
                        serialize_map_to_dict(
                            document.getDocument().getData()
                        )
                    )
                    self.document_count += 1
                    continue
                self.view.populate_data(
                    serialize_map_to_dict(
                        document.getDocument().getData()
                    )
                )

    @staticmethod
    def initiate_payment(data):
        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": "Bearer sk_test_2321d12ff13018949c07a82089cfc1cef287d3ee",
            "Content-Type": "application/json"
        }
        # Make the POST request
        response = requests.post(url, headers=headers, json=data)
        print(response.json())
        return response.json()["data"]["access_code"]

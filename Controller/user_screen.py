from Controller.base_controller import BaseScreenController


class UserScreenController(BaseScreenController):
    """
    The `UserScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def submit_user_details(self, name, phone_number):
        self.model.submit_user_details(name, phone_number, callback=self.on_submit_user_details_complete)

    def on_submit_user_details_complete(self, task):
        if task.isSuccessful():
            self.view.switch_screen("finance screen")
        else:
            self.view.toast(task.getException().getLocalizedMessage())

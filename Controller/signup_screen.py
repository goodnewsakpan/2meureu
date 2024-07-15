from Controller.base_controller import BaseScreenController


class SignupScreenController(BaseScreenController):
    """
    The `SignupScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def account_signup(self, email, password):
        self.model.signup(email, password, callback=self.on_complete)

    def on_complete(self, task):
        if task.isSuccessful():
            self.view.switch_screen("user screen")
        else:
            self.view.toast(task.getException().getLocalizedMessage())
        self.model.gc_listener()

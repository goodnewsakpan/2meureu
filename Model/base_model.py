# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.
from sjfirebase.jinterface import OnCompleteListener

from libs.decorator import silencer, android_only


class BaseScreenModel:
    """Implements a base class for model modules."""

    _observers = []

    def __init__(self, database):
        self.db = database
        self.listener = None
        self.__do_android_init__()

    @android_only
    def __do_android_init__(self):
        self.__android_init__()

    def __android_init__(self):
        pass

    def gc_listener(self):
        self.listener = None

    def send_email_verification(self, *_):
        user = self.db.user.get_current_user()
        user.reload()
        user.sendEmailVerification()

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, name_screen: str, *args, **kwargs) -> None:
        """
        Method that will be called by the observer when the model data changes.

        :param name_screen:
            name of the view for which the method should be called
            :meth:`model_is_changed`.
        """

        for observer in self._observers:
            if observer.name == name_screen:
                observer.model_is_changed(*args, **kwargs)
                break

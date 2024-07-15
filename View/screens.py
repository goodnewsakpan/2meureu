# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.payment_screen import PaymentScreenModel
from Controller.payment_screen import PaymentScreenController
from View.PaymentScreen.payment_screen import PaymentScreenView
from Model.finance_screen import FinanceScreenModel
from Controller.finance_screen import FinanceScreenController
from View.FinanceScreen.finance_screen import FinanceScreenView
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from View.LoginScreen.login_screen import LoginScreenView
from Model.signup_screen import SignupScreenModel
from Controller.signup_screen import SignupScreenController
from View.SignupScreen.signup_screen import SignupScreenView
from Model.activity_screen import ActivityScreenModel
from Controller.activity_screen import ActivityScreenController
from View.ActivityScreen.activity_screen import ActivityScreenView
from Model.assessment_screen import AssessmentScreenModel
from Controller.assessment_screen import AssessmentScreenController
from View.AssessmentScreen.assessment_screen import AssessmentScreenView
from Model.user_screen import UserScreenModel
from Controller.user_screen import UserScreenController
from View.UserScreen.user_screen import UserScreenView

screens = {
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
        'view': LoginScreenView,
        'kv': "./View/LoginScreen/login_screen.kv"
    },

    'user screen': {
        'model': UserScreenModel,
        'controller': UserScreenController,
        'view': UserScreenView,
        'kv': "./View/UserScreen/user_screen.kv"
    },

    'payment screen': {
        'model': PaymentScreenModel,
        'controller': PaymentScreenController,
        'view': PaymentScreenView,
        'kv': "./View/PaymentScreen/payment_screen.kv"
    },

    'activity screen': {
        'model': ActivityScreenModel,
        'controller': ActivityScreenController,
        'view': ActivityScreenView,
        'kv': "./View/ActivityScreen/activity_screen.kv"
    },

    'finance screen': {
        'model': FinanceScreenModel,
        'controller': FinanceScreenController,
        'view': FinanceScreenView,
        'kv': "./View/FinanceScreen/finance_screen.kv"
    },

    'signup screen': {
        'model': SignupScreenModel,
        'controller': SignupScreenController,
        'view': SignupScreenView,
        'kv': "./View/SignupScreen/signup_screen.kv"
    },

    'assessment screen': {
        'model': AssessmentScreenModel,
        'controller': AssessmentScreenController,
        'view': AssessmentScreenView,
        'kv': "./View/AssessmentScreen/assessment_screen.kv"
    },

}

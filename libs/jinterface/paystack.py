from jnius import PythonJavaClass, java_method


class PaystackSheetResultCallback(PythonJavaClass):
    __javacontext__ = "app"
    __javainterfaces__ = ["org/kivy/paystack/PaystackSheetResultCallback"]

    def __init__(self, on_cancelled, on_failed, on_completed):
        self.on_cancelled_callback = on_cancelled
        self.on_failed_callback = on_failed
        self.on_completed_callback = on_completed

    @java_method("(Lcom/paystack/android/ui/paymentsheet/PaymentSheetResult$Cancelled;)V")
    def on_cancelled(self, cancelled):
        self.on_cancelled_callback(cancelled)

    @java_method("(Lcom/paystack/android/ui/paymentsheet/PaymentSheetResult$Failed;)V")
    def on_failed(self, failed):
        self.on_failed_callback(failed)

    @java_method("(Lcom/paystack/android/ui/paymentsheet/PaymentSheetResult$Completed;)V")
    def on_completed(self, completed):
        self.on_completed_callback(completed)

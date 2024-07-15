package org.kivy.paystack;

import com.paystack.android.ui.paymentsheet.PaymentSheetResult;

public interface PaystackSheetResultCallback {
    public void on_cancelled(PaymentSheetResult.Cancelled cancelled);
    public void on_failed(PaymentSheetResult.Failed failed);
    public void on_completed(PaymentSheetResult.Completed completed);
}
package org.kivy.paystack;

import com.paystack.android.core.Paystack;
import com.paystack.android.ui.paymentsheet.PaymentSheet;
import com.paystack.android.ui.paymentsheet.PaymentSheetResult;
import org.kivy.android.PythonActivity;
import android.util.Log;


public class PaystackKivy {
    private static PaymentSheet paymentSheet;
    private static PythonActivity activity;
    private static PaystackSheetResultCallback callback;

    public static void set_public_key(String key) {
        activity = PythonActivity.mActivity;
        Paystack.builder()
        .setPublicKey(key)
        .setLoggingEnabled(true)
        .build();

        paymentSheet = new PaymentSheet(activity, PaystackKivy::payment_complete);
    }

    public static void make_payment(String access_code, PaystackSheetResultCallback callback_wrapper) {
        // Pass access_code from transaction initialize call
        PythonActivity activity = PythonActivity.mActivity;
        activity.launch_paystack_sheet(access_code, callback_wrapper);
    }

    private static void payment_complete(PaymentSheetResult paymentSheetResult) {
        String message;
        Log.d("Cumming", "payment completed .............................");
//         Log.d("Cumming", paymentSheetResult);

        if (paymentSheetResult instanceof PaymentSheetResult.Cancelled) {
            message = "Cancelled";
            callback.on_cancelled((PaymentSheetResult.Cancelled) paymentSheetResult);
        } else if (paymentSheetResult instanceof PaymentSheetResult.Failed) {
            PaymentSheetResult.Failed failedResult = (PaymentSheetResult.Failed) paymentSheetResult;
            callback.on_failed(failedResult);
            Log.e("Payment failed", failedResult.getError().getMessage() != null ?
                    failedResult.getError().getMessage() : "Failed", failedResult.getError());
            message = failedResult.getError().getMessage() != null ?
                    failedResult.getError().getMessage() : "Failed";
        } else if (paymentSheetResult instanceof PaymentSheetResult.Completed) {
            callback.on_completed((PaymentSheetResult.Completed) paymentSheetResult);
            Log.d("Payment successful", ((PaymentSheetResult.Completed) paymentSheetResult).getPaymentCompletionDetails().toString());
            message = "Successful";
        } else {
            message = "You shouldn't be here";
        }
    }
}
def validate_payment(payment):
    assert payment["amount"] > 0, "Insufficient amount"
    assert payment["status"] == "SUCCESS", "Payment failed"


payments = [
    {
        "amount": 100,
        "status": "SUCCESS"
    },
    {
        "amount": 200,
        "status": "SUCCESS"
    },
    {
        "amount": 10,
        "status": "SUCCESS"
    }
]

for payment in payments:
    validate_payment(payment)
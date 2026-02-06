def validate_payment(payment):
    assert payment["amount"] > 0, "Amount must be positive"
    assert payment["status"] == "SUCCESS", "Status must be SUCCESS"
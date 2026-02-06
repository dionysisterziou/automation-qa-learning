import pytest

def validate_payment(payment):
    assert payment["amount"] > 0, "Payment should be positive"
    assert payment["status"] == "SUCCESS", "Status must be SUCCESS"

@pytest.mark.parametrize("payment, should_pass", [
    ({"amount": 10, "status": "SUCCESS"}, True),
    ({"amount": 0, "status": "SUCCESS"}, False),
    ({"amount": 20, "status": "SUCCESS"}, True),
    ({"amount": 30, "status": "FAILED"}, False)
])
def test_payment_validation(payment, should_pass):
    if should_pass:
        validate_payment(payment)
    else:
        with pytest.raises(AssertionError):
            validate_payment(payment)
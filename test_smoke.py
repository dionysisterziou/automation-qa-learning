import pytest


# Μάθημα 10 - Πολλά pytest tests (σωστή δομή)
# def test_payment_success():
#     status = "SUCCESS"
#     assert status == "SUCCESS"


# def test_payment_failed():
#     status = "FAILED"
#     assert status == "FAILED"


# def test_payment_amount_positive():
#     amount = 100
#     assert amount > 0

# Μάθημα 11 - Reuse business rules με functions μέσα σε pytest
# def validate_payment(payment):
#     assert payment["amount"] > 0, "Amount must be positive"
#     assert payment["status"] == "SUCCESS", "Status must be SUCCESS"


# def test_payment_ok():
#     payment = {"amount": 100, "status": "SUCCESS"}
#     validate_payment(payment)


# def test_payment_zero_amount_fails():
#     payment = {"amount": 0, "status": "SUCCESS"}
#     with pytest.raises(AssertionError):
#         validate_payment(payment)


# Μάθημα 14 - @pytest.mark.parametrize
def validate_payment(payment):
    assert payment["amount"] > 0, "Amount must be positive"
    assert payment["status"] == "SUCCESS", "Status must be SUCCESS"


@pytest.mark.parametrize("payment", [{"amount": 1, "status": "SUCCESS"}, {"amount": 50, "status": "SUCCESS"}, {"amount": 999, "status": "SUCCESS"}])
def test_valid_payments(payment):
    validate_payment(payment)
import pytest

def validate_payment_response(resp):
    assert resp["status"] == "SUCCESS", "API status should be SUCCESS"
    assert resp["data"]["amount"] > 0, "Amount must be positive"
    assert resp["data"]["currency"] == "EUR", "Currency must be EUR"


def test_payment_response_ok():
    response = {
        "status": "SUCCESS",
        "data": {
            "id": "p_123",
            "amount": 100,
            "currency": "EUR"
        }
    }

    validate_payment_response(response)


def test_payment_response_invalid_amount_should_fail():
    response = {
        "status": "SUCCESS",
        "data": {
            "id": "p_123",
            "amount": 0,
            "currency": "EUR"
        }
    }

    with pytest.raises(AssertionError):
        validate_payment_response(response)


def test_payment_response_missing_currency_should_fail():
    response = {
        "status": "SUCCESS",
        "data": {
            "id": "p_123",
            "amount": 10
        }
    }

    with pytest.raises(KeyError):
        validate_payment_response(response)
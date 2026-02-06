import pytest


def validate_transactions(resp):
    assert resp["status"] == "SUCCESS", "API status should be SUCCESS"

    for tx in resp["transactions"]:
        assert tx["amount"] > 0, "Transaction amount must be positive"


def test_transactions_ok():
    response = {
        "status": "SUCCESS",
        "transactions": [
            {"id": "t1", "amount": 10},
            {"id": "t2", "amount": 20},
        ]
    }

    validate_transactions(response)


def test_transactions_fail():
    response = {
        "status": "SUCCESS",
        "transactions": [
            {"id": "t1", "amount": 0}
        ]
    }

    with pytest.raises(AssertionError):
        validate_transactions(response)
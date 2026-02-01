import pytest


def validate_transactions_strict(resp):
    assert resp["status"] == "SUCCESS", "API status should be SUCCESS"

    for tx in resp["transactions"]:
        assert tx["amount"] > 0, f"Invalid transaction amount: {tx['amount']}"


def test_transactions_all_valid():
    response = {
        "status": "SUCCESS",
        "transactions": [
            {"id": "t1", "amount": 10},
            {"id": "t2", "amount": 20},
        ]
    }

    validate_transactions_strict(response)


def test_transactions_invalid():
    response = {
        "status": "SUCCESS",
        "transactions": [
            {"id": "t1", "amount": 30},
            {"id": "t2", "amount": 24},
            {"id": "t3", "amount": 0}
        ]
    }

    with pytest.raises(AssertionError):
        validate_transactions_strict(response)
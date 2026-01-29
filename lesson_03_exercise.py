balance = 100
withdraw_amount = 40

if balance >= withdraw_amount:
    status = "SUCCESS"
else:
    status = "FAILED"


assert status == "SUCCESS", "Withdrawal should succeed when balance is sufficient"
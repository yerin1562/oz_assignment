class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.type = type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:
        return f"{self.type}: {self.amount}원, 잔고: {self.balance}원"

    def to_tuple(self) -> tuple:
        return self.type, self.amount, self.balance

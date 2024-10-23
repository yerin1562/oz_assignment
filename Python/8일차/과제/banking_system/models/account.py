from banking_system.models.transaction import Transaction
from banking_system.utils.decorators import validate_transaction
from banking_system.utils.exceptions import InsufficientFundsError, NegativeAmountError


class Account:
    bank_name = "MyBank"

    def __init__(self, __balance: int, transaction: str) -> None:
        self.__balance = __balance
        self.transaction = transaction

    @validate_transaction
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        self.__balance += amount
        self.transaction.append(Transaction("입금", amount, self.__balance))

    @validate_transaction
    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance)
        self.__balance -= amount
        self.transaction.append(Transaction("출금", amount, self.__balance))

    def get_balance(self) -> int:
        return self.__balance

    def get_transaction(self) -> list:
        return self.transaction

    @classmethod
    def get_bank_name(self) -> str:
        return cls.bank_name

    @classmethod
    def set_bank_name(self, name: str) -> None:
        cls.bank_name = name



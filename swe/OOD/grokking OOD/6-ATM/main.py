from enum import Enum

class TransactionType(Enum):
    BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSIT_CHECK, WITHDRAW, TRANSFER = 1, 2, 3, 4, 5

class TransactionStatus(Enum):
    SUCCESS, FAILURE, BLOCKED, FULL, PARTIAL, NONE = 1, 2, 3, 4, 5, 6

class CustomerStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, CLOSED, UNKNOWN = 1, 2, 3, 4, 5, 6, 7

class Address:
    def __init__(self, street) -> None:
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

# Customer, Card, and Account: “Customer” encapsulates the ATM user, “Card” the ATM card, and “Account” can be of two types: checking and savings:

# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.

class Customer:
    def __init__(self, name, address, emails, phone, status) -> None:
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__card = Card()
        self.__account = Account

    def make_transaction(self, transaction):
        None

    def get_billing_address(self):
        None

class Account:
    def __init__(self, number, customer_name, expiry, pin)):
        self.__account_number = number
        self.__customer_name = customer_name
        self.__card_expiry = expiry
        self.__pin = pin
    def get_billing_address(self):
        None

class Account:
    def __init__(self, account_number) -> None:
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0
    
    def get_available_balance(self):
        return self.__available_balance

class SavingAccount(Account):
    def __init__(self, debit_card_number) -> None:
        self.__debit_card_number = debit_card_number

# Bank, ATM, CashDispenser, Keypad, Screen, Printer and DepositSlot: The ATM will have different components like keypad, screen, etc.
from abc import ABC

class Bank:
    def __init__(self, name, bank_code) -> None:
        self.__name = name
        self.__bank_code = bank_code
    
    def get_bank_code(self):
        return self.__bank_code
    def add_atm(self, atm):
        None

class ATM:
    def __init__(self, id, location):
        self.__atm_id = id
        self.__location = location
        self.__cash_dispenser = CashDispenser()
        self.__keypad = Keypad()
        self.__screen = Screen()
        self.__printer = Printer()
        self.__deposit_slot = CheckDeposit()
        self.__cash_deposit = CashDeposit
    
    def authenticate_user(self):
        None
    def make_transaction(self, customer, transaction):
        None

class CashDispenser:
    def __init__(self) -> None:
        self.__total_five_dollar_bills = 0
        self.__total_twenty_dollar_bills = 0
    def dispense_cash(self, amount):
        None
    def can_dispense_cash(self):
        None

class Keypad:
    def get_input(self):
        None

class Screen:
    def show_message(self, message):
        None
    def get_input(self):
        None

class Printer:
    def print_receipt(self, transaction):
        None

class CashDeposit:
    def __init__(self) -> None:
        pass

class DepositSlot(ABC):
    def __init__(self) -> None:
        self.__total_amount = 0.0

    def get_total_amount(self):
        return self.__total_amount

class CheckDepositSlot(DepositSlot):
    def get_check_amount(self):
        None

class CashDepositSlot(DepositSlot):
    def receive_dollar_bill(self):
        None

# Transaction and its subclasses: Customers can perform different transactions on the ATM, these classes encapsulate them:

from abc import ABC

class Transaction(ABC):
    def __init__(self, id, creation_date, status) -> None:
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status
    
    def make_transaction(self):
        None

class BalanceInquiry(Transaction):
    def __init__(self, id, creation_date, status) -> None:
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status
    def make_transaction(self):
        None
    
class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id
    def get_account_id(self):
        return self.__account_id

class Deposit(Transaction):
    def __init__(self, amount):
        self.__amount = amount
    def get_amount(self):
        return self.__amount

class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self.__check_number = check_number
        self.__bank_code = bank_code
    def get_check_number(self):
        return self.__check_number

class CashDeposit(Deposit):
    def __init__(self, cash_deposit_limit):
        self.__cash_deposit_limit = cash_deposit_limit

class Withdraw(Transaction):
    def __init__(self, amount):
        self.__amount = amount
    def get_amount(self):
        return self.__amount

class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self.__destination_account_number = destination_account_number
    def get_destination_account_number(self):
        return self.__destination_account_number
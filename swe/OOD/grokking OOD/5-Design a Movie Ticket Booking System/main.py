from enum import Enum

class BookingStatus(Enum):
    REQUESTED, PENDING, CONFIRMED, CHECK_IN, CNANCELLATION_REQUESTED, CANCELLED, CHECK_OUT = 1, 2, 3, 4, 5, 6, 7
class SeatType(Enum):
    REGULAR, PREMIUM, ACCESSIBLE, EMERGENCY_EXIT = 1, 2, 3, 4

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

# Account, Customer, Admin, FrontDeskOfficer, and Guest: These classes represent the different people that interact with our system:
from abc import ABC
from .constants import AccountStatus

# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.

class Account:
    def __init__(self, id, password, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status
    def reset_pass(self):
        None

from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account
class Customer(Person):
    def make_booking(self, booking):
        None
    def get_booking(self):
        None

class Admin(Person):
    def add_movie(self, movie):
        None
    def add_show(self, show):
        None
    def block_user(self, customer):
        None

class FrontDeskOfficer(Person):
    def create_booking(self, booking):
        None
class Guest:
    def register_account(self):
        None

# Show and Movie: A movie will have many shows:
from datetime import datetime

class Show:
    def __init__(self, id, played_at, movie, start_time, end_time) -> None:
        self.__show_id = id
        self.__created_on = datetime.date.today()
        self.__start_time = start_time

        self.__end_time = end_time
        self.__played_at = played_at
        self.__movie = movie

class Movie:
    def __init__(self, title, description, duration_in_mins, language, release_date, country, genre, added_by):
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__country = country
        self.__genre = genre
        self.__movie_added_by = added_by
        self.__shows = []
    def get_shows(self):
        None

# Booking, ShowSeat, and Payment: Customers will reserve seats with a booking and make a payment:
from datetime import datetime
from .cinema import CinemaHallSeat

class Booking:
    def __init__(self, booking_number, number_of_seats, status)
        self.__booking_number = booking_number
        self.__created_on = datetime.date.today()
        self.__number_of_seats = number_of_seats
        self.__status = status
        self.__payment = None
        self.__show_seats = []
    
    def make_payment(self, payment):
        None
    def cancel(self):
        None
    def get_seats(self, seats):
        None

class ShowSeat:
    def __init__(self, id, is_reserved, price):
        self.__show_seat_id = id
        self.__is_reserved = is_reserved
        self.__price = price

class Payment:
    def __init__(self, amount, transaction_id, payment_status):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status

# City, Cinema, CinemaHall and CinemaHallSeat: Each city can have many cinemas and each cinema can have many cinema halls:

class City:
    def __init__(self, name, state, zip_code):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code
class Cinema:
    def __init__(self, name, total_cinema_halls, address, halls):
        self.__name = name
        self.__total_cinema_halls = total_cinema_halls
        self.__location = address
        self.__halls = halls

class CinemaHall:
    def __init__(self, name, total_seats, seats, shows):
        self.__name = name
        self.__total_seats = total_seats
        self.__seats = seats
        self.__shows = shows

class CinemaHallSeat:
    def __init__(self, id, seat_type):
        self.__hall_seat_id = id
        self.__seat_type = seat_type

# Search interface and Catalog: Catalog will implement Search to facilitate searching of products.
from abc import ABC

class Search(ABC):
    def search_by_title(self, title):
        None
    def search_by_genre(self, genre):
        None
    def search_by_language(self, language):
        None
    def search_by_release_date(self, rel_date):
        None
    def search_by_city(self, city_name):
        None

class Catalog(Search):
    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

        def search_by_title(self, title):
            return self.__movie_titles.get(title)
       
            
        def search_by_language(self, language):
            return self.__movie_languages.get(language)
        def search_by_city(self, city_name):
            return self.__movie_cities.get(city_name)

# Concurrency
# How to handle concurrency; such that no two users are able to book the same seat?

# We can use transactions in SQL databases to avoid any clashes. For example, if we are using SQL server we can utilize Transaction Isolation Levels to lock the rows before we update them. Note: within a transaction, if we read rows we get a write-lock on them so that they can’t be updated by anyone else. Here is the sample code:
```sql
set transactions isolation level serializable;
begin transaction;

    -- suppose we intend to reverse three seats(IDs: 54, 55, 56) for showID = 99
    select * from showseat where showID = 99 && ShowSeatID in (54, 55, 56) && isReserved = 0

    -- if the number of rows returned by the above statement is NOT three, then we can return failture for user
    update ShowSeat table ...
    update Booking table ...
commit transactions;
```

# 'Serializable' 是最高的隔离级别，可确保免受Dirty、Nonrepeatable和Phantoms读取的安全性。

# 一旦上述数据库事务成功，我们可以安全地假设预订已成功标记，并且没有两个客户能够预订同一个座位。

# 有关详细信息，请阅读JDBC 事务隔离级别。
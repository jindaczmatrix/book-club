from enum import Enum

class QuestionStatus(Enum):
    OPEN, CLOSED, ON_HOLD, DELETED = 1, 2, 3, 4

class QuestionClosingRemark(Enum):
    DUPLICATE, OFF_TOPIC, TOO_BROAD, NOT_CONSTRUCTIVE, NOT_A_REAL_QUESTION, PRIMIARY_OPINION_BASED = 1, 2, 3, 4, 5, 6

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1,2,3,4,5

# Account, Member, Admin, and Moderator: These classes represent the different people that interact with our system:
from .constants import *

# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.

class Account:
    def __init__(self, id, password, name, address, email, phone, status=AccountStatus.Active) -> None:
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__reputation = 0
    
    def reset_password(self):
        None

class Member:
    def __init__(self, account) -> None:
        self.__account = account
        self.__badges = []
    def get_reputation(self):
        return self.__account.get_reputation()
    def get_email(self):
        return self.__account.get_email()
    def create_question(self, question):
        None
    def create_tag(self, tag):
        None

class Admin(Member):
    def block_member(self, member):
        None
    def unblock_member(self, member):
        None

class Moderator(Member):
    def close_question(self, question):
        None
    def undelete_question(self, question):
        None

# Badge, Tag, and Notification: Members have badges, questions have tags and notifications:
from datetime import datetime

class Badge:
    def __init__(self, name, description) -> None:
        self.__name = name
        self.__description = description
class Tag:
    def __init__(self, name, description) -> None:
        self.__name = name
        self.__description = description
        self.__daily_asked_frequency = 0
        self.__weekly_asked_frequency = 0
    def send_notification(self):
        None

# Photo and Bounty: Members can put bounties on questions. Answers and Questions can have multiple photos:
from datetime import datetime

class Photo:
    def __init__(self, id, path, member) -> None:
        self.__id = id
        self.__path = path
        self.__creation_date = datetime.now()
        self.creating_member = member
    def delete(self):
        None

class Bounty:
    def __init__(self, reputation, expiry) -> None:
        self.__reputation = reputation
        self.__expiry = expiry
    def modify_reputation(self, reputation):
        None

# Question, Comment and Answer: Members can ask questions, as well as add an answer to any question. All members can add comments to all open questions or answers:
from datetime import datetime
from abc import ABC
from .constants import *

class Search(ABC):
    def search(self, query):
        None

class Question(Search):
    def __init__(self, title, description, bounty, asking_member) -> None:
        self.__title = title
        self.__description = description
        self.__view_count = 0
        self.__vote_count = 0
        self.__creation_time = datetime.now()
        self.__update_time = datetime.now()
        self.__status = QuestionStatus.OPEN
        self.__closing_remark = QuestionClosingRemark.DUPLICATE

        self.__bounty = bounty
        self.__asking_member = asking_member
        self.__photos = []
        self.__comments = []
        self.__answers = []

    def close(self):
        None
    def undelete(self):
        None
    def add_comment(self, comment):
        None
    def add_bounty(self, bounty):
        None
    def search(self, query):
         # return all questions containing the string query in their title or description.
         None
class Comment:
    def __init__(self, text, member) -> None:
        self.__text = text
        self.__creation_time = datetime.now()
        self.__flag_count = 0
        self.__vote_count = 0
        self.__asking_member = member
    def increment_vote_count(self):
        None

class Answer:
    def __init__(self, text, member) -> None:
        self.__answer_text = text
        self.__accepted = False
        self.__vote_count = 0
        self.__flag_count = 0
        self.__creation_time = datetime.now()
        self.__creating_member = member
        self.__photos = []
    def increment_vote_count(self):
        None
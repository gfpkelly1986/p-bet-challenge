"""
An application to update customer files with correct updates and update Google sheets if needed.
"""
import gspread
import json
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Customer Updates')

# data before deserialisation class = <class '_io.TextIOWrapper'>
data = open('forwarder_updates.json',)

# # data after deserialisation <class 'list'>
with open('forwarder_updates.json', 'r') as updates:
    data = json.load(updates)


class Customer_Update:
    def __init__(self, data):
        self.data = data

class FunBet(Customer_Update):
    def __init__(self, data):
        super().__init__(self, data)

    def filter_list(data):
        list1 = []
        for values in data:
            for value in values:
                if values[value] == 'Core':
                    list1.append(values)
        fun_bet = open('funbet.json', 'w')
        json.dump(list1, fun_bet, indent = 4)

class CrazyBet(Customer_Update):
    def __init__(self, data):
        super().__init__(self, data)

    def filter_list(data):
        list2 = []
        for values in data:
            for value in values:
                if values[value] == 'SerieA':
                    list2.append(values)
        fun_bet = open('crazybet.json', 'w')
        json.dump(list2, fun_bet, indent = 4)


class LuckyBet(Customer_Update):
    def __init__(self, data):
        super().__init__(self, data)

    def filter_list(data):
        list3 = []
        for values in data:
            for value in values:
                if value == 'Probability' and values[value] > 0.25:
                    list3.append(values)
        fun_bet = open('luckybet.json', 'w')
        json.dump(list3, fun_bet, indent = 4)

        
FunBet.filter_list(data)
CrazyBet.filter_list(data)
LuckyBet.filter_list(data)








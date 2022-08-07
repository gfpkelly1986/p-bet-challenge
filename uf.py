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

print(type(data))

# # data after deserialisation <class 'list'>
with open('forwarder_updates.json', 'r') as updates:
    data = json.load(updates)

print(type(data))


def fun_bet_customer_update(data):
    """
    This function will filter the data for key values equal to 'Core'
    It returns a list of the filtered data.
    """
    list1 = []
    for values in data:
        for value in values:
            if values[value] == 'Core':
                list1.append(values)
    return (list1)


def crazy_bet_customer_update(data):
    """
    This function will filter the data for key values equal to 'SerieA'
    It returns a list of the filtered data.
    """
    list2 = []
    for values in data:
        for value in values:
            if values[value] == 'SerieA':
                list2.append(values)
    return (list2)



returned_list_fun_bet = fun_bet_customer_update(data)
fun_bet = open('funbet.json', 'w')
json.dump(returned_list_fun_bet, fun_bet, indent = 4)

returned_list_crazy_bet = crazy_bet_customer_update(data)
crazy_bet = open('crazybet.json', 'w')
json.dump(returned_list_crazy_bet, crazy_bet, indent = 4)







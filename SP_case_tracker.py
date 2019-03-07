# import some helpful libraries/classes/global variables
import numpy as np

# defining classes that may be needed
class CASE:
    def __init__(self, case_num, year, main_organ):
        self.case_num = case_num
        self.year = year
        self.main_organ = main_organ

# installing needed libraries and enabling API with credentials JSON file from google (renamed to 'credentials.json')
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# talking and opening the google sheet
client = gspread.authorize(credentials)
sheet = client.open('SP_Case_Tracker').sheet1
old_data_all = sheet.get_all_values()
data = sheet.get_all_records()

# start a case building building session


def create_case():
    case_num = input("Enter a case number: ")
    while case_num.isalpha() or case_num == '' or case_num.__contains__(' '):
        case_num = input("Whoops, please enter a number: ")
    year = input("Enter the year of case: ")
    while year.isalpha() or year == '' or year.__contains__(' '):
        year = input("Whoops, please enter a numerical year: ")
    yr = int(year)
    while 1900 > yr or yr > 2020 or yr == '':
        year = input("Whoops, please enter a year between 1900 and 2019: ")
        yr = int(year)
    organ = True
    main_organ = input("Enter the main organ of case: ")
    while organ:
        if main_organ.isnumeric():
            main_organ = input("I am sorry, please enter an organ without numbers: ")
        elif main_organ.__contains__(' '):
            main_organ = input("Please only enter one main organ without spaces: ")
        elif main_organ == '':
            main_organ = input("You must enter a main organ: ")
        else:
            organ = False
    case_att.extend((case_num, year, main_organ))
    return


while True:
    add_case = str(input("Would you like to add a case? (y/n): ").lower())
    if add_case == "y":
        print("\n---YOU WILL NOW ADD A NEW CASE---\n")
        case_att = []  # list needed for create_case function
        create_case()
        sheet.append_row(case_att)
        input("Press enter to continue...")
    elif add_case == "n":
        print("Sounds, good. Closing...")
        break
    else:
        print("I'm sorry I did not understand... try again.")


# reporting what happened this session
new_data_all = sheet.get_all_values()
rows_added = len(new_data_all) - len(old_data_all)
print(new_data_all)
print(f"{rows_added} rows were added this session.")


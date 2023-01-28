from Google import Create_Service
import csv

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CLIENT_SECRET = "credentials.json"
API_NAME = "sheets"
API_VERSION = "v4"

spreadsheet_id = '' # Your spreadsheet id here

def create_service():
    service = Create_Service(CLIENT_SECRET, API_NAME,API_VERSION, SCOPES)
    return service


def upload(service, csv_file, sheet_name = "Sheet1"):
    f = open(csv_file, "r")
    values = [r for r in csv.reader(f)]
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=sheet_name, valueInputOption="USER_ENTERED", body={"values": values}).execute()
        

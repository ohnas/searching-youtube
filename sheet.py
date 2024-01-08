import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SAMPLE_SPREADSHEET_ID = "161aGJr6OlTMdcYddEtBGKIc8PHQp3jXyC32w6KnwTA8"


def authorize_credentials():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def get_last_row():
    creds = authorize_credentials()
    service = build("sheets", "v4", credentials=creds)
    range_name = "test"

    # Google Sheet에서 값 읽기
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_name)
        .execute()
    )
    values = result.get("values", [])

    if not values:
        print("No data found.")
    else:
        last_row = len(values)  # 값이 있는 마지막 행의 번호
        return last_row + 1


def read_value():
    creds = authorize_credentials()
    range_name = "test!A2"
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=range_name,
        )
        .execute()
    )
    values = result.get("values", [])
    if not values:
        print("No data found.")
    else:
        return values[0][0]


def write_values(values):
    creds = authorize_credentials()
    range_name = "test!C:G"
    service = build("sheets", "v4", credentials=creds)
    data = [
        {"range": range_name, "values": values},
    ]
    body = {"valueInputOption": "USER_ENTERED", "data": data}
    result = (
        service.spreadsheets()
        .values()
        .batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=body)
        .execute()
    )
    print(result)

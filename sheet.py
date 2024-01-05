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


def read_value():
    creds = authorize_credentials()
    range_name = "test!A1"
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
        for row in values:
            # A1 셀 값 출력
            print(row[0])


def write_values():
    pass

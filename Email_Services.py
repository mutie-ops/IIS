import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText

# Set up the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

file2 = 'C:\\Users\\HP\\PycharmProjects\\IIS\\data\\credentials\\cred.json'


def authentication():
    global creds
    token_save = "C:\\Users\\HP\\PycharmProjects\\IIS\\\data\\credentials\\token.json"
    if os.path.exists(token_save):
        creds = Credentials.from_authorized_user_file(token_save, SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(file2, SCOPES)
        creds = flow.run_local_server(port=0)

        with open(token_save, 'w') as json_file:
            json_file.write(creds.to_json())


authentication()


def create_message(message, to, subject):
    with build('gmail', 'v1', credentials=creds) as service:
        # Compose the email
        message = MIMEText(message)
        message['to'] = to
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

        # Send the email
        try:
            message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
            print(f"Message sent: {message['id']}")
        except HttpError as error:
            print(f"An error occurred: {error}")

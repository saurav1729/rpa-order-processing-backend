# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# import base64
# import json
# from models.connection import Connection
# from models.email_config import EmailConfig
# from utils.db import db
# from services.uipath_service import process_with_uipath  # Assuming UiPath integration is already done in uipath_service.py

# def get_gmail_service(connection):
#     """Returns an authenticated Gmail service using OAuth credentials."""
#     creds = Credentials.from_authorized_user_info(json.loads(connection.oauth_token), ['https://www.googleapis.com/auth/gmail.modify'])
#     return build('gmail', 'v1', credentials=creds)

# def process_email(data):
#     """Fetches the latest email for a connection and processes it."""
#     connection_id = data.get('connection_id')
#     connection = Connection.query.get(connection_id)
#     if not connection:
#         return {"message": "Invalid connection"}
    
#     service = get_gmail_service(connection)

#     # Fetch the latest email from the inbox
#     results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=1).execute()
#     messages = results.get('messages', [])

#     if not messages:
#         return {"message": "No new emails"}

#     msg = service.users().messages().get(userId='me', id=messages[0]['id']).execute()

#     # Extract email content and headers
#     payload = msg['payload']
#     headers = payload['headers']

#     subject = next(header['value'] for header in headers if header['name'] == 'Subject')
#     sender = next(header['value'] for header in headers if header['name'] == 'From')

#     # Decode the email content
#     if 'parts' in payload:
#         parts = payload['parts']
#         data = parts[0]['body']['data']
#     else:
#         data = payload['body']['data']
    
#     content = base64.urlsafe_b64decode(data).decode('utf-8')

#     # Process the email content with UiPath
#     processed_result = process_with_uipath(connection, subject, sender, content)

#     # Save the email analytics (but not the order details)
#     save_email_analytics(connection, subject, sender, content, processed_result)

#     # Move the email to a processed folder
#     move_email_to_processed_folder(service, msg)

#     return {"message": "Email processed", "subject": subject, "sender": sender, "uipath_result": processed_result}

# def save_email_analytics(connection, subject, sender, content, processed_result):
#     """Saves email analytics to the database."""
#     email_data = {
#         "connection_id": connection.id,
#         "subject": subject,
#         "sender": sender,
#         "content": content,
#         "uipath_result": processed_result,
#         "status": "processed"
#     }

#     # Insert email analytics record into the database
#     new_email = EmailConfig(
#         connection_id=connection.id,
#         order_creation_url=None,  # Don't store order details
#         destination_folder="processed_emails"
#     )
    
#     db.session.add(new_email)
#     db.session.commit()

# def move_email_to_processed_folder(service, msg):
#     """Move the email to a processed folder."""
#     new_labels = {'removeLabelIds': ['INBOX'], 'addLabelIds': ['Label_123']}  # Replace with actual label ID for processed emails
#     service.users().messages().modify(userId='me', id=msg['id'], body=new_labels).execute()

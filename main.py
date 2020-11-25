''' Application that sends special messages to that special someone.'''

# Imports
import smtplib
from email.message import EmailMessage
import random



# *================================* #
# File that contains all messages.
MSGS_PATH = 'GirlfriendNanny\\gf_messages.txt'

# Gmail information of SENDER
MY_GMAIL = ''                           # ENTER YOUR GMAIL
MY_PASSWORD = ''                        # ENTER YOUR GMAIL PASSWORD

# Gmail information of RECEIVER
RECEIVER = ''                           # ENTER RECIEVER GMAIL
# *================================* #


def line_picker():
    with open(MSGS_PATH, 'r', encoding='utf-8') as msgs:
        choice = random.randrange(0, len(msgs.readlines()))
        msgs.close()

    with open(MSGS_PATH, 'r', encoding='utf-8') as msgs:
        return ('\n' + msgs.readlines()[choice])

message = EmailMessage()
message['Subject'] = 'Daily Cute Message :)'
message['From'] = MY_GMAIL
message['To'] = RECEIVER
message['Bcc'] = MY_GMAIL               # <---- Send BLIND copy to yourself

message.set_content(line_picker())

def send_email():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(MY_GMAIL, MY_PASSWORD)
        smtp.send_message(message)
        
    
send_email()
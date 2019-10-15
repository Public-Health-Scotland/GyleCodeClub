'''
Mini-module to house exchangelib-related functions to interact with Outlook
'''

# Standard library imports
import logging
import getpass
from os.path import join
import os

# External library imports
from exchangelib import (DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody,
                         FileAttachment)

log_extra = {'user':getpass.getuser()}
console_log = logging.getLogger('pyalerts_console')
file_log = logging.getLogger('pyalerts_file')

def connect_to_account(email, username, password):
    '''
    Create a connection to an Outlook email account
    '''

    credentials = Credentials(username=username, password=password)

    my_account = Account(primary_smtp_address=email,
                         credentials=credentials,
                         autodiscover=True,
                         access_type=DELEGATE)

    console_log.info("Connected to Outlook account")
    file_log.info("Connected to Outlook account", extra=log_extra)

    return my_account

def generate_email(account, body, recipient, hb):
    '''
    The function gets called for each recipient.
    Emails are saved in the Drafts folder for human review
    '''
    
    m = Message(
        account=account,
        folder=account.drafts,
        subject='Discovery alert',
        body=HTMLBody(body),
        to_recipients=[Mailbox(email_address=recipient)]
    )

    root_path = join(os.getcwd(), 'pyalerts')
    hb_temp_path = join(root_path, "temp", f"temp_{hb}")

    for image_basename in os.listdir(hb_temp_path):

        image_path = join(hb_temp_path, image_basename)

        with open(image_path, 'rb') as f:
            embed_image = FileAttachment(
                name=image_path,
                content_id=os.path.basename(image_path),
                content=f.read(),
                is_inline=True)

        m.attach(embed_image)

    m.save()

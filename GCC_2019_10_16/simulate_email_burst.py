'''
Go through latest_data.csv and email CEO's of each
health board with failing indicators for the latest
available time period.
'''

# Standard library imports
import argparse
import logging
from os.path import exists
import sys
import getpass

# External library imports
import pandas as pd

# pyalerts imports
from pyalerts.html_templating import prepare_html_body
from pyalerts.email_generator import connect_to_account, generate_email
from pyalerts.breach_analysis import identify_breaches
from pyalerts.utils import create_temp_image_dirs, clean_up
from pyalerts.visualisations import generate_viz

def main():
    '''
    Make sure the script runs with two parameters:
    username and password for the Outlook account.

    Logging config is in pyalerts > static
    '''

    log_extra = {'user':getpass.getuser()}
    console_log = logging.getLogger('pyalerts_console')
    file_log = logging.getLogger('pyalerts_file')

    console_log.info("Python imports successful")

    #check if "latest_data.csv" exists
    if not exists("latest_data.csv"):
        console_log.info("Check complete: no new data")
        file_log.info("Check complete: no new data", extra=log_extra)
        sys.exit()

    #if latest_data.csv exists, connect to Outlook and send alerts
    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument('password')

    args = parser.parse_args()

    EMAIL = 'german.priks@nhs.net'
    USERNAME = args.username
    PASSWORD = args.password

    my_account = connect_to_account(EMAIL, USERNAME, PASSWORD)
    
    breaches = identify_breaches()
    contacts = pd.read_excel("contacts.xlsx")

    #create temp directories for embedded images
    create_temp_image_dirs(breaches)

    #create images using Seaborn
    generate_viz(breaches)

    #make sure you're not including boards with no breaches
    total_emails_to_send = len(breaches.keys())

    #temp_refresh_date
    refresh_date = pd.to_datetime(pd.read_csv("latest_data.csv")['Reporting Date'], dayfirst=True).max()

    #breaches is a nested dictionary
    for i, hb in enumerate(breaches.keys()):

        exec_name = contacts[contacts['Board'] == hb]['Name'].values[0]
        exec_email = contacts[contacts['Board'] == hb]['Email'].values[0]
        email_body = prepare_html_body(refresh_date, exec_name, hb, breaches[hb]) 

        generate_email(my_account, email_body, exec_email, hb)

        console_log.info(
            "Alert email saved in Outlook Drafts (%s/%s)",
            i+1, total_emails_to_send)
        break #remove when finished testing

    #clean up and exit
    clean_up()
    file_log.info("Latest_data.csv ingested and deleted", extra=log_extra)
    sys.exit()

if __name__ == "__main__":
    main()

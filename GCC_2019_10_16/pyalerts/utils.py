'''
Mini-module to house miscellaneous functions
'''
# Standard library imports
from os import mkdir, getcwd, remove
from os.path import join
import shutil
import logging

def create_temp_image_dirs(breaches):
    '''
    Create a folder structure like so:
    |--...
    |--pyalerts
    |  |--temp
    |  |  |--temp_%board_name%
    |  |  |  |  |--temp_image_boxplot.png
    |  |  |  |  |--temp_image_timetrend.png
    '''
    #because the function is called by simulate_email_burst, the 
    #working directory is dev_alerts folder

    console_log = logging.getLogger('pyalerts_console')

    root_path = join(getcwd(), 'pyalerts')
    
    mkdir(join(root_path, 'temp'))

    for hb in breaches.keys():
        mkdir(join(root_path, 'temp', f'temp_{hb}'))

    console_log.info("Temporary image folders created")

def clean_up():
    '''
    Remove latest_data.csv and the temp image files
    '''

    console_log = logging.getLogger('pyalerts_console')
    
    root_path = getcwd()
    remove(join(root_path, "latest_data.csv"))
    shutil.rmtree(join(root_path, "pyalerts", "temp"))

    console_log.info("Clean-up complete")

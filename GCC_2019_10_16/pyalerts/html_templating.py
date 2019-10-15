'''
Mini-module to house Jinja2-related functions to generate HTML email body
'''

# Standard library imports
import os
import logging
from io import StringIO

# External library imports
from jinja2 import Environment, FileSystemLoader

console_log = logging.getLogger('pyalerts_console')
file_log = logging.getLogger('pyalerts_file')

def prepare_html_body(refresh_date, exec_name, board, breaches):
    '''
    Use Jinja templating engine to dynamically
    create pretty HTML emails
    '''

    env = Environment(loader=FileSystemLoader(os.getcwd()))
        
    template = env.get_template(r"pyalerts/static/letter_template.jinja")

    output = StringIO()

    template.stream(
        refresh_date=refresh_date,
        exec_name=exec_name,
        board=board,
        breaches=breaches
        ).dump(output)

    return output.getvalue()

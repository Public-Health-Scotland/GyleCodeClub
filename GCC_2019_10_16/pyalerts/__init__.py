'''
__init__ file to identify the folder as a package and setup logging
Note that we're setting root logger to WARNING as some imported libraries
will have their own logging and will print INFO to root.
'''
import logging.config
import sys

logging.config.fileConfig('pyalerts/static/logging.conf')

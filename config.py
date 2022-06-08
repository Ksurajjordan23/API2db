import requests
import json
import os
import webbrowser
import httplib2
import urllib.request
import psycopg2
import sys
import psycopg2.extensions
from dotenv import load_dotenv

import os
load_dotenv()

DATABASES= {
        'Engine' : 'psycopg2',
        'Host' : os.getenv("Database_host"),
        'User' : os.getenv("Database_user"),
        'Password' : os.getenv("Database_pwd"),
        'Name' : os.getenv("Database_Name"),
        'Port' : os.getenv("Database_port")
}

access_key = os.getenv("apikey")

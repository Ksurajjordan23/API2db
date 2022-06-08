import requests
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

class JsonPlaceHolderAPI:
    def get(self, id):
        url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(id)
        results = requests.get(url)
        return results.json

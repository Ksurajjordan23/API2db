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
from models import JsonData

from models import JsonData

class CreateRecord():
    def posts(self, **kwargs):
        posts.create(
        user_id = kwargs['userId'],
        id = kwargs['id'],
        title = kwargs['title'],
        body= kwargs['body'])

class UpdateRecord():
    def posts(self):
        pass
class DeleteRecord():
    def posts(self):
        pass
class ReadRecord():
    def posts(self):
        pass

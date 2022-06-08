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
from peewee import *
import config

database = PostgresqlDatabase(
    database = config.DATABASES['Name'],
    user = config.DATABASES['User'],
    password = config.DATABASES['Password'],
    host = config.DATABASES['Host'],
    port = config.DATABASES['Port'])

class BaseModel(Model):
    class Meta:
        database = database
        
class JsonData(BaseModel):
    user_id = Autofield()
    id = Autofield()
    title = Charfield(max_length =255)
    body = Charfield(max_length =255)
    
    class Meta:
        table_name = 'posts'

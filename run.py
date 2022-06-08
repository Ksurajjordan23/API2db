import requests
import json
import os
import webbrowser
import httplib2
import urllib.request
import psycopg2
import sys
import psycopg2.extensions
from db import CreateRecord
from json import JsonPlaceHolderAPI


if __name__=="__main__":
    ticker_list = []

    for ticker in ticker_list:
        posts = JsonPlaceHolderAPI().get(ticker)
        CreateRecord().posts(
            user_id = posts['user_id'],
            id = posts['id'],
            title = posts['title'],
            body = posts['body']
            )
            

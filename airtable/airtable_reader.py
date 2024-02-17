import pyairtable
import os
import requests
from pyairtable import Api, Base, Table
from dotenv import load_dotenv
load_dotenv(".env")
AIRTABLE_BASE_ID=os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY=os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME=os.environ.get("AIRTABLE_TABLE_NAME")


endpoint=f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

headers= {
  "Authorization": f"Bearer {AIRTABLE_API_KEY}",
  "Content-Type": "application/json"
}


#downloading\printing contacts
api = Api(AIRTABLE_API_KEY)
api.all(AIRTABLE_BASE_ID, 'Contacts')

base = Base(AIRTABLE_API_KEY, AIRTABLE_BASE_ID)
base.all('Contacts')

table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)
table.all()
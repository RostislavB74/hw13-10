import django
import  os
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")

django.setup()
from quotes.models import Quotes, Tags, Authors

client = MongoClient("mongodb://localhost")
db = client.hw

authors = db.authors.find()

for author in authors:
    print (author)

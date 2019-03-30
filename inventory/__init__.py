from flask import Flask


inventory = Flask(__name__)
from inventory import views

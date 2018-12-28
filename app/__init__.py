from flask import Flask

app = Flask(__name__)

# To prevent a circular import error, load routes at bottom of this file.
from app import routes
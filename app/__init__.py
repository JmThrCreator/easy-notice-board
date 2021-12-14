from flask import Flask
from config import Config
from load_variables import get_source_folder, get_navigation_setting, get_program_destination
from load_poppler import load_poppler

app = Flask(__name__)
app.config.from_object(Config)

load_poppler()


from app import routes



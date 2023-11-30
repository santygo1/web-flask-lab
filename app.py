from flask import Flask

app = Flask(__name__)

from controller import main_controller
from controller import matrix_controller
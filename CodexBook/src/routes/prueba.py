from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request
# from ..models.models import Note
# from .. import db
import json


main = Blueprint('main', __name__)


@main.route('/home')
def home():
    return render_template('index.html')
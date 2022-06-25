from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request
# from .. import db
import json

views = Blueprint('views', __name__)


# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')
#         if len(note) < 1:
#             flash('Note is too short!', category='error')
#         else:
#             new_note = Note(data=note, user_id=current_user.id)
#             db.session.add(new_note)
#             db.session.commit()
#             flash('Note added!', category="success")
#     return render_template("home.html", user=current_user)


# @views.route('/delete-note', methods=['POST'])
# def delete_note():    
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
    
#     return jsonify({})


views = Blueprint('views', __name__)


@views.route('/home', methods=['GET'])
def home():
    return render_template("home.html")


@views.route('/reto', methods=['GET'])    
def reto():
    return render_template("reto.html")


@views.route('/ranking', methods=['GET'])    
def ranking():
    return render_template("ranking.html")


@views.route('/answer', methods=['GET'])    
def answer():
    return render_template("answer.html")
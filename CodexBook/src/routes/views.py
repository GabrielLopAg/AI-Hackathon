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


@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@views.route('/reto', methods=['GET'])    
def reto():
    return render_template("reto.html")


@views.route('/reto2', methods=['GET'])    
def reto2():
    return render_template("reto2.html")


@views.route('/reto3', methods=['GET'])    
def reto3():
    return render_template("reto3.html")


@views.route('/ranking', methods=['GET'])    
def ranking():
    return render_template("ranking.html")


@views.route('/answer', methods=['GET'])    
def answer():
    return render_template("answer.html")

# Nuevas rutas
@views.route('/profile', methods=['GET'])    
def profile():
    return render_template("profile.html")


@views.route('/cv', methods=['GET'])    
def cv():
    return render_template("cv.html")


@views.route('/upload', methods=['GET'])    
def upload():
    return render_template("upload.html")


@views.route('/logpro', methods=['GET'])    
def logpro():
    return render_template("logpro.html")


@views.route('/logrec', methods=['GET'])    
def logrec():
    return render_template("logrec.html")


@views.route('/iniciorec', methods=['GET'])    
def iniciorec():
    return render_template("iniciorec.html")


@views.route('/general', methods=['GET'])    
def general():
    return render_template("general.html")
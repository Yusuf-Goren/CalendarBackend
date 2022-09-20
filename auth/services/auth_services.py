
from flask import Response, jsonify, make_response, request, abort
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from model import User, Role
from app import db, app
from http.client import BAD_REQUEST


def register(request):
    name = request.json['name']
    surname = request.json['surname']
    email = request.json['email']
    phone = request.json['phone']
    isPat = request.json['isPat']
    isDoc = request.json['isDoc']

    user = User.query.filter(
        or_(User.phone == phone, User.email == email)).first()
    if(user):
        if(user.phone == phone or phone == ""):
            abort(make_response(
                jsonify({"message": "There is a user with this phone!!!"}), 400))
        if(user.email == email or email == ""):
            abort(make_response(
                jsonify({"message": "You already registered with this e-mail"}), 400))

    password = generate_password_hash(
        request.json['password'], method='sha256')

    user = User(name, surname, email, password, phone)

    db.session.add(user)
    patient = Role.query.filter(Role.id == 1).first()
    doctor = Role.query.filter(Role.id == 2).first()
    if(isPat):
        user.assignment.append(patient)
    elif(isDoc):
        user.assignment.append(doctor)
    else:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'At least one of an assignment must select"'}
        )

    db.session.commit()
    return {'message': '{user.assignment} created'}


def login(request):
    auth = request.json
    print(auth)
    if not auth or not auth.get('email') or not auth.get('password'):

        return abort(make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        ))

    user = User.query.filter_by(email=auth.get('email')) .first()

    password = request.json['password']
    if user:
        if check_password_hash(user.password, password):
            token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30000)}, app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({'token': token})

    print("Invalid identity")
    return "Invalid identity "


def logout():
    return "You logged off"

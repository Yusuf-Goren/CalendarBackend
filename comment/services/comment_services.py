from http.client import BAD_REQUEST
from re import I
from tokenize import endpats
from flask import abort, jsonify, make_response, request
from model import User, Comments
from app import db
from datetime import datetime


def get_doctor_comments(current_user, doctor_id):
    items = []
    if not current_user:
        return "unauthorize"
    for item in Comments.query.filter_by(doctor_id=doctor_id).order_by(Comments.id.desc()).all():
        user = User.query.filter_by(id=item.patient_id).first()
        items.append({
            "id": item.id,
            "name": user.name,
            "surname": user.surname,
            "text": item.text,
            "patient_id": item.patient_id
        })

    return jsonify(items)


def create_comment(current_user, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    text = request.json['text']
    doctor_id = request.json['doctor_id']

    comment = Comments(text=text, patient_id=current_user.id,
                       doctor_id=doctor_id)
    db.session.add(comment)

    db.session.commit()
    return {'message': 'comment created!'}


def edit_comment(current_user, comment_id, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )
    comment = Comments.query.filter_by(id=comment_id).first()

    if(type(comment) == "NoneType"):
        return make_response(
            '404 There is no with that id', 404
        )
    elif(comment.patient_id != current_user.id):
        return make_response(
            '401 Unauthorized You cant change someones comment', 401
        )

    text = request.json['text']
    db.session.query(Comments).filter_by(id=comment_id).update(
        dict(text=text)
    )
    db.session.commit()
    return {'message': 'comment edited!'}


def delete_comment(current_user, comment_id):
    comment = Comments.query.filter_by(id=comment_id).first()
    if(comment.patient_id == current_user.id):
        db.session.query(Comments).filter_by(id=comment_id).delete()
        db.session.commit()
        return {'message': comment_id + " deleted"}
    else:
        return {'message': "error"}

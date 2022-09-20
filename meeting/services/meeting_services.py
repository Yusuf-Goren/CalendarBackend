from http.client import BAD_REQUEST
from pydoc import doc
from re import I
from tokenize import endpats
from tracemalloc import start
from flask import abort, jsonify, make_response, request
from model import About, Blog, Meeting, User
from app import db
from datetime import datetime


def get_meetings(current_user):
    items = []

    if not current_user:
        return "XXX"
    for role in current_user.assignment:
        if "doctor" in role.name:
            for item in Meeting.query.filter_by(doctor_id=current_user.id).order_by(Meeting.start_date).all():
                user = User.query.filter(User.id == item.patient_id).first()
                del item.__dict__['_sa_instance_state']
                item = item.__dict__
                item["title"] = "lesson with : " + \
                    user.name + " " + user.surname
                items.append(item)
        else:
            for item in Meeting.query.filter_by(patient_id=current_user.id).order_by(Meeting.start_date).all():
                del item.__dict__['_sa_instance_state']
                items.append(item.__dict__)
    return jsonify(items)


def get_user(current_user):
    user = User.query.filter_by(id=current_user.id).first()
    for role in user.assignment:
        if "doctor" in role.name:
            return {"name": user.name, "surname": user.surname, "role": "doctor", "id": user.id}
    return {"name": user.name, "surname": user.surname, "role": "patient", "id": user.id}


def get_one_user(current_user, user_id):
    user = User.query.filter_by(id=user_id).first()

    return {"name": user.name, "surname": user.surname}


def get_all_doctors(current_user):
    items = []
    for item in User.query.all():
        for role in item.assignment:
            if "doctor" in role.name:
                about = About.query.filter_by(doctor_id=item.id).first()
                if type(about) == "NoneType":
                    about.text = None
                items.append({
                    "id": item.id,
                    "name": item.name,
                    "surname": item.surname,
                    "about": about.text
                })

    return {"data": items}


def get_all_users(current_user):
    items = []
    for item in User.query.all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def get_doc_meetings(current_user, doctor_id):
    items = []
    for item in Meeting.query.filter_by(doctor_id=doctor_id).order_by(Meeting.id).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def create_meeting(current_user, request):
    title = request.json['title']
    start_date = request.json['startdate']
    end_date = request.json['endDate']
    doctor_id = request.json['doctorId']

    start_date = datetime.strptime(start_date, '%d %b %Y %H:%M')
    end_date = datetime.strptime(end_date, '%d %b %Y %H:%M')

    date = datetime.now()
    if(start_date > end_date):
        return make_response(
            'Invalid date', 400

        )

    if(date > start_date):
        return make_response(
            'Invalid date', 400

        )
    doctor_meetings = []
    user_meetings = []
    # for item in Meeting.query.filter_by(doctor_id=doctor_id).all():
    #     del item.__dict__['_sa_instance_state']
    #     doctor_meetings.append(item.__dict__)

    # for item in Meeting.query.filter_by(patient_id=current_user.id).all():
    #     del item.__dict__['_sa_instance_state']
    #     user_meetings.append(item.__dict__)

    # for item in doctor_meetings:
    #     if item.start_date == start_date:
    #         return make_response(
    #             'Invalid date', 400
    #         )

    # for item in user_meetings:
    #     if item.start_date == start_date:
    #         return make_response(
    #             'Invalid date', 400
    #         )

    meeting = Meeting(title=title, start_date=start_date, end_date=end_date,
                      patient_id=current_user.id, doctor_id=doctor_id)
    db.session.add(meeting)

    db.session.commit()
    return {'message': 'Meeting created!'}


def edit_meeting(current_user, meeting_id, request):
    meeting = Meeting.query.filter_by(id=meeting_id).first()
    if(meeting.patient_id == current_user.id):
        title = request.json['title']
        start_date = request.json['startdate']
        end_date = request.json['endDate']
        doctor_id = request.json['doctorId']
        db.session.query(Meeting).filter_by(id=meeting_id).update(
            dict(title=title, start_date=start_date,
                 end_date=end_date, doctor_id=doctor_id)
        )
        db.session.commit()
        return {'message': meeting_id + ' Meeting edited!'}
    else:
        return {'message': 'error!'}


def delete_meeting(current_user, meeting_id):
    meeting = Meeting.query.filter_by(id=meeting_id).first()
    if(meeting.patient_id == current_user.id or meeting.doctor_id == current_user.id):
        db.session.query(Meeting).filter_by(id=meeting_id).delete()
        db.session.commit()
        return {'message': meeting_id + " deleted"}
    else:
        return {'message': "error"}

from urllib import response
from meeting.services import meeting_services
from flask import Blueprint, request
from helpers import token_required
MEETING = Blueprint('MEETING', __name__)


@MEETING.get("/")
@token_required
def get_meetings(current_user):
    response = meeting_services.get_meetings(current_user)
    return response


@MEETING.get("/user/<user_id>")
@token_required
def get_one_user(current_user, user_id):
    response = meeting_services.get_one_user(current_user, user_id)
    return response


@MEETING.get("/oneuser")
@token_required
def get_user(current_user):
    response = meeting_services.get_user(current_user)
    return response


@MEETING.get("/users")
@token_required
def get_all_users(current_user):
    response = meeting_services.get_all_users(current_user)
    return response


@MEETING.get("/doctors")
@token_required
def get_all_doctors(current_user):
    response = meeting_services.get_all_doctors(current_user)
    return response


@MEETING.post("/doctors/<doctor_id>")
@token_required
def get_doc_meetings(current_user, doctor_id):
    response = meeting_services.get_doc_meetings(current_user, doctor_id)
    return response


@MEETING.post("/create")
@token_required
def create_meeting(current_user):
    response = meeting_services.create_meeting(current_user, request)
    return response


@MEETING.put("/edit/<meeting_id>")
@token_required
def edit_meeting(current_user, meeting_id):
    response = meeting_services.edit_meeting(current_user, meeting_id, request)
    return response


@MEETING.delete("/delete/<meeting_id>")
@token_required
def delete_meeting(current_user, meeting_id):
    response = meeting_services.delete_meeting(
        current_user, meeting_id)
    return response

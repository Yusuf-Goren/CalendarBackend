from urllib import response
from comment.services import comment_services
from flask import Blueprint, request
from helpers import token_required
COMMENT = Blueprint('COMMENT', __name__)


@COMMENT.get("/<doctor_id>")
@token_required
def get_comments(current_user, doctor_id):
    response = comment_services.get_doctor_comments(current_user, doctor_id)
    return response


@COMMENT.post("/create")
@token_required
def create_comment(current_user):
    response = comment_services.create_comment(
        current_user, request)
    return response


@COMMENT.put("/edit/<comment_id>")
@token_required
def edit_comment(current_user, comment_id):
    response = comment_services.edit_comment(
        current_user, comment_id, request)
    return response


@COMMENT.delete("/delete/<comment_id>")
@token_required
def delete_comment(current_user, comment_id):
    response = comment_services.delete_comment(
        current_user, comment_id)
    return response

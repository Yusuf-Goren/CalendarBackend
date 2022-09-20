

from urllib import response
from helpers import token_required
from info.services import info_services
from flask import Blueprint, request
INFO = Blueprint('INFO', __name__)


@INFO.get("/about/user/<user_id>")
@token_required
def get_one_about(current_user, user_id):
    response = info_services.get_one_about(current_user, user_id)
    return response


@INFO.get("/about")
@token_required
def get_about(current_user):
    response = info_services.get_about(current_user)
    return response


@INFO.post("/about/create")
@token_required
def create_about(current_user):
    response = info_services.create_about(current_user, request)
    return response


@INFO.put("/about/edit/<about_id>")
@token_required
def edit_meeting(current_user, about_id):
    response = info_services.edit_about(current_user, about_id, request)
    return response


@INFO.get("/education")
@token_required
def get_edu(current_user):
    response = info_services.get_edu(current_user)
    return response


@INFO.get("/education/user/<user_id>")
@token_required
def get_one_edu(current_user, user_id):
    response = info_services.get_one_edu(current_user, user_id)
    return response


@INFO.post("/education/create")
@token_required
def create_edu(current_user):
    response = info_services.create_edu(current_user, request)
    return response


@INFO.put("/education/edit/<edu_id>")
@token_required
def edit_edu(current_user, edu_id):
    response = info_services.edit_edu(current_user, edu_id, request)
    return response


@INFO.delete("/education/delete/<edu_id>")
@token_required
def delete_edu(current_user, edu_id):
    response = info_services.delete_edu(current_user, edu_id)
    return response


@INFO.get("/certification")
@token_required
def get_cer(current_user):
    response = info_services.get_cer(current_user)
    return response


@INFO.get("/certification/user/<user_id>")
@token_required
def get_one_cer(current_user, user_id):
    response = info_services.get_one_cer(current_user, user_id)
    return response


@INFO.post("/certification/create")
@token_required
def create_cer(current_user):
    response = info_services.create_cer(current_user, request)
    return response


@INFO.put("/certification/edit/<cer_id>")
@token_required
def edit_cer(current_user, cer_id):
    response = info_services.edit_cer(current_user, cer_id, request)
    return response


@INFO.delete("/certification/delete/<cer_id>")
@token_required
def delete_cer(current_user, cer_id):
    response = info_services.delete_cer(current_user, cer_id)
    return response


@INFO.get("/blog")
@token_required
def get_blog(current_user):
    response = info_services.get_blog(current_user)
    return response


@INFO.post("/blog/<blog_id>")
@token_required
def get_one_blog(current_user, blog_id):
    response = info_services.get_one_blog(current_user, blog_id)
    return response


@INFO.get("/blog/user/<user_id>")
@token_required
def get_one_user_blog(current_user, user_id):
    response = info_services.get_one_user_blog(current_user, user_id)
    return response


@INFO.post("/blog/create")
@token_required
def create_blog(current_user):
    response = info_services.create_blog(current_user, request)
    return response


@INFO.put("/blog/edit/<blog_id>")
@token_required
def edit_blog(current_user, blog_id):
    response = info_services.edit_blog(current_user, blog_id, request)
    return response


@INFO.delete("/blog/delete/<blog_id>")
@token_required
def delete_blog(current_user, blog_id):
    response = info_services.delete_blog(current_user, blog_id)
    return response

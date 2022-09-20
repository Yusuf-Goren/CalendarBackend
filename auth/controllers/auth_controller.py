

from urllib import response
from auth.services import auth_services
from flask import Blueprint, request
AUTH = Blueprint('AUTH', __name__)


@AUTH.post("/login")
def login():
    response = auth_services.login(request)
    return response


@AUTH.post("/register")
def register():
    response = auth_services.register(request)
    return response


@AUTH.get("/logout")
def logout():
    response = auth_services.logout()
    return response

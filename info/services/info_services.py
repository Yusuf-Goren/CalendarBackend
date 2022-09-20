from flask import abort, jsonify, make_response, request
from model import User, About, Education, Certification, Blog
from app import db
from datetime import datetime
import os


def get_about(current_user):
    items = []
    if not current_user:
        return "XXX"
    for item in About.query.filter_by(doctor_id=current_user.id).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)

    return jsonify(items)


def get_one_about(current_user, user_id):
    about = About.query.filter_by(doctor_id=user_id).first()
    return {"title": about.title, "text": about.text}


def create_about(current_user, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    title = request.json['title']
    text = request.json['text']

    about = About(title=title, text=text, doctor_id=current_user.id)
    db.session.add(about)

    db.session.commit()
    return {'message': 'about created!'}


def edit_about(current_user, about_id, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    about = About.query.filter_by(id=about_id).first()
    if(about.doctor_id == current_user.id):
        title = request.json['title']
        text = request.json['text']
        db.session.query(About).filter_by(id=about_id).update(
            dict(title=title, text=text)
        )
        db.session.commit()
        return {'message': 'about edited!'}
    return make_response(
        '401 Unauthorized', 401
    )


def get_edu(current_user):
    items = []
    if not current_user:
        return "XXX"
    for item in Education.query.filter_by(doctor_id=current_user.id).order_by(Education.id.desc()).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def get_one_edu(current_user, user_id):
    items = []
    if not current_user:
        return "XXX"
    for item in Education.query.filter_by(doctor_id=user_id).order_by(Education.id.desc()).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def create_edu(current_user, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    institution = request.json['institution']
    desciripton = request.json['desciripton']
    start_date = request.json['startDate']
    end_date = request.json['endDate']
    average = request.json['avg']

    edu = Education(institution=institution, desciripton=desciripton, start_date=start_date,
                    end_date=end_date, average=average, doctor_id=current_user.id)
    db.session.add(edu)

    db.session.commit()
    return {'message': 'education created!'}


def edit_edu(current_user, edu_id, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    edu = Education.query.filter_by(id=edu_id).first()
    if(edu.doctor_id == current_user.id):
        institution = request.json['institution']
        desciripton = request.json['desciripton']
        start_date = request.json['startDate']
        end_date = request.json['endDate']
        average = request.json['avg']

        db.session.query(Education).filter_by(id=edu_id).update(
            dict(institution=institution, desciripton=desciripton, start_date=start_date,
                 end_date=end_date, average=average)
        )
        db.session.commit()
        return {'message': 'edu edited!'}
    return make_response(
        '401 Unauthorized', 401
    )


def delete_edu(current_user, edu_id):
    edu = Education.query.filter_by(id=edu_id).first()
    if(edu.doctor_id == current_user.id):
        db.session.query(Education).filter_by(id=edu_id).delete()
        db.session.commit()
        return {'message': edu_id + " deleted"}
    else:
        return {'message': "error"}


def get_cer(current_user):
    items = []
    if not current_user:
        return "XXX"
    for item in Certification.query.filter_by(doctor_id=current_user.id).order_by(Certification.id.desc()).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def get_one_cer(current_user, user_id):
    items = []
    if not current_user:
        return "XXX"
    for item in Certification.query.filter_by(doctor_id=user_id).order_by(Certification.id.desc()).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def create_cer(current_user, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )
    institution = request.json['institution']
    desciripton = request.json['desciripton']
    start_date = request.json['startDate']
    end_date = request.json['endDate'] if "endDate" in request.json else None

    cer = Certification(institution=institution, desciripton=desciripton, start_date=start_date,
                        end_date=end_date, doctor_id=current_user.id)
    db.session.add(cer)

    db.session.commit()
    return {'message': 'certification created!'}


def edit_cer(current_user, cer_id, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    cer = Certification.query.filter_by(id=cer_id).first()
    if(cer.doctor_id == current_user.id):
        institution = request.json['institution']
        desciripton = request.json['desciripton']
        start_date = request.json['startDate']
        end_date = request.json['endDate']
        db.session.query(Certification).filter_by(id=cer_id).update(
            dict(institution=institution, desciripton=desciripton, start_date=start_date,
                 end_date=end_date)
        )
        db.session.commit()
        return {'message': 'cer edited!'}
    return make_response(
        '401 Unauthorized', 401
    )


def delete_cer(current_user, cer_id):
    cer = Certification.query.filter_by(id=cer_id).first()
    if(cer.doctor_id == current_user.id):
        db.session.query(Certification).filter_by(id=cer_id).delete()
        db.session.commit()
        return {'message': cer_id + "idli certification deleted"}
    else:
        return {'message': "error"}


def get_blog(current_user):
    items = []
    if not current_user:
        return "XXX"
    for item in Blog.query.filter_by(doctor_id=current_user.id).order_by(Blog.id.desc()).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def get_one_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    user = User.query.filter_by(id=blog.doctor_id).first()
    return {"title": blog.title, "text": blog.text, "username": user.name, "surname": user.surname, "created_at": blog.created_at}


def get_one_user_blog(current_user, user_id):
    items = []
    if not current_user:
        return "XXX"
    for item in Blog.query.filter_by(doctor_id=user_id).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def create_blog(current_user, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    title = request.json['title']
    text = request.json['text']

    blog = Blog(title=title, text=text, doctor_id=current_user.id)
    db.session.add(blog)

    db.session.commit()
    return {'message': 'Blog created!'}


def edit_blog(current_user, blog_id, request):
    item = User.query.filter_by(id=current_user.id).first()
    for role in item.assignment:
        if not "doctor" in role.name:
            return make_response(
                '401 Unauthorized', 401
            )

    blog = Blog.query.filter_by(id=blog_id).first()
    if(blog.doctor_id == current_user.id):
        title = request.json['title']
        text = request.json['text']
        db.session.query(Blog).filter_by(id=blog_id).update(
            dict(title=title, text=text)
        )
        db.session.commit()
        return {'message': 'blog edited!'}
    return make_response(
        '401 Unauthorized', 401
    )


def delete_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    if(blog.doctor_id == current_user.id):
        db.session.query(Blog).filter_by(id=blog_id).delete()
        db.session.commit()
        return {'message': blog_id + "idli blog deleted"}
    else:
        return {'message': "error"}

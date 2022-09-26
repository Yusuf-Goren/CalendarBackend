from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from io import BytesIO


app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/calendarapp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rqxzwuljlogffz:603e2b9c34c53c44279d5e597f05113e8820c8c204bf308a09769072a1e58223@ec2-3-93-206-109.compute-1.amazonaws.com:5432/d1ap1qq01tad9d'
app.config['SECRET_KEY'] = 'secretKey'


db = SQLAlchemy()

with app.app_context():
    from auth.controllers.auth_controller import AUTH
    # from meeting.controllers.meeting_controller import MEETING
    # from info.controllers.info_controller import INFO
    # from comment.controllers.comment_controller import COMMENT

    db.init_app(app)
    db.create_all()
    db.session.commit()
    migrate = Migrate(app, db)

    app.register_blueprint(AUTH, url_prefix='/')
    # app.register_blueprint(MEETING, url_prefix='/meeting')
    # app.register_blueprint(INFO, url_prefix='/info')
    # app.register_blueprint(COMMENT, url_prefix='/comments')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from io import BytesIO


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/calendarapp'
app.config['SECRET_KEY'] = 'secretKey'


db = SQLAlchemy()

with app.app_context():
    from auth.controllers.auth_controller import AUTH
    from meeting.controllers.meeting_controller import MEETING
    from info.controllers.info_controller import INFO
    from comment.controllers.comment_controller import COMMENT

    db.init_app(app)
    db.create_all()
    db.session.commit()
    migrate = Migrate(app, db)

    app.register_blueprint(AUTH, url_prefix='/')
    app.register_blueprint(MEETING, url_prefix='/meeting')
    app.register_blueprint(INFO, url_prefix='/info')
    app.register_blueprint(COMMENT, url_prefix='/comments')


if __name__ == "__main__":
    app.run(debug=True)

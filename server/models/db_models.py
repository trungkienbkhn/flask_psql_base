from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from server.app import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), index=True, nullable=False)
    last_name = db.Column(db.String(30), index=True, nullable=False)
    email = db.Column(db.String(255), index=True, nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if key == 'password':
                self.password = User.hash_password(value)

    @staticmethod
    def hash_password(password):
        return pwd_context.encrypt(password, category="admin")

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def get_user_info_object(self):
        return {
            'user_id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

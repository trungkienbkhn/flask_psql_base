from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from passlib.apps import custom_app_context as pwd_context
from server.app import app

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), index=True, nullable=False)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), index=True, nullable=False)
    last_name = db.Column(db.String(30), index=True, nullable=False)
    email = db.Column(db.String(255), index=True, nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', foreign_keys=[role_id], lazy=True)

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

    def generate_auth_token(self, expiration=600, uid=None):
        if uid is None:
            uid = self.id
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        auth_token = s.dumps({'id': uid})
        retry_count = 0
        while str(auth_token).count(' ') != 0 and retry_count < 2:
            auth_token = s.dumps({'id': uid})
            retry_count += 1
        if retry_count == 2:
            raise Exception('Unable to generate token')
        return auth_token

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user

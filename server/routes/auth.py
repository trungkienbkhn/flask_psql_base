from flask import request, jsonify, abort, make_response, g, session
from server.app import app, config
from server.routes.user import get_user_info
from server.models.db_models import User


@app.before_request
def before_request_func():
    # This function is executed before every request
    bearer_token = request.headers.get('Authorization')
    connected_user = session.get('user')
    if connected_user:
        g.user = User.query.filter_by(id=session['user'].get('id')).first()
        return
    elif not connected_user and request.endpoint == 'login':
        return

    if not bearer_token:
        abort(make_response(jsonify(message="invalid credentials"), 401))

    token = bearer_token.split()[-1]
    if not verify_password(token, 'x'):
        abort(make_response(jsonify(message="invalid credentials"), 401))


@app.route('/login', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(make_response(jsonify(message="Missing email or password"), 400))
    if not verify_password(email, password):
        abort(make_response(jsonify(message="Email or password is incorrect"), 401))

    session['user'] = get_user_info(g.user)
    duration = config.get('AUTH_PERSISTENCE', 86400)
    token = generate_token(g.user.id, duration)

    return jsonify({'token': token, 'duration': duration})


@app.route('/logout')
def logout():
    session.clear()

    return jsonify({"message": 'ok'})


def verify_password(tid_or_token, password):
    if len(tid_or_token) > 3 and tid_or_token.startswith('_T_'):
        tid_or_token = tid_or_token[3:]
        user = User.verify_auth_token(tid_or_token)
        if not user:
            return False
    else:
        # try to authenticate with email/password
        user = User.query.filter_by(email=tid_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user

    return True


def generate_token(user_id, duration):
    token = g.user.generate_auth_token(duration, user_id).decode('ascii')

    return "_T_" + token

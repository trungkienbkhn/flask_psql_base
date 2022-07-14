from flask import jsonify, abort, make_response
from server.app import app
from server.models.db_models import User


@app.route("/user/list", methods=["GET"])
def list_user():
    lst = User.query.all()

    users = []
    for u in lst:
        current_user = get_user_info(u)
        if current_user is not None:
            users.append(current_user)

    return jsonify(users)


def get_user_info(current_user):
    u = {
        'id': str(current_user.id),
        'name': current_user.first_name + ' ' + current_user.last_name,
        'first_name': current_user.first_name,
        'last_name': current_user.last_name,
        'email': current_user.email
    }

    return u


@app.route("/user/<uid>", methods=["GET"])
def user(uid):
    if not uid:
        abort(make_response(jsonify(message="invalid user_id"), 400))

    current_user = User.query.filter_by(id=uid).first()
    if current_user is None:
        return make_response(jsonify(message="unknown user"), 400)
    result = get_user_info(current_user)

    return jsonify(result)

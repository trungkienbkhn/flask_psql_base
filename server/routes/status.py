from flask import jsonify
from server.models.db_models import User
from server.app import app


@app.route('/api/status', methods=['GET'])
def get_status():
    result = {
        'server': 'ok',
        'db': 'failed'
    }
    if User.query.all():
        result['db'] = 'ok'

    return jsonify({"data": result})

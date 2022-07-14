from flask import redirect
from server.app import app
# pylint: disable=unused-import
from server.routes import status, user, auth
from server.models.db_models import db


@app.route('/', methods=['GET'])
def index():
    return redirect("/api/status")


if __name__ == "__main__":
    app.run()


def get_app():
    return app


def get_db():
    return db

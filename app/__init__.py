import logging

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_appbuilder import AppBuilder, SQLA
from app.index import HomeView
from app import models

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=HomeView)

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

@app.route('/list_coefficients', methods=['GET'])
def list_coefficients():
    result_set = db.session.query(models.Coefficient).all()

    return jsonify(result_set)



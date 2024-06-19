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

@app.route('/admin/list_coefficients', methods=['GET'])
def list_coefficients():
    result_set = db.session.query(models.Coefficient).all()

    return jsonify(result_set), 200

@app.route('/admin', methods=['GET'])
def render_admin():
    result_set = db.session.query(models.Coefficient).all()

    distance_coefficient = result_set[0].value
    weight_coefficient = result_set[1].value

    return render_template('admin.html', distance_coefficient=distance_coefficient, weight_coefficient=weight_coefficient), 200

@app.route('/admin/update_coefficients', methods=['POST'])
def update_coefficients():
    new_distance_coefficient = request.form.get("new_distance_coefficient")
    new_weight_coefficient = request.form.get("new_weight_coefficient")

    if new_distance_coefficient is None and new_weight_coefficient is None:
        return jsonify({ "error": "One or more of the required values were not provided."}), 400
    
    db.session.query(models.Coefficient).filter(models.Coefficient.name == "distance").update({ models.Coefficient.value: new_distance_coefficient })
    db.session.query(models.Coefficient).filter(models.Coefficient.name == "weight").update({ models.Coefficient.value: new_weight_coefficient })

    db.session.flush()
    db.session.commit()

    return '', 204
    

@app.route('/calculate_cost', methods=['POST'])
def calculate_cost():
    # Get distance and weight from request body
    delivery_distance = request.form.get('delivery_distance', type=float)
    delivery_weight = request.form.get('delivery_weight', type=float)

    if delivery_distance is None:
        return jsonify({ "error": "delivery_distance value was not provided or was provided in an invalid format" }), 400
    
    if delivery_weight is None:
        return jsonify({ "error": "delivery_weight value was not provided or was provided in an invalid format" }), 400

    # Get distance coefficient and weight coefficient from PostgreSQL database
    result_set = db.session.query(models.Coefficient)

    distance_coefficient = float(result_set.filter(models.Coefficient.name == 'distance').first().value)
    weight_coefficient = float(result_set.filter(models.Coefficient.name == 'weight').first().value)

    # Perform calculation
    delivery_cost = (distance_coefficient * delivery_distance) + (weight_coefficient * delivery_weight)
    
    db.session.flush()
    db.session.commit()

    delivery_cost_str = "{:.2f}".format(delivery_cost)

    return jsonify({ "cost": delivery_cost_str, "status_message": "value successfully calculated"  })

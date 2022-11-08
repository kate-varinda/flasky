from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.cyclist import Cyclist
from .routes_helper import get_one_object_or_abort
from app.models.bike import Bike


cyclist_bp = Blueprint("cyclist_bp", __name__, url_prefix="/cyclist")

@cyclist_bp.route("", methods=["POST"])

def add_cyclist():
    request_body = request.get_json()

    new_cyclist = Cyclist.from_dict(request_body)

    db.session.add(new_cyclist)
    db.session.commit()

    return {"id": new_cyclist.id}, 201


@cyclist_bp.route("", methods=["GET"])
def get_all_cyclists():
    cyclists = Cyclist.query.all()

    response = [cyclist.to_dict() for cyclist in cyclists]
    return jsonify(response), 200

def get_one_cyclist_or_abort(Cyclist, cyclist_id):
    try:
        cyclist_id = int(cyclist_id)
    except ValueError:
        response_str = f"Invalid cyclist_id: {cyclist_id}. ID must be an integer."
        return jsonify({"message": response_str}), 400

    matching_cyclist = Cyclist.query.get(cyclist_id)

    if matching_cyclist is None:
        response_str = f"cyclist with id {cyclist_id} was not found in the database."
        abort(make_response({"message": response_str}, 404))
    
    return matching_cyclist


@cyclist_bp.route("/<cyclist_id>", methods=["GET"])
def get_one_cyclist(cyclist_id):
    chosen_cyclist = get_one_object_or_abort(Cyclist, cyclist_id)

    cyclist_dict = chosen_cyclist.to_dict()

    return jsonify(cyclist_dict), 200

@cyclist_bp.route("/<cyclist_id>/bike", methods=["GET"])
def get_all_bikes_from_cyclist(cyclist_id):
    cyclist = get_one_cyclist(Cyclist, cyclist_id)

    bike_response = [bike.to_dict() for bike in cyclist.bikes]
    return jsonify(bike_response), 200

@cyclist_bp.route("/<cyclist_id>/bike", methods=["POST"])
def post_bike_belonging_to_cylist(cyclist_id):
    parent_cyclist = get_one_cyclist_or_abort(Cyclist, cyclist_id)

    request_body = request.get_json()
    new_bike = Bike.from_dict(request_body)
    new_bike.cyclist = parent_cyclist

    db.session.add(new_bike)
    db.session.commit()

    return jsonify({"message":f"Bike {new_bike.name} belonging to {new_bike.cyclist.name} successfully added."}), 201
from urllib import response
from flask import Blueprint, jsonify

class Bike:
    def __init__(self, id, name, price, size, type):
        self.id = id
        self.name = name
        self.price = price
        self.size = size
        self.type = type

bikes = [
    Bike(5, "Nina", 100, 48, "gravel"),
    Bike(8, "Bike 3000", 1000, 50, "hybrid"),
    Bike(2, "Auberon", 2000, 52, "electronic")
]

bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")

@bike_bp.route("", methods=["GET"])
def get_all_bikes():
    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name": bike.name,
            "price": bike.price,
            "size": bike.size,
            "type": bike.type
        }
        response.append(bike_dict)
    return jsonify(response), 200


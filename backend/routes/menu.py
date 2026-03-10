from flask import Blueprint, jsonify
from db import menu_collection

menu_routes = Blueprint("menu_routes", __name__)

@menu_routes.route("/menu", methods=["GET"])
def get_menu():

    items = []

    for item in menu_collection.find({}, {"_id": 0}):
        items.append(item)

    return jsonify(items)
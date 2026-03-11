from bson import ObjectId
from flask import Blueprint, jsonify, request
from db import menu_collection

menu_routes = Blueprint("menu_routes", __name__)

@menu_routes.route("/menu", methods=["GET"])
def get_menu():

    items = []

    for item in menu_collection.find():
        item["_id"] = str(item["_id"])  # convert ObjectId to string
        items.append(item)

    return jsonify(items)

@menu_routes.route("/menu", methods=["POST"])
def add_menu():

    data = request.json

    menu_collection.insert_one({
        "name": data["name"],
        "category": data["category"],
        "price": data["price"]
    })

    return jsonify({"message": "Menu item added"})

@menu_routes.route("/menu/<id>", methods=["DELETE"])
def delete_menu(id):

    menu_collection.delete_one({
        "_id": ObjectId(id)
    })

    return jsonify({"message": "deleted"})
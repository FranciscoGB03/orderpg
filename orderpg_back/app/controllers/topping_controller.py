from flask import request, jsonify
from app.services.supabase_service import add_topping_to_db, get_all_topping_active_service, get_all_toppings_service, update_topping_service

def add_topping():
    data = request.json
    name, status = data.get("name"), data.get("active")

    if not name or not status:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    try:
        add_topping_to_db(name, status)
        return jsonify({"message": "Topping agregado con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_toppings_active():
    try:
        toppings = get_all_topping_active_service()
        return jsonify(toppings), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_all_toppings():
    try:
        toppings = get_all_toppings_service()
        return jsonify(toppings), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_topping(topping_id):
    data = request.json
    name = data.get("name")
    status=data.get("active")

    if not name:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    return update_topping_service(topping_id, name, status)
from flask import request, jsonify
from app.services.supabase_service import add_syrup_service, get_all_syrup_active_service, get_all_syrups_service, update_syrup_service

def add_syrup():
    data = request.json
    name, status = data.get("name"), data.get("active")

    if not name or not status:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    try:
        add_syrup_service(name, status)
        return jsonify({"message": "Járabe agregado con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_syrups_active():
    try:
        syrups = get_all_syrup_active_service()
        return jsonify(syrups), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_all_syrups():
    try:
        syrups = get_all_syrups_service()
        return jsonify(syrups), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_syrup(syrup_id):
    data = request.json
    name = data.get("name")
    status=data.get("active")

    if not name:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    return update_syrup_service(syrup_id, name, status)
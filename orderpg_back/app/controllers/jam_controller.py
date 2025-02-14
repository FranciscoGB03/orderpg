from flask import request, jsonify
from app.services.supabase_service import add_jam_service, get_all_jam_active_service, get_all_jams_service, update_jam_service

def add_jam():
    data = request.json
    name, status = data.get("name"), data.get("active")

    if not name or not status:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    try:
        add_jam_service(name, status)
        return jsonify({"message": "Mermelada agregada con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_jams_active():
    try:
        syrups = get_all_jam_active_service()
        return jsonify(syrups), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_all_jams():
    try:
        syrups = get_all_jams_service()
        return jsonify(syrups), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_jam(jam_id):
    data = request.json
    name = data.get("name")
    status=data.get("active")

    if not name:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    return update_jam_service(jam_id, name, status)
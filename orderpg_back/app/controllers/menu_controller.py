from flask import request, jsonify
from app.services.supabase_service import add_menu_to_db, get_all_menus_active_service, get_all_menus_service, update_menu_service

def add_menu():
    data = request.json
    name, price, description, status = data.get("name"), data.get("price"), data.get("description"), data.get("active")

    if not name or not price or not description:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    try:
        add_menu_to_db(name, price, description, status)
        return jsonify({"message": "Menú agregado con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_menus_active():
    try:
        menus = get_all_menus_active_service()
        return jsonify(menus), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_all_menus():
    try:
        menus = get_all_menus_service()
        return jsonify(menus), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_menu(menu_id):
    data = request.json
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    status=data.get("active")

    if not name or not price or not description:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    return update_menu_service(menu_id, name, price, description,status)
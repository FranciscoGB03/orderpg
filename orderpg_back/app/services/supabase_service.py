from flask import jsonify
from supabase import create_client
from app.config import Config

supabase_client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)

# Metodo para agregar un menu a la tabla de menus de supabase
def add_menu_to_db(name, price, description, status):
    try:
        response = supabase_client.table("menus").insert({
            "name": name,
            "price": price,
            "description": description,
            "active": status
        }).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

#Metodo para la consulta de los menus existentes
def get_all_menus_active_service():
    try:
        response = supabase_client.table("menus").select("*").eq("active",True).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

#Metodo para la consulta de los menus
def get_all_menus_service():
    try:
        response = supabase_client.table("menus").select("*").execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")


# Metodo para actualizar un menu 
def update_menu_service(menu_id, name, price, description,status):
    try:
        response = supabase_client.table("menus").update({
            "name": name,
            "price": price,
            "description": description,
            "active":status
        }).eq("id", menu_id).execute()

        if response.data:
            return jsonify({"message": "Menú actualizado con éxito"}), 200
        else:
            return jsonify({"error": "Menú no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
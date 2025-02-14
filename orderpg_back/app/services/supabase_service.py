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

def add_topping_to_db(name, status):
    try:
        response = supabase_client.table("toppings").insert({
            "name": name,
            "active": status
        }).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

def get_all_topping_active_service():
    try:
        response = supabase_client.table("toppings").select("*").eq("active",True).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")
    
def get_all_toppings_service():
    try:
        response = supabase_client.table("toppings").select("*").execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")
    
# Metodo para actualizar un topping 
def update_topping_service(topping_id, name,status):
    try:
        response = supabase_client.table("toppings").update({
            "name": name,
            "active":status
        }).eq("id", topping_id).execute()

        if response.data:
            return jsonify({"message": "Topping actualizado con éxito"}), 200
        else:
            return jsonify({"error": "Topping no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def add_syrup_service(name, status):
    try:
        response = supabase_client.table("syrup").insert({
            "name": name,
            "active": status
        }).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

def get_all_syrup_active_service():
    try:
        response = supabase_client.table("syrup").select("*").eq("active",True).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

def get_all_syrups_service():
    try:
        response = supabase_client.table("syrup").select("*").execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

def update_syrup_service(syrup_id, name, status):
    try:
        response = supabase_client.table("syrup").update({
            "name": name,
            "active":status
        }).eq("id", syrup_id).execute()

        if response.data:
            return jsonify({"message": "Járabe actualizado con éxito"}), 200
        else:
            return jsonify({"error": "Jarabe no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_jam_service(name, status):
    try:
        response = supabase_client.table("jam").insert({
            "name": name,
            "active": status
        }).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")
    
def get_all_jam_active_service(): 
    try:
        response = supabase_client.table("jam").select("*").eq("active",True).execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

def get_all_jams_service(): 
    try:
        response = supabase_client.table("jam").select("*").execute()
        return response.data
    except Exception as e:
        raise Exception(f"Error en Supabase: {str(e)}")

def update_jam_service(jam_id, name, status):
    try:
        response = supabase_client.table("jam").update({
            "name": name,
            "active":status
        }).eq("id", jam_id).execute()

        if response.data:
            return jsonify({"message": "Mermelada actualizada con éxito"}), 200
        else:
            return jsonify({"error": "Mermelada no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
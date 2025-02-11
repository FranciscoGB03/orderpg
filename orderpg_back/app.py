import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import supabase
from supabase import create_client

app = Flask(__name__)
CORS(app)  # Habilitar CORS para que el frontend pueda acceder al backend

load_dotenv() 
# Configuración del bot de Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # ID del chat donde llegarán los pedidos
# configuracion a supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# Conexion a supabase  
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

def tarea_repetitiva():
    print("Hola")

# Configurar el scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(tarea_repetitiva, 'interval', seconds=30)  # Ejecuta cada 30 segundos
scheduler.start()

# ruta para matener vivo el servidor en render
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": CHAT_ID}), 200

#ruta para mandar el mensaje a telegram
@app.route('/api/order', methods=['POST'])
def handle_order():
    data = request.json
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    # Extraer información del pedido
    customer_name = data.get("customer_name")
    product = data.get("product")
    product_name=product.get("name")
    notes=data.get("notes")
    address = data.get("address")
    amount = data.get("amount")
    phone = data.get("phone")

    if not customer_name or not product_name or not amount:
        return jsonify({"error": "Faltan campos"}), 400

    # Crear el mensaje para Telegram
    message = f"🍰 *Nuevo Pedido de Postres* 🍰\n\n👤 Cliente: {customer_name}\n🍨 Producto: {product_name}\n\nNotas:{notes}\n Cantidad: {amount}\n Telefono de contacto:{phone}\n📍 Dirección de envio: {address}"
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"  # Permite darle formato al mensaje
    }

    # Enviar mensaje a Telegram
    response = requests.post(telegram_url, json=payload)
    if response.status_code == 200:
        return jsonify({"message": "Pedido enviado exitosamente"}), 200
    else:
        return jsonify({"error": "No se pudo enviar el mensaje a Telegram"}), 500
    
@app.route("/api/add-menu", methods=["POST"])
def add_menu():
    data = request.json
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")

    if not name or not price or not description:
        return jsonify({"error": "Todos los campos son requeridos"}), 400

    # Guardar en Supabase
    try:
        response = supabase_client.table("menus").insert({
            "name": name,
            "price": price,
            "description": description
        }).execute()
        return jsonify({"message": "Menú agregado con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/menus", methods=["GET"])
def get_menus():
    try:
        response = supabase_client.table("menus").select("*").execute()
        data = response.data  # Obtener los datos de la respuesta
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    try:
        port = int(os.environ.get("PORT", 5000))  # Render asigna un puerto dinámico
        app.run(host='0.0.0.0', port=port, debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
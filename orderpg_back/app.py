import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)  # Habilitar CORS para que el frontend pueda acceder al backend

# Configuración del bot de Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("SUPABASE_KEY")  # ID del chat donde llegarán los pedidos

def tarea_repetitiva():
    print("Hola")

# Configurar el scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(tarea_repetitiva, 'interval', seconds=30)  # Ejecuta cada 30 segundos
scheduler.start()

# ruta para matener vivo el servidor en render
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200

#ruta para mandar el mensaje a telegram
@app.route('/api/order', methods=['POST'])
def handle_order():
    data = request.json
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    # Extraer información del pedido
    customer_name = data.get("customer_name")
    dessert = data.get("dessert")
    address = data.get("address")

    if not customer_name or not dessert or not address:
        return jsonify({"error": "Faltan campos"}), 400

    # Crear el mensaje para Telegram
    message = f"🍰 *Nuevo Pedido de Postres* 🍰\n\n👤 Cliente: {customer_name}\n🍨 Postre: {dessert}\n📍 Dirección: {address}"
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

if __name__ == '__main__':
    try:
        port = int(os.environ.get("PORT", 5000))  # Render asigna un puerto dinámico
        app.run(host='0.0.0.0', port=port, debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
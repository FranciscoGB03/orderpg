from flask import request, jsonify
from app.services.telegram_service import send_order_to_telegram

def handle_order():
    data = request.json
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    customer_name = data.get("customer_name")
    products = data.get("products", [])  # Lista de productos
    phone = data.get("phone")
    address = data.get("address", "")

    if not customer_name or not products or not phone:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    success = send_order_to_telegram(customer_name, products, phone, address)

    if success:
        return jsonify({"message": "Pedido enviado exitosamente"}), 200
    else:
        return jsonify({"error": "No se pudo enviar el mensaje a Telegram"}), 500
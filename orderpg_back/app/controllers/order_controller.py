from flask import request, jsonify
from app.services.telegram_service import send_order_to_telegram

def handle_order():
    data = request.json
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    customer_name = data.get("customer_name")
    product = data.get("product", {})
    product_name = product.get("name")
    notes = data.get("notes", "")
    address = data.get("address", "")
    amount = data.get("amount")
    phone = data.get("phone")

    if not customer_name or not product_name or not amount:
        return jsonify({"error": "Faltan campos"}), 400

    success = send_order_to_telegram(customer_name, product_name, notes, amount, phone, address)
    
    if success:
        return jsonify({"message": "Pedido enviado exitosamente"}), 200
    else:
        return jsonify({"error": "No se pudo enviar el mensaje a Telegram"}), 500

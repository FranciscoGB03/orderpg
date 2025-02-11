import requests
from app.config import Config

def send_order_to_telegram(customer_name, product_name, notes, amount, phone, address):
    message = (
        f"🍰 *Nuevo Pedido de Postres* 🍰\n\n"
        f"👤 Cliente: {customer_name}\n"
        f"🍨 Producto: {product_name}\n"
        f"📓 Notas: {notes}\n"
        f"#️⃣ Cantidad: {amount}\n"
        f"📞 Telefono: {phone}\n"
        f"📍 Dirección: {address}"
    )
    
    telegram_url = f"https://api.telegram.org/bot{Config.BOT_TOKEN}/sendMessage"
    payload = {"chat_id": Config.CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    response = requests.post(telegram_url, json=payload)
    return response.status_code == 200

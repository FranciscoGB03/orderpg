import requests
from app.config import Config

def send_order_to_telegram(customer_name, products, phone, address):
    product_details = "\n".join(
        [
            f"🍨 Producto: {p['name']}\n"
            f"🍫 Topping: {p.get('topping', 'Sin Topping')}\n"
            f"🍓 Mermelada: {p.get('jam', 'Sin mermelada')}\n"
            f"🍯 Jarabe: {p.get('syrup', 'Sin jarabe')}\n"
            f"📓 Elección, complemento o especificación en el pedido: {p.get('notes', 'Sin notas')}\n"
            f"#️⃣ Cantidad: {p['amount']}\n"
            f"💲 Precio unitario: {p['price']}\n"
            f"💰 Subtotal: {p['amount'] * p['price']}\n"
            "-------------------"
            for p in products
        ]
    )

    total = sum(p["amount"] * p["price"] for p in products)

    message = (
        f"🍰 *Nuevo Pedido de Postres* 🍰\n\n"
        f"👤 Cliente: {customer_name}\n"
        f"📞 Teléfono: {phone}\n"
        f"📍 Dirección: {address}\n\n"
        f"🛒 *Detalle del Pedido:* \n{product_details}\n"
        f"💳 *Total a pagar: {total}*\n"
    )

    telegram_url = f"https://api.telegram.org/bot{Config.BOT_TOKEN}/sendMessage"
    payload = {"chat_id": Config.CHAT_ID, "text": message, "parse_mode": "Markdown"}

    response = requests.post(telegram_url, json=payload)
    return response.status_code == 200

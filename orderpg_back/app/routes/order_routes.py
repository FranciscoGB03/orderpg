from flask import Blueprint
from app.controllers.order_controller import handle_order

order_bp = Blueprint("order_bp", __name__)

order_bp.route("/order", methods=["POST"])(handle_order)

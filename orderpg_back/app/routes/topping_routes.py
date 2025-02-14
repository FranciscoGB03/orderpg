from flask import Blueprint
from app.controllers.topping_controller import add_topping, get_toppings_active, get_all_toppings, update_topping

topping_bp = Blueprint("topping_bp", __name__)

topping_bp.route("/add-topping", methods=["POST"])(add_topping)
topping_bp.route("/allActiveToppings", methods=["GET"])(get_toppings_active)
topping_bp.route("/update-topping/<int:topping_id>", methods=["PUT"])(update_topping)
topping_bp.route("/allTopings",methods=["GET"])(get_all_toppings)
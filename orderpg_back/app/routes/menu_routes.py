from flask import Blueprint
from app.controllers.menu_controller import add_menu, get_all_menus, get_menus_active, update_menu

menu_bp = Blueprint("menu_bp", __name__)

menu_bp.route("/add-menu", methods=["POST"])(add_menu)
menu_bp.route("/menus", methods=["GET"])(get_menus_active)
menu_bp.route("/update-menu/<int:menu_id>", methods=["PUT"])(update_menu)
menu_bp.route("/allMenus",methods=["GET"])(get_all_menus)

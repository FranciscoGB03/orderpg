from flask import Blueprint
from app.controllers.syrup_controller import add_syrup, get_all_syrups, get_syrups_active, update_syrup

syrup_bp = Blueprint("syrup_bp", __name__)

syrup_bp.route("/add-syrup", methods=["POST"])(add_syrup)
syrup_bp.route("/allActiveSyrups", methods=["GET"])(get_syrups_active)
syrup_bp.route("/update-syrup/<int:syrup_id>", methods=["PUT"])(update_syrup)
syrup_bp.route("/allSyrups",methods=["GET"])(get_all_syrups)
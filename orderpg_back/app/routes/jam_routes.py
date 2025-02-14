from flask import Blueprint
from app.controllers.jam_controller import add_jam, get_all_jams, get_jams_active, update_jam

jam_bp = Blueprint("jam_bp", __name__)

jam_bp.route("/add-jam", methods=["POST"])(add_jam)
jam_bp.route("/allActiveJams", methods=["GET"])(get_jams_active)
jam_bp.route("/update-jam/<int:jam_id>", methods=["PUT"])(update_jam)
jam_bp.route("/allJams",methods=["GET"])(get_all_jams)
from flask import Blueprint
from app.controllers.ping_controller import ping

ping_bp=Blueprint("ping_bp", __name__)

ping_bp.route("/ping", methods=["GET"])(ping)
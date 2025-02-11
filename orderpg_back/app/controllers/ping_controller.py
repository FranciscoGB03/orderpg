from flask import jsonify

def ping():
    return jsonify({"message":"hola"}),200
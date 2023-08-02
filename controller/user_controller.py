from app import app
from flask import request,jsonify
from model.user_model import user_model
from flask import request
obj=user_model()
@app.route("/user",methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()
@app.route("/user",methods=["POST"])
def user_add_controller():
    return obj.user_add_model(request.form)

@app.route("/user",methods=["PUT"])
def user_update_controller():
    if request.form:
        result = obj.user_update_model(request.form)
        return jsonify(result)  
    
@app.route("/user/<id>",methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)



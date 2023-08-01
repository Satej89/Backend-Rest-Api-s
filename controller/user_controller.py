from app import app
from flask import request
from model.user_model import user_model
from flask import request
obj=user_model()
@app.route("/user",methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()
@app.route("/user/add",methods=["POST"])
def user_add_controller():
    #print(request.form)
    return obj.user_add_model(request.form)



from app import app
from flask import request,jsonify
from model.user_model import user_model
import json
from datetime import datetime
from flask import request ,send_file
obj=user_model()

@app.route("/user",methods=["GET"])
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user",methods=["POST"])
def user_add_controller():
    return obj.user_add_model(request.form)

# @app.route("/user/<id>",methods=["PUT"])
# def user_update_controller(id):
#     if request.form:
#         result = obj.user_update_model(request.form,id)
#         return jsonify(result) ;
        
@app.route("/user",methods=["PUT"])
def user_update_controller():
    if request.form:
        result = obj.user_update_model(request.form)
        return result

@app.route("/user/<id>",methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route("/user/<id>",methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form,id)

@app.route("/user/<uid>/upload/avtar",methods=["PUT"])
def user_upload_controller(uid):
    file=request.files['avtar']
    
    unique_filename =str(datetime.now().timestamp()).replace(".","")
    print(unique_filename)
    filename_split=file.filename.split(".")
    exten= filename_split[len(filename_split)-1]
    final_path=f"Images/{unique_filename}.{exten}"
    file.save(final_path)

    return obj.user_upload_model(uid,final_path)

@app.route("/Images/<filename>")
def user_getavtar_controller(filename):
    return send_file(f"Images/{filename}")

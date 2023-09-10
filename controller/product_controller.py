from app import app
from flask import request,jsonify
from model.product_model import product_model
import json
from datetime import datetime
from flask import request ,send_file
obj=product_model()

@app.route("/product",methods=["GET"])
def product_getall_controller():
    return obj.product_getall_model()
  
@app.route("/product",methods=["POST"])
def product_add_controller():
    return obj.product_add_model(request.form)

@app.route("/product",methods=["PUT"])
def product_update_controller():
    if request.form:
        result = obj.product_update_model(request.form)
        return result
    
@app.route("/product/<id>",methods=["DELETE"])
def product_delete_controller(id):
    return obj.product_delete_model(id)

@app.route("/product/<id>",methods=["PATCH"])
def product_patch_controller(id):
    return obj.product_patch_model(request.form,id)

@app.route("/product/image/<uid>",methods=["PUT"])
def product_upload_controller(uid):
    file=request.files['image']
    
    unique_filename =str(datetime.now().timestamp()).replace(".","")
    print(unique_filename)
    filename_split=file.filename.split(".")
    exten= filename_split[len(filename_split)-1]
    final_path=f"Images/product_image/{unique_filename}.{exten}"
    file.save(final_path)
    return obj.product_upload_model(uid,final_path)










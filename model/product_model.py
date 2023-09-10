import mysql.connector
import json
from flask import make_response
class product_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Satej@892002",database="flask_project4")
            self.cur = self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("connection is successful.")
        except:
            print("some error in sql connection.......")
    def product_getall_model(self):
        self.cur.execute("SELECT * FROM product ")
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response( {"Payload":result},200)
            # return json.dumps(result)
        else:
            return make_response( {"Message":"No data is in there....."},204)

    def product_add_model(self,data):
        self.cur.execute(f"INSERT INTO product(name,description,image,price,company_name ,review) VALUES ('{data['name']}','{data['description']}','{data['image']}','{data['price']}','{data['company_name']}','{data['review']}')")
        return make_response( {"Message":"Product is added successfully in the database...."},201)
    
    def product_update_model(self,data):
        self.cur.execute(f"UPDATE product SET name='{data['name']}', description='{data['description']}', image='{data['image']}',company_name='{data['company_name']}',review='{data['review']}',price='{data['price']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response ({"Message":"Product Updated successfully in the database...."},201)
        else:
            return make_response ({"Message":"The id is not there so the product is not updated......."},204)

    def product_delete_model(self,id):
        self.cur.execute(f"DELETE FROM product WHERE id ={id}")
        if self.cur.rowcount>0:
            return make_response( {"Message":"The product is deleted successfully........"},200)
        else:
            return make_response({"Message":"The id is not present so the product is not delete......."},202)
        
    def product_patch_model(self,data,id):
        qry= "UPDATE product SET "
        for key in data:
            qry= qry + f"{key}='{data[key]}',"
        qry = qry[:-1]+f" WHERE id={id}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response ({"Message":"Product is Updated successfully.... "},201)
        else:
            return make_response ({"Message":"The Product is not updated......."},204)
    def product_upload_model(self,uid,path):
        self.cur.execute(f"UPDATE product SET image='{path}' WHERE id ={uid}")
        if self.cur.rowcount>0:
            return make_response ({"Message":"Image uploaded successfully...."},201)
        else:
            return make_response ({"Message":"Image is not able to update...."},204)












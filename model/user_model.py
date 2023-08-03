import mysql.connector
import json
from flask import make_response 
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Satej@892002",database="flask_project4")
            self.cur = self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("connection is successful.")
        except:
            print("some error in sql connection.......")
    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response( {"Payload":result},200)
            # return json.dumps(result)
        else:
            return make_response( {"Message":"No data is in there....."},204)
        
    def user_add_model(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role ,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        return make_response( {"Message":"User created successfully in the database...."},201)
    
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', role='{data['role']}',phone='{data['phone']}',password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response ({"Message":"User Updated successfully in the database...."},201)
        else:
            return make_response ({"Message":"The id is not there so the data is not updated......."},204)

    
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id ={id}")
        if self.cur.rowcount>0:
            return make_response( {"Message":"The data is deleted successfully........"},200)
        else:
            return make_response({"Message":"The id is not there so the data is not delete......."},202)
        

    def user_patch_model(self,data,id):
        qry= "UPDATE users SET "
        for key in data:
            qry= qry + f"{key}='{data[key]}',"
        qry = qry[:-1]+f" WHERE id={id}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response ({"Message":"User data is Updated successfully "},201)
        else:
            return make_response ({"Message":"The data is not updated......."},204)  
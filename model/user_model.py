import mysql.connector
import json
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
            return json.dumps(result)
        else:
            return "There is no data"
        
    def user_add_model(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role ,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        return "user created successfully in the database...."
    

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', role='{data['role']}',phone='{data['phone']}',password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return "The data is updated successfully........"
        else:
            return "The id is not there so the data is not updated......."

    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id ={id}")
        if self.cur.rowcount>0:
            return "The data is deleted successfully........"
        else:
            return "The id is not there so the data is not delete......."  
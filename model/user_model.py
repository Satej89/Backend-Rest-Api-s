import mysql.connector
import json
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Satej@892002",database="flask_project4")
            self.cur = self.con.cursor(dictionary=True)
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
        print(data['email'])
        return "this is user add new modedxlllllll"
    
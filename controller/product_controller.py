from app import app
@app.route("/product/add")
def prod_add():
    return "you are product add page"
from flask import render_template 
from app import app
from models.orderlist import orders

@app.route("/orders")
def index():
    return render_template("index.html", title="Home", all_orders=orders)
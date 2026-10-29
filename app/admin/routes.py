from app.admin import admin
from flask import render_template

@admin.route("/panel")
def panel():
    return render_template("panel.html")

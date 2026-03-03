from flask import Blueprint, render_template

main = Blueprint("main", __name__) # Serve para organizar rotas. O Blueprint ajuda a dividir isso em módulos

@main.route("/")
def index():
    return render_template("index.html")
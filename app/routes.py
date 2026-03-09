from flask import Blueprint, render_template, request, redirect, url_for
from app.database import SessionLocal
from app.models import Material
from decimal import Decimal

main = Blueprint("main", __name__) # Serve para organizar rotas. O Blueprint ajuda a dividir isso em módulos

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/materiais", methods=["GET", "POST"]) #GET mostrar a página. Post receber formulário
def materiais():
    session = SessionLocal()

    if request.method == "POST":
        nome = request.form["nome"]
        custo_unitario = Decimal(request.form["custo_unitario"])
        unidade = request.form["unidade"]

        novo_material = Material(
            nome=nome,
            custo_unitario=custo_unitario,
            unidade_medida=unidade
        )

        session.add(novo_material)
        session.commit()

        return redirect(url_for("main.materiais"))
    
    # buscar materiais no banco
    materiais = session.query(Material).all()

    session.close()

    return render_template("materiais.html", materiais=materiais)

@main.route("/excluir_material/<int:id>")
def excluir_material(id):
    session = SessionLocal()

    material = session.query(Material).get(id)

    if material:
        session.delete(material)
        session.commit()

    session.close()

    return redirect(url_for("main.materiais"))

@main.route("/editar_material/<int:id>", methods=["GET", "POST"])
def editar_material(id):
    session = SessionLocal()
    material = session.query(Material).get(id)

    if request.method == "POST":
        material.nome = request.form["nome"]
        material.custo_unitario = Decimal(request.form["custo_unitario"])
        material.unidade_medida = request.form["unidade"]

        session.commit()
        session.close()

        return redirect(url_for("main.materiais"))
    
    return render_template("editar_material.html", material=material)
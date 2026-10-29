
from app.blog import blog
from flask import render_template

@blog.route("/entrada/<int:id>")
def entrada(id):
    titulos = {
        1: "Primera entrada del blog",
        2: "Segunda entrada del blog",
        3: "Tercera entrada del blog"
    }

    titulo = titulos.get(id, "Entrada no encontrada")

    return render_template("entrada.html", titulo=titulo)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    lista = [
        "Farinha",
        "Açúcar Mascavo",
        "Ovo",
        "Achocolatado",
        "Fermento",
        "Leite",
        "Amor",
    ]

    return render_template(
        "home.html", 
        nome="guilherme",
        ingredientes=lista
    )

@app.route('/seila')
def seila():
    return render_template("seila.html")

@app.route('/turmas')
def turmas():
    return render_template("turmas.html")

@app.route('/professor')
def professor():
    return render_template("professor.html")

@app.route('/ambiente')
def ambiente():
    return render_template("ambiente.html")

app.run()

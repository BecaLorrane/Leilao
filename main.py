from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/index.html")
def buttonVoltar():
    return render_template("index.html")

@app.route("/principal.html")
def buttonEntrar():
    return render_template("principal.html")


@app.route("/login.html")
def login():
    return render_template("login.html")


@app.route("/cadastro.html")
def cadastro():
    return render_template("cadastro.html")


@app.route("/tesla1.html")
def buttonLance1():
    return render_template("tesla1.html")

@app.route("/tesla2.html")
def buttonLance2():
    return render_template("tesla2.html")

@app.route("/tesla3.html")
def buttonLance3():
    return render_template("tesla3.html")

@app.route("/index.html")
def buttonVoltarCadastro():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask,render_template

app = Flask(__name__)

#ruta raiz
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/grados/<int:valor>")
def convertir(valor):
    return render_template("grados.html", resultado = valor * 9/5 + 32)

@app.route("/prestamo/<int:monto>")
def prestamo(monto):
    return render_template("prestamo.html", resultado = monto * 0.1897 / 0.1897 + 1 - 1 - 3) 
    
if __name__ == "__main__":
    app.run(debug=True)
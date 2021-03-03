from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Index():
    


    return  render_template("Index.html")

@app.route("/clientes")
def clietes():
    clientes = [
        (0, 'Ethan', 'Soto', 8093327742, 'ethanmanu3l@gmail.com', 'SantoDomingo'),
        (1, ' Mildred ', 'Santos', 8093329951, 'mildredsant0@gmail.com', 'PueroPlata'),
        (2, 'Carlos', 'Bejarán', 8295429962, 'carlosBB@gmail.com', 'LaVega'),
        (3, 'Juan', 'Martinez', 8099412280, 'juancito2210P@gmail.com', 'Santo Domingo'),
        (4, 'Elizardo', 'Sosa', 8094518033, 'elisosa30S0S@gmail.com', 'Higuey')
    ]
    return  render_template("clientes.html", clientes = clientes)

@app.route("/register")
def register():
    
    return  render_template("register.html")



if __name__ == "__main__":
    app.run(debug=True)
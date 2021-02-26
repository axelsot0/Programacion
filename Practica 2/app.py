
from flask import Flask,render_template

app = Flask(__name__)

#ruta raiz
@app.route('/')
def index():
    
    return render_template('index.html')

# En el backend definir una lista de clientes que contenga diccionarios con las siguientes claves: Id, Nombre, Apellido, Telefono, email, Ciudad # 
@app.route('/clientes')
def clientes():
    usuario = [
        (0, 'Ethan', 'Soto', 8093327742, 'ethanmanu3l@gmail.com', 'SantoDomingo'),
        (1, ' Mildred ', 'Santos', 8093329951, 'mildredsant0@gmail.com', 'PueroPlata'),
        (2, 'Carlos', 'Bejarán', 8295429962, 'carlosBB@gmail.com', 'LaVega'),
        (3, 'Juan', 'Martinez', 8099412280, 'juancito2210P@gmail.com', 'Santo Domingo'),
        (4, 'Elizardo', 'Sosa', 8094518033, 'elisosa30S0S@gmail.com', 'Higuey')
    ]


    return render_template("clientes.html", usuario=usuario)  
    
@app.route('/id/<int:iden>')
def idntificación(iden):

    iden = {0, 1,  2,  3,  4}

  
    return render_template('id.html', iden = iden)
    



    
if __name__ == "__main__":
    app.run(debug=True)
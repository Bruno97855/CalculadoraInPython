from flask import Flask, jsonify, request 
from flask_cors import CORS
from Calculadora import autores, dec2any, any2dec
app = Flask(__name__)
CORS(app)

@app.route('/autores', methods=['GET'])
def get_books():
    lista_autores = autores()
    return jsonify(lista_autores)

@app.route('/calcular/<string:numero>/<int:base>/<int:calcType>', methods=['GET'])
def get_calc(numero,base,calcType):
    result = ""
    if calcType == 1:
        result = dec2any(numero, base)
    elif calcType == 2:
        result = any2dec(numero, base)

    if result != "":
        return jsonify(result)
    return jsonify({"message": "Erro no calculo"}), 404

if __name__ == '__main__':
    app.run(debug=True)
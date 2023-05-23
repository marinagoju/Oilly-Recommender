from flask import Flask, render_template, request
import pickle
import Utilities
import Recomendador_script as rs

application = Flask(__name__)


@application.route('/')
def man():
    return render_template('home.html')


@application.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    indices = rs.recomendador(str(data1)).index.tolist()
    solucion= str(indices)
    return solucion

if __name__ == "__main__":
    application.run(debug=True)
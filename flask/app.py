from flask import Flask, render_template, request
import pickle
import numpy as np
import Recomendador_script as rs


app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    arr = np.array([[data1]])
    pred = rs.recomendador(str(arr))
    return pred


if __name__ == "__main__":
    app.run(debug=True)

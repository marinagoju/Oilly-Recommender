from flask import Flask, render_template, request
import Recomendador_script as rs
import pickle

model = pickle.load(open('modelo.pkl','rb'))

application = Flask(__name__)


@application.route('/')
def man():
    return render_template('home.html')


@application.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    indices = rs.recomendador(str(data1)).index.tolist()
    return str(indices)


if __name__ == "__main__":
    application.run(debug=True)

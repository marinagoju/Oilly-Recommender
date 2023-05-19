from flask import Flask, render_template, request
import Recomendador_script as rs


app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    indices = rs.recomendador(str(data1)).index.tolist()
    return str(indices)


if __name__ == "__main__":
    app.run(debug=True)

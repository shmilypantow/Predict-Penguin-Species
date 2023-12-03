from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('modelpenguin.sav', 'rb'))


@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    culmen_lenght = float(request.form['culmen_lenght'])
    culmen_depth = float(request.form['culmen_depth'])
    flipper_lenght = float(request.form['flipper_lenght'])
    body_mass = float(request.form['body_mass'])
    result = model.predict([[culmen_lenght, culmen_depth, flipper_lenght, body_mass]])[0]
    return render_template('index.html',**locals())


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')



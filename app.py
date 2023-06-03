import numpy as np
from flask import Flask, request, render_template
import pickle
import seaborn

app = Flask(__name__, template_folder='Templates')  # Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))
print("Model loaded")


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        wine = float(request.form["wname"])
        fixed_acidity = float(request.form["facid"])
        volatile_acidity = float(request.form["vacid"])
        citric_acid = float(request.form["cacid"])
        residual_sugar = float(request.form["rsugar"])
        chlorides = float(request.form["cl"])
        free_sulfur_dioxide = float(request.form["fsd"])
        total_sulfur_dioxide = float(request.form["tsd"])
        density = float(request.form["den"])
        pH = float(request.form["pH"])
        sulphates = float(request.form["phate"])
        alcohol = float(request.form["batch"])

        input_lst = [[wine, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
                     total_sulfur_dioxide, density, pH, sulphates, alcohol]]
        input_arr = np.asarray(input_lst)
        input_reshape = input_arr.reshape(1, -1)
        pred = model.predict(input_reshape)
        print(pred)

        if pred[0] == 1:
            return render_template('Good.html')
        else:
            return render_template('Bad.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

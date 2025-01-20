import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the machine learning model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    age = float(request.form['age'])
    sex = request.form['sex']
    cp = float(request.form['cp'])
    restbps = float(request.form['restbps'])
    chol = float(request.form['chol'])
    fbs = float(request.form['fbs'])
    restecg = float(request.form['restecg'])
    thalach = float(request.form['thalach'])
    exang = float(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = float(request.form['slope'])
    ca = float(request.form['ca'])
    thal = float(request.form['thal'])

    # Perform one-hot encoding for sex
    sex = 1 if sex == 'male' else 0
    sex = 1 if sex == 'female' else 0
    # Make prediction using the loaded model
    prediction = model.predict([[age, sex, cp, restbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if prediction == 0:
        result = "Patient Does not have any heart disease detected."
    else:
        result = "Patient has heart disease he needs more tests."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

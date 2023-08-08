from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('D:/ML/Project 1/random_forest_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input for all 14 attributes
        crim = float(request.form['crim'])
        zn = float(request.form['zn'])
        indus = float(request.form['indus'])
        chas = int(request.form['chas'])
        nox = float(request.form['nox'])
        rm = float(request.form['rm'])
        age = float(request.form['age'])
        dis = float(request.form['dis'])
        rad = float(request.form['rad'])
        tax = float(request.form['tax'])
        ptratio = float(request.form['ptratio'])
        b = float(request.form['b'])
        lstat = float(request.form['lstat'])
        medv = float(request.form['medv'])

        # Perform input validation
        if not(0 <= crim <= 100) or not(0 <= zn <= 100) or not(0 <= indus <= 100) or not(0 <= chas <= 1) or \
           not(0 <= nox <= 1) or not(1 <= rm <= 10) or not(0 <= age <= 100) or not(0 <= dis <= 20) or \
           not(0 <= rad <= 24) or not(100 <= tax <= 1000) or not(10 <= ptratio <= 30) or not(300 <= b <= 400) or \
           not(0 <= lstat <= 100) or not(5 <= medv <= 50):
            raise ValueError("Invalid input range")

        # Prepare input features for prediction
        input_data = [[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat, medv]]

        # Make the prediction
        prediction = model.predict(input_data)[0]

        return render_template('index.html', prediction=prediction)
    except ValueError as e:
        return render_template('index.html', prediction=str(e))
    except:
        return render_template('index.html', prediction="Invalid input")

if __name__ == '__main__':
    app.run(debug=True)

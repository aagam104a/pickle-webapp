from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pickled model
with open(r'C:\Users\Admin\Desktop\CARDIO_PROJECT\pickle-webapp\random_forest_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs from the form
    features = [
        float(request.form['general_health']),
        float(request.form['checkup']),
        float(request.form['exercise']),
        float(request.form['depression']),
        float(request.form['diabetes']),
        float(request.form['arthritis']),
        float(request.form['age_category']),
        float(request.form['sex_Male']),
        float(request.form['sex_Female']),
        float(request.form['height']),
        float(request.form['weight']),
        float(request.form['bmi']),
        float(request.form['alcohol_consumption']),
        float(request.form['fruit_consumption']),
        float(request.form['vegetables_consumption']),
        float(request.form['potato_consumption']),
        float(request.form['smoking_history_No']),
        float(request.form['smoking_history_Yes'])
    ]

    # Create a feature array from the user inputs
    user_input = [features]

    # Use the loaded model to make predictions
    prediction = loaded_model.predict(user_input)

    # Display the prediction
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)


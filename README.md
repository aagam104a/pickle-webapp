# Cardio Forecast Web Application

This is a simple web application built using Flask and Python for predicting the risk of Cardiovascular Disease based on user input. The application uses a Random Forest Classifier model trained on relevant features.

## Requirements

- Python 3.x
- Flask
- pickle (for loading the trained model)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
Install the required dependencies:

bash
Copy code
pip install flask
Usage
Run the Flask application:

bash
Copy code
python app.py
Open your web browser and go to http://localhost:5000 to access the web application.

Fill in the form with the required information:

General health
Checkup frequency
Exercise frequency
Depression status
Diabetes status
Arthritis status
Age category
Sex
Height
Weight
BMI (Body Mass Index)
Alcohol consumption
Fruit consumption
Vegetables consumption
Potato consumption
Smoking history
Click the "Predict" button to see the predicted risk of Cardiovascular Disease.

File Structure
app.py: Main Flask application file containing the routes and model prediction logic.
templates/: Directory containing HTML templates for the web pages.
index.html: HTML template for the home page with the form.
result.html: HTML template for displaying the prediction result.
static/: Directory containing static files such as CSS stylesheets and images.
random_forest_model.pkl: Pickled trained Random Forest Classifier model for predicting the risk of Cardiovascular Disease.

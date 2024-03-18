# 🩺 Cardio Forecast Web Application

This is a simple web application built using Flask and Python for predicting the risk of Cardiovascular Disease based on user input. The application uses a Random Forest Classifier model trained on relevant features.

## 📋 Requirements

- Python 3.9.0 or Above
- Flask (Backend Framework)
- pickle (for loading the trained model)

## 💻 Installation

1. Clone the repository:

   \`\`\`bash
   git clone (https://github.com/aagam104a/Cardio_Forecast_pickle-webapp.git)
   \`\`\`

2. Install the required dependencies:

   \`\`\`bash
   pip install flask
   \`\`\`

## 🚀 Usage

1. Run the Flask application:

   \`\`\`bash
   python app.py
   \`\`\`

2. Open your web browser and go to \`http://localhost:5000\` to access the web application.

3. Fill in the form with the required information:

   - General health
   - Checkup frequency
   - Exercise frequency
   - Depression status
   - Diabetes status
   - Arthritis status
   - Age category
   - Sex
   - Height
   - Weight
   - BMI (Body Mass Index)
   - Alcohol consumption
   - Fruit consumption
   - Vegetables consumption
   - Potato consumption
   - Smoking history

4. Click the \"Predict\" button to see the predicted risk of Cardiovascular Disease.

## 📁 File Structure

- \`app.py\`: Main Flask application file containing the routes and model prediction logic.
- \`templates/\`: Directory containing HTML templates for the web pages.
  - \`index.html\`: HTML template for the home page with the form.
  - \`result.html\`: HTML template for displaying the prediction result.
- \`static/\`: Directory containing static files such as CSS stylesheets and images.
- \`random_forest_model.pkl\`: Pickled trained Random Forest Classifier model for predicting the risk of Cardiovascular Disease.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details." > README.md

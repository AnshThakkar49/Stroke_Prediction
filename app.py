from flask import Flask, render_template, request
import joblib
import numpy as np

#Initializing Flas app
app = Flask(__name__)

#Load trained model
model = joblib.load("Stroke_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the form
        user_input = [float(x) for x in request.form.values()]

        #Make prediction 
        prediction = model.predict(input_array)[0]

        # Show result
        result = "High Risk of Stroke" if prediction == 1 else "Low risk of Stroke"
        return render_tempelate("index.html", prediction_text=f"Prediction: {result}")
    
    except:
        return f"Error: {e}"
    
if __name__ == "__main__":
    app.run(debug=True)
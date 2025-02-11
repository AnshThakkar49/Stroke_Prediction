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
        # Get user input but IGNORE height & weight (index 3 & 4)
        form_values = list(request.form.values())
        user_input = [float(form_values[i]) for i in range(len(form_values)) if i not in [8, 9]]

        # Validate that hypertension & heart_disease are 0 or 1
        #if user_input[1] not in [0, 1] or user_input[2] not in [0, 1]:
        #    return render_template("index.html", prediction_text="❌ Error: Hypertension & Heart Disease must be 0 or 1.")

        # Convert to NumPy array and reshape
        input_array = np.array(user_input).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)[0]

        # Show result
        result = "High Risk of Stroke" if prediction == 1 else "Low Risk of Stroke"
        return render_template("index.html", prediction_text=f"Prediction: {result}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")
    
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the model and label encoder
model = load_model('pothole_detection_model.h5')
label_encoder = LabelEncoder()
label_encoder.fit(["normal road", "pothole"])  # Assuming these two classes

# Function to preprocess the uploaded data and make predictions
def preprocess_and_predict(file):
    # Read the CSV file
    df = pd.read_csv(file)

    # Preprocess the data
    X = df.drop(columns=['time', 'label'])  # Drop 'time' and 'label' columns
    prediction = model.predict(X)

    # Get the prediction as 'pothole' or 'normal road'
    results = []
    for pred in prediction:
        label = label_encoder.inverse_transform((pred > 0.5).astype(int))
        results.append(label[0])

    return results

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    # Process the file and get the prediction
    results = preprocess_and_predict(file)
    
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import joblib

app = Flask(_name_)

# Load the trained model
model = joblib.load('classification.pkl')

@app.route('/prediction', methods=['POST'])
def prediction():
    # Check if an audio file was sent
    if 'file' not in request.files:
        return jsonify({'error': 'No audio file uploaded'})

    audio_file = request.files['file']

    # Convert the audio file to JSON format
    # Your audio processing code here...

    # Make predictions using the model
    # Your prediction code here...

    # Example response
    result = {
        'prediction': 'Your predicted output'
    }

    return jsonify(result)

if _name_ == '_main_':
    app.run()
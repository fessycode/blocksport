from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    team1 = request.form.get('team1')
    team2 = request.form.get('team2')

    # Perform feature engineering based on your model's requirements
    features = [team1, team2]  # Placeholder for demonstration

    # Make a prediction using the loaded model
    prediction = model.predict([features])[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

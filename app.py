from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('OPENWEATHER_API_KEY') 

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather_data():
    # Get location from query string
    location = request.args.get('location', type=str)  

    # Return error if no location provided
    if not location:
        return jsonify({'error': 'Missing location parameter'}), 400

    try:
        # Request weather data from OpenWeatherMap API
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Log the error and return a server error response
        print(e)
        return jsonify({'error': 'Error fetching data from OpenWeatherMap API'}), 500

    try:
        # Return the JSON response
        return jsonify(response.json())  
    except ValueError:
        # Return an error if the response is not valid JSON
        return jsonify({'error': 'Non-JSON response from OpenWeatherMap API'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  

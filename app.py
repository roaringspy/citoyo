from flask import Flask, request, render_template, jsonify
import threading
import time
import random

app = Flask(__name__)

# Global variables
generated_html_output = None
processing_complete = False
input_params = {}

def run_script_and_capture_output(city_name):
    global generated_html_output, processing_complete, input_params
    # city_name = input_params.get('city_name', 'Unknown City')
    # Simulate HTML generation (replace with your actual logic)
    # Here, we just read the content of the city's HTML file from the static folder
    try:
        with open(f'static/{city_name}.html', 'r') as f:
            generated_html_output = f.read()
    except FileNotFoundError:
        generated_html_output = f"<h1>Error: City data not found for {city_name}</h1>"
    except Exception as e:
        generated_html_output = f"<h1>Error processing city data: {str(e)}</h1>"
    
    processing_complete = True


@app.route('/', methods=['GET', 'POST'])
def index():
    global generated_html_output, processing_complete, input_params
    cities = ["Ahmedabad", "Pune", "Delhi"]  # Example cities - Match filenames

    if request.method == 'POST':
        city_name = request.form['city_name']
        input_params = {
            'city_name': city_name
        }
        generated_html_output = None  # Reset output for new request
        processing_complete = False  # Reset processing status for new request
        threading.Thread(target=run_script_and_capture_output, args=(city_name,)).start()
        return '', 200  # No content response, using AJAX

    return render_template('index.html', cities=cities)

@app.route('/output')
def output():
    global generated_html_output, processing_complete
    if processing_complete:
        return jsonify({'html_output': generated_html_output})
    else:
        return jsonify({'html_output': None})

if __name__ == '__main__':
    app.run(debug=True)
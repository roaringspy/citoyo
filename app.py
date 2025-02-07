from flask import Flask, request, render_template, jsonify
import threading
import time
import random

app = Flask(__name__)

# Global variables
generated_html_output = None
processing_complete = False
input_params = {}

def run_script_and_capture_output():
    global generated_html_output, processing_complete, input_params
    city_name = input_params.get('city_name', 'Unknown City')
    processing_complete = True

@app.route('/', methods=['GET', 'POST'])
def index():
    global generated_html_output, processing_complete, input_params
    cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]  # Example cities

    if request.method == 'POST':
        input_params = {
            'city_name': request.form['city_name']
        }
        generated_html_output = None
        processing_complete = False
        threading.Thread(target=run_script_and_capture_output).start()
        return '', 204  # No content response, as we're using AJAX

    return render_template('index.html', cities=cities)

@app.route('/output')
def output():
    global generated_html_output, processing_complete
    if processing_complete:
        output_to_send = generated_html_output
        generated_html_output = None
        processing_complete = False
        return jsonify({'html_output': output_to_send})
    else:
        return jsonify({'html_output': None})

if __name__ == '__main__':
    app.run(debug=True)

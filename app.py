from flask import Flask, request, render_template, jsonify
import subprocess
import time  # For adding a delay
import threading # For running script in background

app = Flask(__name__)

# Global variable to store the generated HTML output
generated_html_output = None
processing_complete = False # Flag to indicate processing status

def run_script_and_capture_output(city_name):
    global generated_html_output, processing_complete
    generated_html_output = None # Reset output
    processing_complete = False # Reset flag
    time.sleep(5) # Minimum 5 second delay - ensure loading page is visible
    try:
        process = subprocess.run(
            ['python', 'your_script.py', city_name],
            capture_output=True,
            text=True,
            check=True
        )
        generated_html_output = process.stdout
    except subprocess.CalledProcessError as e:
        generated_html_output = f"Error running script: {e}<br><pre>{e.stderr}</pre>"
    except FileNotFoundError:
        generated_html_output = "Error: Python script 'your_script.py' not found."
    finally:
        processing_complete = True # Mark processing as complete


@app.route('/', methods=['GET', 'POST'])
def index():
    global generated_html_output, processing_complete
    generated_html_output = None # Reset output when index page is loaded initially
    processing_complete = False # Reset processing flag
    if request.method == 'POST':
        city_name = request.form['city_name']

        # Start the script execution in a background thread
        thread = threading.Thread(target=run_script_and_capture_output, args=(city_name,))
        thread.start()

        return render_template('loading.html') # Immediately render loading page

    return render_template('index.html', html_output=None) # Initial page load


@app.route('/output')
def output():
    global generated_html_output, processing_complete
    if processing_complete:
        output_to_send = generated_html_output
        generated_html_output = None # Clear output after sending once if you want to reset for next request. Remove if you want to keep the last output accessible.
        processing_complete = False # Reset processing flag for next request. Remove if you want to keep it true.
        return jsonify({'html_output': output_to_send})
    else:
        return jsonify({'html_output': None}) # Not ready yet


if __name__ == '__main__':
    app.run(debug=True)
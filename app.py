from flask import Flask, request, send_from_directory
import os
import pandas as pd
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = './uploads'
app.config['RESULT_FOLDER'] = './results'

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Read the uploaded Excel file
        data = pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Convert the data into a process log
        event_log = log_converter.apply(data)

        # Discover the Directly-Follows Graph of the process
        dfg = dfg_discovery.apply(event_log)

        # Save the DFG as a .txt file
        with open(os.path.join(app.config['RESULT_FOLDER'], 'result.txt'), 'w') as f:
            f.write(str(dfg))

        return send_from_directory(app.config['RESULT_FOLDER'], 'result.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
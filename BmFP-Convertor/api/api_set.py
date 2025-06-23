from flask import Flask, request, jsonify
from clinical_analysis import clinical_ecg_analysis
from dat_to_csv import convert_dat_to_csv
from read_ecg import plot_ecg_segments
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def index():
    return "Welcome to BmFP Convertor API!"

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/access', methods=['POST'])
def analyze_ecg():
    if 'FileDAT' not in request.files or 'FileHEA' not in request.files:
        print("Missing required files in the request.")
        return jsonify({"error": "Both .dat and .hea files are required"}), 400
    
    file_dat = request.files['FileDAT']
    file_hea = request.files['FileHEA']

    print("Received request to analyze ECG data.")
    print(f"FileDAT: {file_dat.filename}, FileHEA: {file_hea.filename}")
  
    save_dir = './BMFP-Dataset'
    os.makedirs(save_dir, exist_ok=True)

    file_dat_path = os.path.join(save_dir, secure_filename(file_dat.filename))
    file_hea_path = os.path.join(save_dir, secure_filename(file_hea.filename))

    file_dat.save(file_dat_path)
    file_hea.save(file_hea_path)

    base_filename = os.path.splitext(file_dat.filename)[0]
    base_path = os.path.join(save_dir, base_filename)


    try:
        convert_dat_to_csv(base_path)
        plot_ecg_segments(base_path)
        results = clinical_ecg_analysis(base_path)

        return jsonify({
            "message": "ECG analyzed successfully.",
            "results": results
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




class api_set:
    app = app

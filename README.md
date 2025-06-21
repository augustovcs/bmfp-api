# BMFP-API

BMFP-API is a backend-focused biomedical signal processing system that allows you to analyze ECG signals from raw `.dat` and `.hea` files (WFDB format). The project uses Python tools such as [WFDB](https://github.com/MIT-LCP/wfdb-python) and [NeuroKit2](https://github.com/neuropsychology/NeuroKit) to extract clinical features from ECG data, generate plots, and export `.csv` and `.png` files for use in professional or research contexts.

This project is designed to be used as a backend service integrated with an ASP.NET Web API, where the user uploads files and receives clinical data and visual outputs in return.

---

## 🔧 Features

- Reads ECG signals from `.dat` and `.hea` files using WFDB.
- Extracts key clinical metrics:  
  - Mean Heart Rate (bpm)  
  - Mean RR Interval (s)  
  - Approximate QRS Duration (ms)  
- Generates clean `.csv` files of the signal.
- Produces a segmented ECG plot as a `.png`.
- Easy to integrate into an ASP.NET backend for web-based analysis.

---

## 📁 Project Structure
```
BMFP-Convertor/
├── BMFP-Dataset/
│ ├── dataset01.dat
│ └── dataset01.hea
├── dat_to_csv.py
├── plot_segments.py
├── clinical_analysis.py
├── main.py
└── output/
├── dataset01.csv
└── ecg_1minute_plot.png
```

---

## 🚀 How to Run

1. **Install dependencies:**

Make sure you have Python 3.9+ and install the following:

```
pip install wfdb neurokit2 matplotlib pandas numpy pywt
```

Add your WFDB files (.dat and .hea):
Place your dataset in the BMFP-Dataset/ folder, for example:

BMFP-Dataset/
├── dataset01.dat
└── dataset01.hea


Run the analysis:
```
python main.py
```

This will:
Convert the .dat signal to .csv
Plot the first minute of ECG into ecg_1minute_plot.png
Print clinical metrics in the terminal

🧠 Example Output
```
Conversion completed successfully.
ECG segments plotted successfully.
Mean Heart Rate (bpm): 73.42
RR Interval Mean (s): 0.83
QRS Duration Mean (ms): 94.2
```

🌐 ASP.NET Integration
This Python backend is designed to work alongside an ASP.NET API project. You can:
Upload .dat and .hea files via a POST request
Trigger the Python script from your ASP.NET controller
Return the .csv, .png, and metrics as an API response

For example, use Process.Start() in ASP.NET to call main.py with the uploaded files' path.

📄 License
This project is open-source and free to use under the MIT License.

👨‍⚕️ Author
Developed by [Augusto Viegas] as part of a biomedical signal analysis toolkit for backend applications.

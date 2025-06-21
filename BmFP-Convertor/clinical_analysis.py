import wfdb
import neurokit2 as nk
import numpy as np
import pandas as pd

def clinical_ecg_analysis(record_path):
    # Load ECG
    record = wfdb.rdrecord(record_path)
    fs = record.fs
    ecg_raw = record.p_signal[:, 0]  # Use first channel (e.g., MLII)

    # Clean ECG signal
    ecg_cleaned = nk.ecg_clean(ecg_raw, sampling_rate=fs)
    peaks, info = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)



    # Detect R-peaks
    peaks, info = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)

    # RR intervals (seconds)
    rr_intervals = np.diff(info["ECG_R_Peaks"]) / fs

    # Mean Heart Rate (bpm)
    mean_hr = 60 / np.mean(rr_intervals)

    # QRS duration (approximate using peak signal width)
    signals, waves = nk.ecg_delineate(ecg_cleaned, rpeaks=info["ECG_R_Peaks"], sampling_rate=fs, method="peaks")

    q_peaks = signals["ECG_Q_Peaks"]
    s_peaks = signals["ECG_S_Peaks"]


    valid = (~q_peaks.isna()) & (~s_peaks.isna())

    qrs_durations_samples = s_peaks[valid].index - q_peaks[valid].index
    qrs_duration_ms = (qrs_durations_samples.to_series() / fs * 1000).mean()


    return {
        "Mean Heart Rate (bpm)": round(mean_hr, 2),
        "RR Interval Mean (s)": round(np.mean(rr_intervals), 3),

"""    In testing - need to ensure that the QRS duration is calculated correctly """ 
        "QRS Duration Mean (ms)": round(qrs_duration_ms, 2)

        #"HRV Summary": hrv_metrics.to_dict(orient='records')[0]
    }




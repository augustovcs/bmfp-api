import wfdb
import neurokit2 as nk
import numpy as np

def clinical_ecg_analysis(record_path):
    # Load ECG
    record = wfdb.rdrecord(record_path)
    fs = record.fs
    ecg_raw = record.p_signal[:, 0]  # Use first channel

    # Clean ECG signal
    ecg_cleaned = nk.ecg_clean(ecg_raw, sampling_rate=fs, method="neurokit")
    
    # Detect R-peaks
    peaks, info = nk.ecg_peaks(ecg_cleaned, method="christov", show=False)

    if len(info["ECG_R_Peaks"]) < 2:
        return {"error": "Insufficient R-peaks detected"}

    # RR intervals
    rr_intervals = np.diff(info["ECG_R_Peaks"]) / fs
    mean_hr = 60 / np.mean(rr_intervals)

    # Delineate waveforms
    try:
        signals, _ = nk.ecg_delineate(
            ecg_cleaned, 
            rpeaks=info["ECG_R_Peaks"], 
            sampling_rate=fs, 
            method="dwt",
            show=False
        )
    except Exception as e:
        return {"error": f"Delineation failed: {str(e)}"}

    # QRS duration calculation
    qrs_durations_ms = []
    valid_qs_pairs = 0
    
    for i in range(len(info["ECG_R_Peaks"]) - 1):
        current_r = info["ECG_R_Peaks"][i]
        next_r = info["ECG_R_Peaks"][i + 1]
        
        q = [q for q in signals.get("ECG_Q_Peaks", []) 
             if current_r < q < next_r]
        s = [s for s in signals.get("ECG_S_Peaks", []) 
             if current_r < s < next_r]
        
        if q and s:
            qrs_duration = (s[0] - q[0]) / fs * 1000
            if 20 < qrs_duration < 200:
                qrs_durations_ms.append(qrs_duration)
                valid_qs_pairs += 1

    # Segment processing
    segment_length = 60 * fs
    results = []
    
    for i in range(0, len(ecg_cleaned), segment_length):
        segment_end = min(i + segment_length, len(ecg_cleaned))
        segment_duration = (segment_end - i) / fs
        
        segment_result = {
            "segment_start": i / fs,
            "segment_end": segment_end / fs,
            "segment_duration": segment_duration,
            "mean_hr": round(mean_hr, 2),
            "rr_interval_mean": round(np.mean(rr_intervals), 3),
            "valid_qs_pairs": valid_qs_pairs
        }
        
        if qrs_durations_ms:
            segment_result.update({
                "qrs_duration_mean": round(np.mean(qrs_durations_ms), 2),
                "qrs_duration_std": round(np.std(qrs_durations_ms), 2),
                "qrs_duration_range": [
                    round(min(qrs_durations_ms), 2),
                    round(max(qrs_durations_ms), 2)
                ]
            })
        else:
            segment_result["qrs_duration"] = "Not measurable"
        
        results.append(segment_result)

    return {
        "overall_analysis": {
            "total_beats": len(info["ECG_R_Peaks"]),
            "total_valid_qs_pairs": valid_qs_pairs
        },
        "segments": results
    }
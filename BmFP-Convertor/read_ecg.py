import wfdb
import matplotlib.pyplot as plt

def plot_ecg_segments(record_path, total_seconds=60, num_segments=4):
    """
    Plots an ECG signal divided into segments.

    Parameters:
        record_path (str): Path (without extension) to the WFDB record files (.dat and .hea).
        total_seconds (int): Total seconds of signal to plot.
        num_segments (int): Number of segments to split the plot into.
    """
    # Read the ECG record
    record = wfdb.rdrecord(record_path)
    
    fs = record.fs
    signal = record.p_signal[:, 0]  # First channel (e.g. MLII)
    time = [i / fs for i in range(len(signal))]

    total_samples = int(fs * total_seconds)
    samples_per_segment = total_samples // num_segments

    fig, axs = plt.subplots(num_segments, 1, figsize=(12, 8), sharex=False)

    for i in range(num_segments):
        start = i * samples_per_segment
        end = start + samples_per_segment
        axs[i].plot(time[start:end], signal[start:end], color='blue')
        axs[i].set_title(f'Segment {i+1} ({i * (total_seconds//num_segments)}-{(i+1) * (total_seconds//num_segments)} s)')
        axs[i].set_ylabel('Amplitude (mV)')
        axs[i].grid(True)

    axs[-1].set_xlabel('Time (s)')
    plt.tight_layout()
    plt.suptitle(f'ECG Signal - MLII Channel ({total_seconds} Seconds in {num_segments} Segments)', y=1.02)

    plt.savefig("ecg_1minute_plot.png", dpi=300)
    plt.show()


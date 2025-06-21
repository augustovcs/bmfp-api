from read_ecg import plot_ecg_segments
from dat_to_csv import convert_dat_to_csv
from clinical_analysis import clinical_ecg_analysis
if __name__ == "__main__":
    convert_dat_to_csv('./BMFP-Dataset/dataset01', './BMFP-Dataset/dataset01.csv')
    print("Conversion completed successfully.")

    analysis_results = clinical_ecg_analysis('./BMFP-Dataset/dataset01')
    for key, value in analysis_results.items():
        print(f"{key}: {value}")

    

    plot_ecg_segments('./BMFP-Dataset/dataset01', total_seconds=60, num_segments=4)
    print("ECG segments plotted successfully.")



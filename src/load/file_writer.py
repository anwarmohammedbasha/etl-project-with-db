"""
file_writer.py — Optionally save transformed data to CSV or cloud storage
"""
import os

def write_csvs(data_dict, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for name, df in data_dict.items():
        path = os.path.join(output_dir, f"{name}.csv")
        df.to_csv(path, index=False)

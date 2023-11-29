import os
import re
import csv

# Define a function to extract energy values from the OUTCAR file
def extract_last_energy_from_outcar(file_path):
    energy_pattern = r"energy\s+without\s+entropy\s+=\s+([-+]?\d*\.\d+|\d+)"
    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.findall(energy_pattern, content)
        if matches:
            last_energy_value = matches[-1]  # Get the energy value of the last match
            return last_energy_value
    return None

# Specify the target directory path
base_directory = r"E:\SolidBattery_YanHuang\ads_K\7"

# Get all subdirectories in the target folder
dirs = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]

# Create a CSV file to save the results
csv_file_path = "energy_results.csv"

# Open the CSV file and write the header
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Directory", "Last Energy"])

    # Loop through subdirectories
    for dir_name in dirs:
        dir_path = os.path.join(base_directory, dir_name)
        outcar_path = os.path.join(dir_path, "OUTCAR")

        # Check if the OUTCAR file exists
        if os.path.exists(outcar_path):
            last_energy_value = extract_last_energy_from_outcar(outcar_path)

            # If successfully extracted the last energy value, write to the CSV file
            if last_energy_value is not None:
                csv_writer.writerow([dir_name, last_energy_value])

print("Extraction completed and written to the CSV file.")

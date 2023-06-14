import os
import pandas as pd

def merge_csvs(folder_path, output_file):
    files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
    if not files:
        print("No CSVs in this folder 🤨")
        return

    dfs = []
    common_columns = None

    for file in files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)

        if common_columns is None:
            common_columns = df.columns.tolist()
        else:
            # Check if the columns are matching
            if df.columns.tolist() != common_columns:
                print(f"Columns in '{file}' don't match the rest 😐")
                continue

        # Add a new column with source CSV
        df['Source'] = file

        dfs.append(df)

    if not dfs:
        print("No CSVs with matching columns found 😵")
        return

    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f"CSVs have been merged and saved to '{output_file}' 🤗")

# Get the location where the script is
script_dir = os.getcwd()

# Output file name
output_file = "merged.csv"

# Merge all CSVs in the current location
merge_csvs(script_dir, output_file)

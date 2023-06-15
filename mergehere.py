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
            df = df.reindex(columns=common_columns)

        for column in df.columns:
            if column not in common_columns:
                common_columns.append(column)

        df['Source'] = file
        dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f"CSVs have been merged and saved to '{output_file}' 🤗")

# Get the location where the script is
script_dir = os.getcwd()

# Output file name
output_file = "merged.csv"

# Merge all CSVs in the current location
merge_csvs(script_dir, output_file)

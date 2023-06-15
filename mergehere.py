import os
import pandas as pd
from pathlib import Path
from tqdm import tqdm

def merge_csvs(folder_path, output_file):
    try:
        # Find CSV files using glob
        csv_files = list(Path(folder_path).glob('*.csv'))
        
        if not csv_files:
            print("No CSVs in this folder 🤨")
            return
        
        dfs = []
        common_columns = set()
        
        # Use tqdm to show progress
        for csv_file in tqdm(csv_files, desc="Merging CSVs", unit="file"):
            df = pd.read_csv(csv_file)
            common_columns.update(df.columns)
            df = df.reindex(columns=common_columns)
            df['Source'] = csv_file.name
            dfs.append(df)
        
        merged_df = pd.concat(dfs, ignore_index=True)
        merged_df.to_csv(output_file, index=False)
        print(f"CSVs have been merged and saved to '{output_file}' 🤗")
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")

# Get the location where the script is
script_dir = os.getcwd()

# Output file name
output_file = "merged.csv"

# Merge all CSVs in the current location
merge_csvs(script_dir, output_file)

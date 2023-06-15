import os
import pandas as pd

def merge_csvs(folder_path, output_file):
    # Use pathlib module for working with file paths
    from pathlib import Path
    
    # Use glob to find CSV files
    csv_files = Path(folder_path).glob('*.csv')
    csv_files = list(csv_files)  # Convert generator to a list
    
    if not csv_files:
        print("No CSVs in this folder 🤨")
        return
    
    dfs = []
    common_columns = set()  # Use set for faster lookup
    
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        
        # Update common_columns using set operations
        common_columns.update(df.columns)
        
        # Reindex the DataFrame with common columns
        df = df.reindex(columns=common_columns)
        
        # Add 'Source' column with file name
        df['Source'] = csv_file.name
        
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

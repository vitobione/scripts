import csv
import os
import sys


def split_csv(input_file, rows_per_file, output_base_name):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the headers

        total_rows = sum(1 for row in reader) + 1  # Count number of rows (including header)
        file.seek(0)  # Reset pointer back to the beginning

        num_files = (total_rows - 1) // rows_per_file + 1  # Calculate number of output files

        for file_num in range(num_files):
            output_file = f"{output_base_name}_{file_num}.csv"

            with open(output_file, 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerow(header)  # Write header row to each file

                rows_written = 0
                for row in reader:
                    if rows_written >= rows_per_file:
                        break

                    writer.writerow(row)
                    rows_written += 1

        print(f"CSV '{input_file}' has been split into {num_files} files 🤗")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file> <rows_per_file> <output_base_name>")
    else:
        input_file = sys.argv[1]
        rows_per_file = int(sys.argv[2])
        output_base_name = sys.argv[3]
        split_csv(input_file, rows_per_file, output_base_name)

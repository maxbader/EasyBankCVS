import csv
import sys

def convert_csv(input_file, output_file):
    # Define the header row
    header = ["my_iban", "description", "booking date", "valuta date", "amount", "currency"]

    with open(input_file, mode='r', encoding='ISO-8859-1', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        # Write the header to the output file
        writer.writerow(header)

        # Write each row from the input file to the output file
        for row in reader:
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_csv.py input.csv output.csv")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    convert_csv(input_csv, output_csv)
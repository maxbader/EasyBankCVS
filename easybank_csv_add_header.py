import csv
import sys

def main(input_file, output_file):
    # Define header for the output file
    header = ["Konto", "Text", "Buchungsdatum", "Valutadatum", "Betrag", "Währung"]

    with open(input_file, mode='r', encoding='iso-8859-1', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        # Write header to output
        writer.writerow(header)

        # Copy the rest of the data
        for row in reader:
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_csv.py <input_file> <output_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    main(input_filename, output_filename)

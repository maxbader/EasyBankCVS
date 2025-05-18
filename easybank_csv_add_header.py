import csv
import sys

def main(input_file='input.csv', output_file='header.csv'):
    header = ['my_iban', 'description', 'date', 'valuta', 'amount', 'currency']
    
    with open(input_file, mode='r', encoding='ISO-8859-1', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile)

        # Write header
        writer.writerow(header)

        # Write all rows from input
        for row in reader:
            writer.writerow(row)

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'header.csv'
    main(input_file, output_file)

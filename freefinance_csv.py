import csv
import sys

# Mapping of input column names to output column names
COLUMN_MAP = {
    'my_iban': 'my_iban',
    'description': 'Beschreibung',
    'date': 'Buchungsdatum',
    'valuta': 'Valutadatum',
    'amount': 'Betrag',
    'currency': 'Währung',
    'iban': 'Auftraggeber Kontonr./IBAN',
    'company': 'Auftraggeber',
    'prefix': 'prefix',
    'bcode': 'Verwendungszweck1'
}

def main(input_file='filtered.csv', output_file='freefinance.csv'):
    with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        output_fields = [COLUMN_MAP[key] for key in COLUMN_MAP]
        writer = csv.DictWriter(outfile, fieldnames=output_fields)
        writer.writeheader()

        for row in reader:
            filtered_row = {
                COLUMN_MAP[key]: row.get(key, '') for key in COLUMN_MAP
            }
            writer.writerow(filtered_row)

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'filtered.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'freefinance.csv'
    main(input_file, output_file)

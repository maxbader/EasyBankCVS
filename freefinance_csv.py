import csv
import sys

# === Column mapping ===
COLUMN_MAPPING = {
    'my_iban': 'my_iban',
    'description': 'Beschreibung',
    'date': 'Buchungsdatum',
    'valuta': 'Valutadatum',
    'amount': 'Betrag',
    'currency': 'Währung',
    'bic': 'Auftraggeber BLZ/BIC',
    'iban': 'Auftraggeber Kontonr./IBAN',
    'company': 'Auftraggeber',
    'prefix': 'prefix',
    'bcode': 'Verwendungszweck1',
}

def filter_and_rename_csv(input_file='filtered.csv', output_file='freefinance.csv'):
    with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        
        # Filter columns that exist in the file
        input_columns = reader.fieldnames
        selected_keys = [key for key in COLUMN_MAPPING.keys() if key in input_columns]
        output_headers = [COLUMN_MAPPING[key] for key in selected_keys]

        writer = csv.DictWriter(outfile, fieldnames=output_headers)
        writer.writeheader()

        for row in reader:
            filtered_row = {COLUMN_MAPPING[key]: row[key] for key in selected_keys}
            writer.writerow(filtered_row)

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'filtered.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'freefinance.csv'
    filter_and_rename_csv(input_file, output_file)

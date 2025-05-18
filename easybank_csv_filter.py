import csv
import re
import sys

# Regular expressions
IBAN_REGEX = r'[A-Z]{2}\d{18}[A-Z]?'  # Matches LU/DE/AT IBANs with optional trailing letter
BCODE_REGEX = r'([A-Z]{2}/\d{9})'     # Captures bcode pattern

def extract_info(description):
    # 1. Extract last IBAN
    ibans = re.findall(IBAN_REGEX, description)
    iban = ibans[-1] if ibans else ''

    # 2. Extract company after IBAN
    company = ''
    if iban:
        parts = description.split(iban)
        if len(parts) > 1:
            after_iban = parts[-1].strip()
            # Company ends at pipe or end of string
            company = after_iban.split('|')[0].strip()

    # 3. Extract bcode and prefix
    bcode_match = re.search(BCODE_REGEX, description)
    bcode = bcode_match.group(1) if bcode_match else ''
    prefix = ''
    if bcode:
        prefix = description.split(bcode)[0].strip()

    return iban, company, prefix, bcode

def process_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile, delimiter=';')
        fieldnames = reader.fieldnames + ['IBAN', 'Company', 'Prefix', 'BCode']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        for row in reader:
            beschreibung = row.get('Beschreibung', '')
            iban, company, prefix, bcode = extract_info(beschreibung)
            row.update({'IBAN': iban, 'Company': company, 'Prefix': prefix, 'BCode': bcode})
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_csv.py input.csv output.csv")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    process_csv(input_csv, output_csv)

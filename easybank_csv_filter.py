import csv
import re
import sys

# === Global regular expressions ===
RE_IBAN = r'\b[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}\b'
RE_BIC = r'\|([A-Z0-9]{8}(?:[A-Z0-9]{3})?)'
RE_BCODE = r'([A-Z]{2})/(\d{9})'

def extract_info(description):
    iban_matches = re.findall(RE_IBAN, description)
    iban = iban_matches[-1] if iban_matches else ''

    bic_match = re.search(RE_BIC, description)
    bic = bic_match.group(1) if bic_match else ''

    company = ''
    if iban:
        after_iban = description.split(iban, 1)[-1]
        match = re.search(r'[| ]([^|]+)', after_iban)
        if match:
            company = match.group(1).strip()

    bcode_match = re.search(RE_BCODE, description)
    prefix = bcode = ''
    if bcode_match:
        prefix = description.split(bcode_match.group(0))[0].strip()
        bcode = bcode_match.group(0)

    return iban, bic, company, prefix, bcode

def process_csv(input_file='header.csv', output_file='filtered.csv'):
    with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['iban', 'bic', 'company', 'prefix', 'bcode']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            description = row.get('description', '')
            iban, bic, company, prefix, bcode = extract_info(description)
            row.update({'iban': iban, 'bic': bic, 'company': company, 'prefix': prefix, 'bcode': bcode})
            writer.writerow(row)

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'header.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'filtered.csv'
    process_csv(input_file, output_file)

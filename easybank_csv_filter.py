import csv
import re
import sys

# Regex patterns
IBAN_PATTERN = r'\b(?:LU\d{18}|DE\d{20}|AT\d{18})\b'
BCODE_PATTERN = r'([A-Z]{2})/(\d{9})'

def extract_iban_and_company(description):
    ibans = re.findall(IBAN_PATTERN, description)
    iban = ibans[-1] if ibans else ''

    company = ''
    if iban:
        post_iban = description.split(iban, 1)[-1]
        match = re.match(r'[ |]?([^|]+)', post_iban.strip())
        if match:
            company = match.group(1).strip()

    return iban, company

def extract_prefix_and_bcode(description):
    match = re.search(BCODE_PATTERN, description)
    if match:
        prefix = description[:match.start()].strip()
        bcode = f"{match.group(1)}/{match.group(2)}"
        return prefix, bcode
    return '', ''

def main(input_file='header.csv', output_file='filtered.csv'):
    with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['iban', 'company', 'prefix', 'bcode']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for row in reader:
            description = row.get('description', '')
            iban, company = extract_iban_and_company(description)
            prefix, bcode = extract_prefix_and_bcode(description)

            row.update({
                'iban': iban,
                'company': company,
                'prefix': prefix,
                'bcode': bcode
            })
            writer.writerow(row)

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'header.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'filtered.csv'
    main(input_file, output_file)

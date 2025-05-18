import csv
import re
import sys

# Example IBANs to match against
iban_pattern = r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"
bcode_pattern = r"([A-Z]{2}/\d{9})"

def extract_info(text):
    # Extract IBANs and pick the last one
    ibans = re.findall(iban_pattern, text)
    iban = ibans[-1] if ibans else ""

    # Extract company name after IBAN
    company = ""
    if iban:
        post_iban = text.split(iban, 1)[-1]
        match = re.search(r"[ \|](.*?)(?:\||$)", post_iban.strip())
        if match:
            company = match.group(1).strip()

    # Extract bcode and prefix
    bcode_match = re.search(bcode_pattern, text)
    bcode = bcode_match.group(1) if bcode_match else ""
    prefix = text.split(bcode, 1)[0].strip() if bcode else ""

    return iban, company, prefix, bcode

def main(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
         open(output_file, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.DictReader(infile, delimiter=';')
        fieldnames = reader.fieldnames + ['IBAN', 'Company', 'Prefix', 'BCode']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()

        for row in reader:
            text = row.get("Text", "")
            iban, company, prefix, bcode = extract_info(text)
            row.update({"IBAN": iban, "Company": company, "Prefix": prefix, "BCode": bcode})
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_info.py <input_file> <output_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    main(input_filename, output_filename)

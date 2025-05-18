# EasyBankCSV
This Python script converts a CSV file exported from the EasyBank App (Austria / Österreich) 
into a more readable and standardized format. It is also likely compatible with CSV exports 
from BAWAG Bank, given the similar formatting conventions.

The processing steps include:

1. **Adding headers**:  
   - The raw CSV typically lacks column headers. The script inserts appropriate headers for clarity and further processing.

2. **Parsing and extracting key information**:  
   - Extracts details such as IBAN, company name, bank code (BIC), and transaction references from the unstructured text fields.

3. **Formatting the output**:  
   - Transforms the data into a structure compatible with popular Austrian accounting and financial tools, including:
     - FreeFinance
     - ProSaldo
     - (potentially other tools that accept standardized bank transaction CSVs)

The result is a clean, structured CSV ready for import into accounting software or for manual review.

## Usage
1. Open your easybank account
1. Make a 'Umsatzsuche' over the time/date to extract
1. Download a CSV file from https://ebanking.easybank.at/ 
1. Run the Python script with the following arguments; the first should be your extracted CSV
```
./easybank_csv_add_header.py input.csv header.csv
./easybank_csv_filter.py header.csv filtered.csv
```
### FreeFinance
1. Run the Python script create the final csv
```
./freefinance.py filtered.csv freefinance.csv
```
1. Open your 'Bankverbindung' account
1. select 'CSV import'
1. Bank/Vorlage wählen: "Standard - Kontoauszug"
1. Upload your `freefinance.csv`
1. Establish a correct and useful relation.

### ProSaldo. 
Run the Python script with the following arguments; the first should be your extracted CSV
1. Run the Python script create the final csv
```
./prosaldo.py filtered.csv prosaldo.csv
```
1. Open your 'ProSaldo' account
1. select 'Bank & Buchen'
1. select 'CSV-/TXT-Import'
1. Upload your `prosaldo.csv`
1. Establish a correct and useful relation.

## Code 
### easybank_csv_add_header 
The code was generated using the LLM ChatGPT with the following prompt:
```
Can you help me to create a simple python script. It should process a CSV file with  semicolons as a delimiter and output a new CSV file. The input file is ISO-8859-1 encoded, while the output should be UTF-8. The input file name and the output filename are arguments to the script. The input CSV has no header row.
The output file must have a header row. With the following titles my_iban, description, date, valuta, amount and currency
The default arguemtns should be input.csv and header.csv
```
### easybank_csv_filter 
The code was generated using the LLM ChatGPT with the following prompt:
```
I would like to read a csv file with a header row encoded in  utf-8 and generate a new file.
The input file name and the output filename are arguments to the script.
The script should extract then some information from the column description.

1. IBAN and company
   The IBAN is found in the string of the column called description. 
   If there is more than one IBAN in the string, the last appearance should be used.
   The company name can be found after the IBAN if there is a space or pipe character, and it ends with the entry or another pipe character. 
   The IBAN and company can be emtpy

There are some bank IBANs as an example.
LU89751000135102200E
DE79590500000020025855
AT113293900005511726

2. prefix and bcode
   The bcode is found in the string of the column called description.
   The bcode is composed of to upper case letters followed by a / and nine digits. 
   The prefix and bcode can be emtpy


The output file should be the input, but each row has the new column values attached. 
The default arguemtns should be header.csv and filtered.csv

```
### freefinance_csv
The code was generated using the LLM ChatGPT with the following prompt:
```
I would like to create a Python script that reads a CSV file encoded in UTF-8 with a header row and generates a new output file.
The input and output filenames should be passed as arguments to the script.

The output file should contain only specific columns, and some of them should be renamed as follows:
    my_iban → "my_iban"
    description → "Beschreibung"
    date → "Buchungsdatum"
    valuta → "Valutadatum"
    amount → "Betrag"
    currency → "Währung"
    iban → "Auftraggeber Kontonr./IBAN"
    company → "Auftraggeber"
    prefix → "prefix"
    bcode → "Verwendungszweck1"

All other columns should be ignored in the output.
The default arguemtns should be filtered.csv and freefinance.csv

```


# Setup
The python enviroment can be crated by crating an enviroment with
```
python3 -m venv ./eb-env
```
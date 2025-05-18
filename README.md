# EasyBankCSV
This Python script converts a CSV extracted form Austrian / Österreich the Easy Bank App to a ProSado or FreeFinance readable CSV. 
It will most likey also work with the BAWAG Bank

## Usage
1. Open your easybank account
1. Make a 'Umsatzsuche' over the time/date to extract
1. Download a CSV file from https://ebanking.easybank.at/ 
1. Run the Python script with the following arguments; the first should be your extracted CSV
```
./easybank_csv_add_header.py input.csv header.csv
./easybank_csv_filter.py header.csv output.csv
```
### ProSaldo
1. Open your 'ProSaldo' account
1. select 'Bank & Buchen'
1. select 'CSV-/TXT-Import'
1. Upload your `output.csv`
1. Establish a correct and useful relation.

### FreeFinance
1. Open your 'Bankverbindung' account
1. select 'CSV import'
1. Bank/Vorlage wählen: "Standard - Kontoauszug"
1. Upload your `output.csv`
1. Establish a correct and useful relation.

## Code 
### easybank_csv_add_header 
The code was generated using the LLM ChatGPT with the following prompt:
```
Can you help me to create a simple python script. It should process a CSV file with  semicolons as a delimiter and output a new CSV file. The input file is ISO-8859-1 encoded, while the output should be UTF-8. The input file name and the output filename are arguments to the script. The input CSV has no header row.
The output file must have a header row. With the following titles Konto, Beschreibung, Buchungsdatum, Valutadatum, Betrag and Währung
```
### easybank_filter 
The code was generated using the LLM ChatGPT with the following prompt:
```
I would like to read a csv file with a header row encoded in  utf-8 and generate a new file.The input file name and the output filename are arguments to the script.
The script should extract then some information from the column Beschreibung.

1. IBAN and company
   If there is more than one IBAN in the string, the last appearance should be used.
   The company name can be found after the IBAN if there is a space or pipe character, and it ends with the entry or another pipe character.

There are some bank IBANs as an example.
LU89751000135102200E
DE79590500000020025855
AT113293900005511726

2. prefix and bcode
   The bcode is composed of to upper case letters followed by a / and nine digits . The prefix is empty or the string in the Text column before the bcode.

The output file should be the input, but each row has the new column values attached.

```

# Setup
The python enviroment can be crated by crating an enviroment with
```
python3 -m venv ./eb-env
```
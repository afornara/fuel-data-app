import csv
import requests
import json

# Funzione per ottenere i dati dal CSV tramite URL
def get_csv_data(url):
    response = requests.get(url)
    data = response.text.splitlines()[1:]  # Ignora la prima riga
    return list(csv.DictReader(data, delimiter=';'))  # Converti in lista

# Carica entrambi i file
file2_data_list = get_csv_data('https://www.mise.gov.it/images/exportCSV/prezzo_alle_8.csv')  # Ora è una lista
file1_data = get_csv_data('https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv')

# Effettua la fusione
merged_data = []

# Per ogni riga in file1, cerca tutte le righe corrispondenti in file2
for row1 in file1_data:
    merged_row = row1.copy()  # Inizia con i dati da file1
    merged_row['prezzi'] = []  # Crea una lista vuota per i dati corrispondenti da file2

    for row2 in file2_data_list:  # Ora usi la lista
        if row1["idImpianto"] == row2["idImpianto"]:
            merged_row['prezzi'].append(row2)  # Aggiunge i dati da file2 alla lista

    merged_data.append(merged_row)

# Salva i dati fusi come JSON
with open('merged_data.json', 'w') as outfile:
    json.dump(merged_data, outfile)

print("Merge completato e dati salvati come merged_data.json.")

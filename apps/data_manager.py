import json
import csv
from . import database

def export_to_json(filename='inventaris.json'):
    data_rows = database.get_semua_kendaraan_db()

    data_dicts = [dict(row) for row in data_rows]

    with open(filename, 'w') as f:
        json.dump(data_dicts, f, indent=4)
        print(f"Data berhasil di ekspor ke {filename}")

def export_to_csv(filename='inventaris.csv'):
    data_rows = database.get_semua_kendaraan_db()
    if not data_rows:
        print("Titdak ada untuk diekspor")
        return
    
    headers = data_rows[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data_rows:
            writer.writerow(dict(row))
            printf(f"Data berhasil diekspor ke{filename}")

def import_from_csv(filename='inventaris.csv'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                database.tambah_kendaraan_db(
                    row['merk'],
                    row['model'],
                    int(row['tahun']),
                    float(row['harga'])
                )
                count +=1
                print(f"Berhasil mengimpor {count} kendaraan dari {filename}")
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan")
    except Exception as e:
        print(f"Terjadi error saat impor : {e}")
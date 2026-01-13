import csv
from model import Mahasiswa

def load_mahasiswa(file_csv):
    mahasiswa = []
    with open(file_csv, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mahasiswa.append(
                Mahasiswa(row["nim"], row["nama"])
            )
    return mahasiswa

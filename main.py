"Program Manajemen Ruang Lab"

from model import Ruangan, Praktikum
from loader import load_mahasiswa
from penjadwal import Penjadwal

praktikum = Praktikum(
    nama="Biologi Molekuler",
    hari="Senin",
    mulai="08:00",
    selesai="10:00"
)

daftar_ruangan = [
    Ruangan("Lab A", 9),
    Ruangan("Lab B", 8),
    Ruangan("Lab C", 8),
]

mahasiswa = load_mahasiswa("data dummy/mahasiswa.csv")

#jadwalnyo
penjadwal = Penjadwal()
penjadwal.bagi_mahasiswa(praktikum, mahasiswa, daftar_ruangan )
penjadwal.tampilkan()

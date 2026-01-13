def jam_ke_menit(jam):
    h, m = map(int, jam.split(":"))
    return h * 60 + m


def menit_ke_jam(menit):
    h = menit // 60
    m = menit % 60
    return f"{h:02d}:{m:02d}"

class Penjadwal:
    def __init__(self):
        self.hasil = []

    def bagi_mahasiswa(self, praktikum, mahasiswa, ruangan):
        index = 0
        sesi = 1

        mulai_menit = jam_ke_menit(praktikum.mulai)
        durasi = 120 #menit
        jeda = 30

        while index < len(mahasiswa):
            selesai_menit = mulai_menit + durasi

            for r in ruangan:
                if index >= len(mahasiswa):
                    break

                daftar = []

                for _ in range(r.kapasitas):
                    if index >= len(mahasiswa):
                        break

                    mhs = mahasiswa[index]
                    daftar.append(f"{mhs.nama} ({mhs.nim})")
                    index += 1

                if daftar:
                    self.hasil.append({
                        "praktikum": praktikum.nama,
                        "ruangan": r.nama,
                        "hari": praktikum.hari,
                        "sesi": sesi,
                        "waktu": f"{menit_ke_jam(mulai_menit)} - {menit_ke_jam(selesai_menit)}",
                        "mahasiswa": daftar
                    })

            mulai_menit = selesai_menit + jeda
            sesi += 1

    def tampilkan(self):
        print("\nJADWAL PRAKTIKUM LAB\n")
        for h in self.hasil:
            print(f"Praktikum : {h['praktikum']}")
            print(f"Ruangan   : {h['ruangan']}")
            print(f"Hari      : {h['hari']}")
            print(f"Sesi ke   : {h['sesi']}")
            print(f"Waktu     : {h['waktu']}")
            print("Mahasiswa :")
            for m in h["mahasiswa"]:
                print(f" - {m}")
            print("\n")
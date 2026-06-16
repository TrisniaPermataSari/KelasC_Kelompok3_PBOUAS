from models import Buku, Majalah, Jurnal, DVDFilmDokumenter


class Perpustakaan:
    def __init__(self):
        self._koleksi = []

    def tambah_koleksi(self, koleksi):
        self._koleksi.append(koleksi)

    def hapus_koleksi(self, kode):
        for item in self._koleksi:
            if item.get_kode() == kode:
                self._koleksi.remove(item)
                return True
        return False

    def tampil_semua(self):
        if not self._koleksi:
            print("  Belum ada data koleksi.")
            return
        print("\nDATA KOLEKSI")
        print("-" * 40)
        for i, item in enumerate(self._koleksi, 1):
            print(f"\nKoleksi {i}:")
            item.tampil_info()
    
    def tambah_buku(self):
        print("\n" + "=" * 30)
        print("TAMBAH DATA BUKU")
        print("-" * 30)
        kode      = input("Masukkan Kode Koleksi  : ")
        judul     = input("Masukkan Judul         : ")
        tahun     = input("Masukkan Tahun Terbit  : ")
        pengarang = input("Masukkan Pengarang     : ")
        penerbit  = input("Masukkan Penerbit      : ")
        self.tambah_koleksi(Buku(kode, judul, tahun, pengarang, penerbit))
        print("-" * 30)
        print("Tambah Buku Sukses")

    def tambah_majalah(self):
        print("\n" + "=" * 30)
        print("TAMBAH DATA MAJALAH")
        print("-" * 30)
        kode     = input("Masukkan Kode Koleksi  : ")
        judul    = input("Masukkan Judul         : ")
        tahun    = input("Masukkan Tahun Terbit  : ")
        penerbit = input("Masukkan Penerbit      : ")
        edisi    = input("Masukkan Edisi         : ")
        self.tambah_koleksi(Majalah(kode, judul, tahun, penerbit, edisi))
        print("-" * 30)
        print("Tambah Majalah Sukses")

    def tambah_jurnal(self):
        print("\n" + "=" * 30)
        print("TAMBAH DATA JURNAL")
        print("-" * 30)
        kode     = input("Masukkan Kode Koleksi  : ")
        judul    = input("Masukkan Judul         : ")
        tahun    = input("Masukkan Tahun Terbit  : ")
        penerbit = input("Masukkan Penerbit      : ")
        bidang   = input("Masukkan Bidang Studi  : ")
        impact   = input("Masukkan Impact Factor : ")
        self.tambah_koleksi(Jurnal(kode, judul, tahun, penerbit, bidang, impact))
        print("-" * 30)
        print("Tambah Jurnal Sukses")

    def tambah_dvd(self):
        print("\n" + "=" * 30)
        print("TAMBAH DATA DVD FILM DOKUMENTER")
        print("-" * 30)
        kode       = input("Masukkan Kode Koleksi  : ")
        judul      = input("Masukkan Judul         : ")
        tahun      = input("Masukkan Tahun Terbit  : ")
        penerbit   = input("Masukkan Penerbit      : ")
        jenis_film = input("Masukkan Jenis Film    : ")
        bidang     = input("Masukkan Bidang Ilmu   : ")
        durasi     = input("Masukkan Durasi (menit): ")
        self.tambah_koleksi(DVDFilmDokumenter(kode, judul, tahun, penerbit, jenis_film, bidang, durasi))
        print("-" * 30)
        print("Tambah DVD Film Dokumenter Sukses")
from models import Buku, Majalah, Jurnal, DVDFilmDokumenter


class InputHandler:
    def input_buku(self):
        print("\n" + "=" * 30)
        print("TAMBAH DATA BUKU")
        print("-" * 30)
        kode      = input("Masukkan Kode Koleksi  : ")
        judul     = input("Masukkan Judul         : ")
        tahun     = input("Masukkan Tahun Terbit  : ")
        pengarang = input("Masukkan Pengarang     : ")
        penerbit  = input("Masukkan Penerbit      : ")
        return Buku(kode, judul, tahun, pengarang, penerbit)

    def input_majalah(self):
        print("\n" + "=" * 30)
        print("TAMBAH DATA MAJALAH")
        print("-" * 30)
        kode     = input("Masukkan Kode Koleksi  : ")
        judul    = input("Masukkan Judul         : ")
        tahun    = input("Masukkan Tahun Terbit  : ")
        penerbit = input("Masukkan Penerbit      : ")
        edisi    = input("Masukkan Edisi         : ")
        return Majalah(kode, judul, tahun, penerbit, edisi)

    def input_jurnal(self):
        print("\n" + "=" * 30)
        print("TAMBAH DATA JURNAL")
        print("-" * 30)
        kode     = input("Masukkan Kode Koleksi  : ")
        judul    = input("Masukkan Judul         : ")
        tahun    = input("Masukkan Tahun Terbit  : ")
        penerbit = input("Masukkan Penerbit      : ")
        bidang   = input("Masukkan Bidang Studi  : ")
        impact   = input("Masukkan Impact Factor : ")
        return Jurnal(kode, judul, tahun, penerbit, bidang, impact)

    def input_dvd(self):
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
        return DVDFilmDokumenter(kode, judul, tahun, penerbit, jenis_film, bidang, durasi)

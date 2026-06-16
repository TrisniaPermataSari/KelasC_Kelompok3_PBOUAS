from abc import ABC, abstractmethod


class KoleksiPerpustakaan(ABC):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit):
        self._kode_koleksi = kode_koleksi
        self._judul = judul
        self._tahun_terbit = tahun_terbit
        self._penerbit = penerbit

    def get_kode(self):
        return self._kode_koleksi

    @abstractmethod
    def get_jenis(self):
        pass

    @abstractmethod
    def tampil_info(self):
        pass


class Buku(KoleksiPerpustakaan):
    def __init__(self, kode_koleksi, judul, tahun_terbit, pengarang, penerbit):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self._pengarang = pengarang

    def get_jenis(self):
        return "Buku"

    def tampil_info(self):
        print(f"  Jenis         : {self.get_jenis()}")
        print(f"  Kode Koleksi  : {self._kode_koleksi}")
        print(f"  Judul         : {self._judul}")
        print(f"  Thn Terbit    : {self._tahun_terbit}")
        print(f"  Pengarang     : {self._pengarang}")
        print(f"  Penerbit      : {self._penerbit}")


class Majalah(KoleksiPerpustakaan):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, edisi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self._edisi = edisi

    def get_jenis(self):
        return "Majalah"

    def tampil_info(self):
        print(f"  Jenis         : {self.get_jenis()}")
        print(f"  Kode Koleksi  : {self._kode_koleksi}")
        print(f"  Judul         : {self._judul}")
        print(f"  Thn Terbit    : {self._tahun_terbit}")
        print(f"  Penerbit      : {self._penerbit}")
        print(f"  Edisi         : {self._edisi}")

        
class Jurnal(KoleksiPerpustakaan):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_studi, impact_factor):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self._bidang_studi = bidang_studi
        self._impact_factor = impact_factor

    def get_jenis(self):
        return "Jurnal"

    def tampil_info(self):
        print(f"  Jenis         : {self.get_jenis()}")
        print(f"  Kode Koleksi  : {self._kode_koleksi}")
        print(f"  Judul         : {self._judul}")
        print(f"  Thn Terbit    : {self._tahun_terbit}")
        print(f"  Penerbit      : {self._penerbit}")
        print(f"  Bidang Studi  : {self._bidang_studi}")
        print(f"  Impact Factor : {self._impact_factor}")

class DVDFilmDokumenter(KoleksiPerpustakaan):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, jenis_film, bidang_ilmu, durasi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self._jenis_film = jenis_film
        self._bidang_ilmu = bidang_ilmu
        self._durasi = durasi

    def get_jenis(self):
        return "DVD Film Dokumenter"

    def tampil_info(self):
        print(f"  Jenis         : {self.get_jenis()}")
        print(f"  Kode Koleksi  : {self._kode_koleksi}")
        print(f"  Judul         : {self._judul}")
        print(f"  Thn Terbit    : {self._tahun_terbit}")
        print(f"  Penerbit      : {self._penerbit}")
        print(f"  Jenis Film    : {self._jenis_film}")
        print(f"  Bidang Ilmu   : {self._bidang_ilmu}")
        print(f"  Durasi        : {self._durasi} menit")
from models import KoleksiPerpustakaan


class Perpustakaan:
    def __init__(self):
        self._koleksi = []

    def tambah_koleksi(self, koleksi: KoleksiPerpustakaan):
        self._koleksi.append(koleksi)

    def hapus_koleksi(self, kode):
        for item in self._koleksi:
            if item.get_kode() == kode:
                self._koleksi.remove(item)
                return True
        return False

    def get_semua_koleksi(self):
        return self._koleksi

    def tampil_semua(self):
        if not self._koleksi:
            print("  Belum ada data koleksi.")
            return
        print("\nDATA KOLEKSI")
        print("-" * 40)
        for i, item in enumerate(self._koleksi, 1):
            print(f"\nKoleksi {i}:")
            item.tampil_info()

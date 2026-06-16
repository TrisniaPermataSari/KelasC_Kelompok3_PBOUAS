from perpustakaan import Perpustakaan
from input_handler import InputHandler


def main():
    perpus = Perpustakaan()
    handler = InputHandler()

    while True:
        print("\n" + "=" * 20)
        print("MENU PROGRAM")
        print("-" * 20)
        print("1. Tambah data koleksi")
        print("2. Hapus data koleksi")
        print("3. Tampil semua data koleksi")
        print("4. Keluar")
        pilih = input("\nNomor yang dipilih: ")

        if pilih == "1":
            print("\n" + "-" * 30)
            print("JENIS KOLEKSI YANG AKAN DITAMBAH")
            print("\n1. Buku\n2. Majalah\n3. Jurnal\n4. DVD Film Dokumenter")
            jenis = input("\nNomor yang dipilih: ")

            koleksi = None
            if jenis == "1":
                koleksi = handler.input_buku()
            elif jenis == "2":
                koleksi = handler.input_majalah()
            elif jenis == "3":
                koleksi = handler.input_jurnal()
            elif jenis == "4":
                koleksi = handler.input_dvd()
            else:
                print("Pilihan tidak valid.")

            if koleksi:
                perpus.tambah_koleksi(koleksi)
                print("-" * 30)
                print("Tambah koleksi sukses.")
            input("\nTekan [ENTER] untuk kembali ke menu program")

        elif pilih == "2":
            print("\n" + "-" * 30)
            print("HAPUS DATA KOLEKSI")
            kode = input("\nMasukkan Kode Koleksi  : ")
            if perpus.hapus_koleksi(kode):
                print("-" * 30)
                print("Hapus data koleksi sukses.")
            else:
                print("Kode koleksi tidak ditemukan.")
            input("\nTekan [ENTER] untuk kembali ke menu program")

        elif pilih == "3":
            perpus.tampil_semua()
            input("\nTekan [ENTER] untuk kembali ke menu program")

        elif pilih == "4":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()

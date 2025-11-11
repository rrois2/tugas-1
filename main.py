from apps.classes import Dealer  # <-- IMPORT CLASS DARI FILE LAIN
from apps.data_manager import export_to_csv, export_to_json, import_from_csv

def main():
    dealer_jaya_abadi = Dealer("Jaya Abadi Motor")

    # Loop utama aplikasi
    while True:
        print("\n===== Aplikasi Penjualan Kendaraan =====")
        print("1. Tampilkan Semua Kendaraan Tersedia")
        print("2. Beli Kendaraan")
        print("3. Tambah Kendaraan Baru")
        print("---")
        print("4. Ekspor Data ke JSON")
        print("5. Ekspor Data ke CSV")
        print("6. Impor Data dari CSV")
        print("7. Keluar")
        
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            dealer_jaya_abadi.tampilkan_kendaraan_tersedia()
        elif pilihan == '2':
            dealer_jaya_abadi.tampilkan_kendaraan_tersedia()
            dealer_jaya_abadi.proses_penjualan()
        elif pilihan == '3':
           dealer_jaya_abadi.tambah_kendaraan_interaktif()

        elif pilihan == '4':
            export_to_json('inventaris.json')

        elif pilihan == '5':
            export_to_csv('inventaris.csv')

        elif pilihan == '6':
            print("Pastikan file CSV memiliki kolom: merk, model, tahun, harga")
            filepath = input("Masukkan nama file CSV (default: inventaris.csv): ")
            if not filepath:
                filepath = 'inventaris.csv'
            import_from_csv(filepath)

        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan fungsi utama saat script dieksekusi
if __name__ == "__main__":
    main()
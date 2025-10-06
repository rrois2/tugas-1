from apps.classes import Kendaraan, Dealer  # <-- IMPORT CLASS DARI FILE LAIN

def main():
    dealer_jaya_abadi = Dealer("Jaya Abadi Motor")
    dealer_jaya_abadi.tambah_kendaraan(Kendaraan("Toyota", "Avanza", 2023, 250000000))
    dealer_jaya_abadi.tambah_kendaraan(Kendaraan("Honda", "Brio Satya", 2022, 180000000))
    dealer_jaya_abadi.tambah_kendaraan(Kendaraan("Mitsubishi", "Xpander", 2024, 320000000))
    dealer_jaya_abadi.tambah_kendaraan(Kendaraan("Suzuki", "Ertiga", 2021, 210000000))

    # Loop utama aplikasi
    while True:
        print("\n===== Aplikasi Penjualan Kendaraan =====")
        print("1. Tampilkan Semua Kendaraan Tersedia")
        print("2. Beli Kendaraan")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            dealer_jaya_abadi.tampilkan_kendaraan_tersedia()
        elif pilihan == '2':
            dealer_jaya_abadi.tampilkan_kendaraan_tersedia()
            dealer_jaya_abadi.proses_penjualan()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan fungsi utama saat script dieksekusi
if __name__ == "__main__":
    main()
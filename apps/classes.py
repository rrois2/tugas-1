class Kendaraan:
    def __init__(self, merk, model, tahun, harga):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.harga = harga
        self.status = "Tersedia"

    def tampilkan_info(self):
        return f"{self.tahun} {self.merk} {self.model} - Rp{self.harga:,.0f} ({self.status})"

    def jual(self):
        self.status = "Terjual"
        print(f"✅ Transaksi Berhasil! {self.merk} {self.model} telah terjual.")


class Dealer:
    def __init__(self, nama):
        self.nama = nama
        self.inventaris = []

    def tambah_kendaraan(self, kendaraan):
        """Menambahkan objek kendaraan ke dalam daftar inventaris."""
        self.inventaris.append(kendaraan)

    def tampilkan_kendaraan_tersedia(self):
        print(f"\n--- Daftar Kendaraan di {self.nama} ---")
        ada_stok = False
        
        for i, mobil in enumerate(self.inventaris):
            if mobil.status == "Tersedia":
                print(f"{i + 1}. {mobil.tampilkan_info()}")
                ada_stok = True

        if not ada_stok:
            print("Saat ini tidak ada kendaraan yang tersedia.")
        print("----------------------------------------")

    def proses_penjualan(self):
        nomor_str = input("Masukkan nomor kendaraan yang ingin dibeli: ")
        
        try:
            nomor_pilihan = int(nomor_str)
            indeks_mobil = nomor_pilihan - 1

            if 0 <= indeks_mobil < len(self.inventaris):
                mobil_dipilih = self.inventaris[indeks_mobil]
                
                if mobil_dipilih.status == "Tersedia":
                    print(f"Anda akan membeli: {mobil_dipilih.tampilkan_info()}")
                    konfirmasi = input("Lanjutkan transaksi? (y/n): ").lower()
                    if konfirmasi == 'y':
                        #mobil_dipilih.jual()
                        harga_mobil = mobil_dipilih.harga
                        print("---------------------------")
                        print(f"Total tagihan : Rp.{harga_mobil:,.0f}")

                        try:
                            uang_str = input("Masukkan jumlah uang pembayaran anda : Rp ")
                            uang_pembayaran = int(uang_str.replace(".","").replace(",",""))

                            if uang_pembayaran >=harga_mobil:
                                kembalian = uang_pembayaran - harga_mobil

                                print(f"\n Pembayaran berhasil")
                                print(f"Uang anda   : Rp{uang_pembayaran :,.0f}")
                                print(f"kembalian anda : Rp{kembalian :,.0f}")

                                mobil_dipilih.jual()
                                print(f"Terima kasih {mobil_dipilih.merk} {mobil_dipilih.model} telah terjual")
                            else:
                                kekurangan = harga_mobbil - uang_pembayaran
                                print(f"\n Transaksi gagal")
                                print(f"Uang anda kurang sebesar Rp{kekurangan:,.0f}")
                        
                        except ValueError:
                            print("Input pembayaran tidak valid. Harap masukkan angka")

                    else:
                        print("Transaksi dibatalkan.")
                else:
                    print("Maaf, kendaraan tersebut sudah terjual.")
            else:
                print("Nomor tidak valid. Silakan pilih nomor dari daftar.")
        except ValueError:
            print("input tidak valid. Harap masukkan angka.")
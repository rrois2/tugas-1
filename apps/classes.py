from . import database


class Kendaraan:
    def __init__(self, id, merk, model, tahun, harga, status="Tersedia"):
        self.id = id
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.harga = harga
        self.status = status

    def tampilkan_info(self):
        return f"{self.tahun} {self.merk} {self.model} - Rp{self.harga:,.0f} ({self.status})"

    # def jual(self):
    #     self.status = "Terjual"
    #     print(f"✅ Transaksi Berhasil! {self.merk} {self.model} telah terjual.")


class Dealer:
    def __init__(self, nama):
        self.nama = nama
        database.create_table()

        self.kendaraan_terdisplay = []

    def tambah_kendaraan_interaktif(self):
        print("\n--- Tambah Kendaraan Baru ---")
        try:
            merk = input("Merk Kendaraan : ")
            model = input("Model Kendaraan : ")
            tahun = int(input("Tahun : "))
            harga = float(input("Harga : "))
           
            if database.tambah_kendaraan_db(merk, model, tahun, harga):
               print(f"Berhasil {tahun} {merk} {model} ditambahkan ke database")
            else:
               print("Gagal menambahkan kendaraan")
        except ValueError:
           print("Input tahun/harga tidak valid. Harap masukan angka")
        except Exception as e:
           print(f"Terjadi error : {e}")


    def tampilkan_kendaraan_tersedia(self):
        print(f"\n--- Daftar Kendaraan di {self.nama} ---")

        data_rows = database.get_semua_kendaraan_db()

        tersedia_rows = [row for row in data_rows if row['status'] == 'Tersedia']

        if not tersedia_rows:
            print("saat ini tidak ada kendaraan yang tersedia")
            print("--------------------------------")
            self.kendaraan_terdisplay = []
            return False
        
        self.kendaraan_terdisplay = []
        for i, row in enumerate(tersedia_rows):
            mobil = Kendaraan(
                row['id'], row['merk'], row['model'],
                row['tahun'], row['harga'], row['status']
            )
            self.kendaraan_terdisplay.append(mobil)
            print(f"{i + 1}.{mobil.tampilkan_info()}")

        print("-----------------------------------")
        return True
        
        

    def proses_penjualan(self):
        if not self.tampilkan_kendaraan_tersedia():
            return
        
        try:
            nomor_str = input("Masukkan nomor kendaraan yang ingin dibeli: ")
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
def Help(role, logged_in):
    # Fungsi ini menampilkan menu help yang berisi panduan penggunaan sistem
    # Parameter input dari prosedur ini yaitu role dan status login dari pengguna 
    
    print("\n============ HELP ============")

    if logged_in == False :    # Tampilan menu help jika penggguna belum login
        print("1. LOGIN - Untuk melakukan login ke dalam sistem")
        print("2. HELP - Untuk menampilkan panduan penggunaan sistem")

    else:
        if role == "admin" :   # Tampilan menu help untuk admin
            print("1. LOGIN - Untuk melakukan login ke dalam sistem")
            print("2. REGISTER - mendaftarkan pengguna baru dengan memasukkan nama, username, dan password")
            print("3. TAMBAH GAME - Untuk menambah game pada toko game")
            print("4. UBAH GAME - Untuk mengubah informasi game pada toko game")
            print("5. UBAH STOK GAME - Untuk mengubah stok game pada toko")
            print("6. LIST GAME - Untuk melihat list game yang dijual pada toko")
            print("7. CARI GAME DI TOKO - Untuk mendapatkan informasi game pada toko, terdapat 5 parameter input namun tidak wajib diisi")
            print("8. TOP UP - Untuk menambahkan saldo kepada User")
            print("9. HELP - Untuk menampilkan panduan penggunaan sistem")
            print("10. SAVE - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
            print("11. EXIT - Untuk keluar dari aplikasi")

        elif role == "user" :                      # Tampilan menu help untuk user
            print("1. LOGIN - Untuk melakukan login ke dalam sistem")
            print("2. LIST GAME - Untuk melihat list game yang dijual pada toko")
            print("3. BELI GAME - Untuk membeli game dari toko")
            print("4. LIHAT GAME USER - Untuk menampilkan daftar game yang dimiliki pengguna")
            print("5. CARI GAME USER - Untuk mendapatkan informasi game sesuai dengan query yang diminta oleh pengguna pada inventory")
            print("6. CARI GAME DI TOKO - Untuk mendapatkan informasi game pada toko, terdapat 5 parameter input namun tidak wajib diisi")
            print("7. LIHAT RIWAYAT PEMBELIAN - Untuk mendapatkan informasi tentang riwayat pembelian game")
            print("8. HELP - Untuk menampilkan panduan penggunaan sistem")
            print("9. SAVE - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
            print("10. EXIT - Untuk keluar dari aplikasi")

        print()

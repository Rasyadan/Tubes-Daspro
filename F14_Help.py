def Help(role, logged_in):
    # Fungsi ini menampilkan menu help yang berisi panduan penggunaan sistem
    # Parameter input dari prosedur ini yaitu role dan status login dari pengguna 
    
    print("\n============ HELP ============")

    if logged_in == False :    # Tampilan menu help jika penggguna belum login
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. help - Untuk menampilkan panduan penggunaan sistem")

    else:
        if role == "admin" :   # Tampilan menu help untuk admin
            print("1. register - mendaftarkan pengguna baru dengan memasukkan nama, username, dan password")
            print("2. login - Untuk melakukan login ke dalam sistem")
            print("3. tambah_game - Untuk menambah game pada toko game")
            print("4. ubah_game - Untuk mengubah informasi game pada toko game")
            print("5. ubah_stok - Untuk mengubah stok game pada toko")
            print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
            print("7. search_game_at_store - Untuk mendapatkan informasi game pada toko, terdapat 5 parameter input namun tidak wajib diisi")
            print("8. topup - Untuk menambahkan saldo kepada User")
            print("9. help - Untuk menampilkan panduan penggunaan sistem")
            print("10. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
            print("11. exit - Untuk keluar dari aplikasi")

        elif role == "user" :                      # Tampilan menu help untuk user
            print("1. login - Untuk melakukan login ke dalam sistem")
            print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
            print("3. buy_game - Untuk membeli game dari toko")
            print("4. list_game - Untuk menampilkan daftar game yang dimiliki pengguna")
            print("5. search_my_game - Untuk mendapatkan informasi game sesuai dengan query yang diminta oleh pengguna pada inventory")
            print("6. search_game_at_store - Untuk mendapatkan informasi game pada toko, terdapat 5 parameter input namun tidak wajib diisi")
            print("7. riwayat - Untuk mendapatkan informasi tentang riwayat pembelian game")
            print("8. help - Untuk menampilkan panduan penggunaan sistem")
            print("9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
            print("10. exit - Untuk keluar dari aplikasi")

        print()

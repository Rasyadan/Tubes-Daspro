from lensplit import arrayLength

def isAdmin (data_pengguna):
    if data_pengguna[4]=="admin":
        True
    else:
        False

def tambahgame(game,data_pengguna):
    if isAdmin(data_pengguna):
        inputSelesai=False
        while not inputSelesai:
            nama= input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun_rilis= int(input("Masukkan tahun rilis: "))
            harga=int(input("Masukkan harga: "))
            stok_awal=int(input("Masukkan stok awal: "))
            if (nama!="" and kategori!="" and tahun_rilis!="" and harga!="" and stok_awal!="" ):
                tambahan=[f"GAME00{arrayLength(game)/6+2}",nama,kategori,tahun_rilis,harga,stok_awal]
                inputSelesai=True
            else:
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
                inputSelesai=False

        game = game+tambahan
        return (game)
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")


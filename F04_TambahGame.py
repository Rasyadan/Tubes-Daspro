from lensplit import arrayLength

def isAdmin (data_pengguna):
    if data_pengguna[4]=="admin":
        return(True)
    else:
        return (False)

def tambahgame(game,data_pengguna):
    if isAdmin(data_pengguna):
        inputSelesai=False
        while not inputSelesai:
            nama= input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun_rilis= input("Masukkan tahun rilis: ")
            harga=input("Masukkan harga: ")
            stok_awal=input("Masukkan stok awal: ")
            if (nama!="" and kategori!="" and tahun_rilis!="" and harga!="" and stok_awal!="" ):
                tambahan=[f"GAME00{round(arrayLength(game)/6)}",nama,kategori,int(tahun_rilis),int(harga),int(stok_awal)]
                inputSelesai=True
            else:
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
                inputSelesai=False

        game = game+tambahan
        return (game)
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.")
        print("Mintalah ke administrator untuk melakukan hal tersebut.")
        return (game)


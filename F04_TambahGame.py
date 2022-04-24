from lensplit import arrayLength

def isAdmin (data_pengguna):
    # Mengecek apakah role pengguna merupakan admin atau user, jika pengguna 
    # adalah admin maka akan mengembalikan True, dan sebaliknya
    # Kamus: 
        # data_pengguna[4] : string
    # Algoritma
    if data_pengguna[4]=="admin":
        return(True)
    else:
        return (False)

def tambahgame(game,data_pengguna):
    # fungsi tambahgame akan menambahkan data sebuah game pada memori file yang berupa array
    # Kamus: 
        # nama,username,password: String
        # logged_in,found : Boolean
        # i : integer
        # data_pengguna: Array
    # Algoritma
    if isAdmin(data_pengguna): # validasi role pengguna
        inputSelesai=False
        while not inputSelesai: # algoritma looping sampai input yang dimasukkan benar (lengkap tidak ada yang kosong)
            nama= input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun_rilis= input("Masukkan tahun rilis: ")
            harga=input("Masukkan harga: ")
            stok_awal=input("Masukkan stok awal: ")
            if (nama!="" and kategori!="" and tahun_rilis!="" and harga!="" and stok_awal!="" ): 
                if arrayLength(game)//6<=9:
                    ID=f"GAME00{arrayLength(game)//6}"
                elif arrayLength(game)//6>9 and arrayLength(game)//6<=99:
                    ID=f"GAME0{arrayLength(game)//6}"
                elif arrayLength(game)//6>99 and arrayLength(game)//6<=999:
                    ID=f"GAME{arrayLength(game)//6}"
                else:
                    print("Penyimpanan data game tidak mencukupi.")
                    break
                tambahan=[ID,nama,kategori,int(tahun_rilis),int(harga),int(stok_awal)] # array game tambahan
                inputSelesai=True
                
            else:
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
                inputSelesai=False

        game = game+tambahan
        return (game)
    else: # jika bukan diakses admin
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.")
        print("Mintalah ke administrator untuk melakukan hal tersebut.")
        return (game)

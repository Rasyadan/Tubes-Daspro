import arrayFunctions
arrayLoc = arrayFunctions.ArrayLoc

def isAdmin (data_pengguna): # Cek apakah pengguna admin atau bukan
    if (data_pengguna[4] == "admin"):
        return True
    else : 
        return False

def ubah_stok(data_pengguna,file_game): # Mengubah stok pada memori dengan parameter jenis pengguna dan file csv game
    if (isAdmin(data_pengguna)): # Cek Admin atau bukan
        game_id = input("Masukkan Game ID : ")
        indeks = arrayLoc(file_game, game_id) 
        if (indeks != -1):
            stok = int(file_game[indeks+5]) # Indeks disesuaikan dengan urutan pada file
            pengubah_stok = int(input("Masukkan jumlah : "))
            if (pengubah_stok < 0):
                if(stok + pengubah_stok >= 0):
                    stok += pengubah_stok
                    file_game[indeks+5] = stok
                    print(f"Stok game {file_game[indeks+1]} berhasil dikurangi. Stok sekarang : {stok}")
                else :
                    print(f"Stok game {file_game[indeks+1]} gagal dikurangi karena stok kurang. Stok sekarang : {stok}")
            else :
                stok += pengubah_stok
                file_game[indeks+5] = str(stok)
                print(f"Stok game {file_game[indeks+1]} berhasil ditambahkan. Stok sekarang : {stok}")
        else :
            print("Tidak ada game dengan ID tersebut!")
    else :
        print("Hanya admin yang bisa mengubah stok game!")
    
    return(file_game)

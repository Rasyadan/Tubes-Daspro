# Variabel
# game_id : string, menyimpan data terkait id_game
# nama_game : string, menyimpan nama game dengan game_id terkait
# isAdmin : bool, menyimpan data apakah pengguna merupakan admin atau bukan
# pengurang_stok : integer, menyimpan angka yang akan digunakan untuk mengurangi stok
# stok_sekarang : integer, menyimpan jumlah stok game saat ini

#Alur

# Cek akses admin atau bukan ? (isAdmin)
# YES :
    # Masukkan ID Game yang stoknya akan diubah (game_id)
    # Cek apakah ID ada atau tidak ?
    # YA :
        # Input angka untuk mengurangi jumlah stok (pengurang_stok)
        # Apakah stok masih > 0 jika stok dikurangi input tersebut? (stok_sekarang, pengurang_stok, nama_game)
        # YA :
            # Kurangi stok sebesar input angka tersebut
            # Tampilkan pesan "Stok game (Nama Game dengan ID tersebut) berhasil dikurangi. Stok sekarang : (Jumlah stok game dengan ID yang berkaitan)"
        # Tidak : 
            # Tampilkan pesan error : "Stok game (Nama Game dengan ID tersebut) gagal dikurangi karena stok kurang. Stok sekarang : (Jumlah stok game dengan ID yang berkaitan) " 
    # Tidak :
        # Tampilkan pesan kesalahan : "Tidak ada game dengan ID tersebut!

# NO :
    #Tampilkan pesan error : "Hanya admin yang bisa mengubah stok game"

import arrayFunctions
from csvparser import parse
arrayLoc = arrayFunctions.ArrayLoc

def isAdmin (user_state): # Cek apakah pengguna admin atau bukan
    if (user_state == "Admin"):
        return True
    else : 
        return False

def ubah_stok(user_state,file_game): # Mengubah stok pada memori dengan parameter jenis pengguna dan file csv game
    if (isAdmin(user_state)): # Cek Admin atau bukan
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

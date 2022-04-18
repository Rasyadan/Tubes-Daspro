# Variabel :
# isAdmin : bool, menyimpan data apakah pengguna merupakan admin atau bukan
# game_id : string, menyimpan data terkait id_game
# nama_game : string, menyimpan nama game dengan game_id terkait
# kategori : string, menyimpan kategori game dengan ID terkait
# tahun_rilis : integer, menyimpan tahun rilis game dengan ID terkait
# harga : integer, menyimpan harga game dengan ID terkait.

#Alur

# Apakah akses admin?
#Ya
# Variabel : Game ID, Nama Game, Kategori, Tahun Rilis, Harga
# Input Game ID, Nama Game, Kategori, Tahun Rilis, Harga
# Cek apakah Game ID bukan string kosong
    # Ya : Ubah data-data pada game dengan game ID terkait dengan input di atas. Jika selain ID kosong, maka gunakan data yang sudah ada.
    # Tidak : Tampilkan pesan error
#No

#Import fungsi-fungsi dari modul lain
import lensplit
from csvparser import parse
from csvparser import removen
import arrayFunctions
ArrayLoc = arrayFunctions.ArrayLoc
length = lensplit.length
split = lensplit.splittext
arrayLen = lensplit.arrayLength

def changeData(input,indeks,file_game): # Prosedur mengganti data pada array game
    if (input != ""):
        file_game[indeks] = input

def isAdmin (user_state): # Cek apakah pengguna admin atau bukan
    if (user_state == "Admin"):
        return True
    else : 
        return False

def ubah_game(user_state,file_game): # Prosedur mengubah data game pada memori
    if (isAdmin(user_state)) :
        # Input Data
        game_id = input("Masukkan ID game : ")
        nama_game = input("Masukkan nama game : ")
        kategori = input("Masukkan kategori : ")
        tahun_rilis = (input("Masukkan tahun rilis : " ))
        harga = input("Masukkan harga : ")

        # Proses penggantian
        if (game_id != ""):
            indeks = ArrayLoc(file_game, game_id)
            if (indeks != -1):
                changeData(nama_game, indeks+1, file_game)
                changeData(kategori, indeks+2, file_game)
                changeData(tahun_rilis, indeks+3, file_game)
                changeData(harga, indeks+4, file_game)
            else :
                print(f"Game dengan ID {game_id} tidak ditemukan")
        else :
            print("Game ID tidak boleh kosong")
    else :
        print("Hanya admin yang dapat mengubah game")
    
    return(file_game)







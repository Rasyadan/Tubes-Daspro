#Import fungsi-fungsi dari modul lain
import lensplit
import arrayFunctions
ArrayLoc = arrayFunctions.ArrayLoc
length = lensplit.length
split = lensplit.splittext
arrayLen = lensplit.arrayLength

def changeData(input,indeks,file_game): # Prosedur mengganti data pada array game
    if (input != ""):
        file_game[indeks] = input

def ubah_game(data_pengguna,file_game): # Prosedur mengubah data game pada memori
    if (data_pengguna == "admin") :
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
        print("Hanya admin yang dapat mengubah game!")
    
    return(file_game)







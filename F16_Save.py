import os
import lensplit
import csvparser

def buat_file(filenya, array_pengganti, dir):
    # Menyimpan data yang awalnya berupa array ke file csv

    # KAMUS LOKAL
    # path, isi_file : string
    
    # ALGORITMA
    path = "./" + dir + "/" + str(filenya)
    isi_file = ""

    file_diganti = open(path, "w")

    for i in range(lensplit.arrayLength(array_pengganti)) :
        isi_file += array_pengganti[i] + "\n"
        
    file_diganti.write(isi_file)
    
    file_diganti.close()


def save(dir, arr_game, arr_riwayat, arr_user, arr_kepemilikan) :
    # Menyimpan data yang awalnya berupa array ke file csv dan menaruhnya di folder tujuan

    # KAMUS LOKAL
    # dir_tiada : boolean
    
    dir_tiada = True 
    arr_game=csvparser.tocsv(arr_game,6,"array")
    arr_user=csvparser.tocsv(arr_user,6,"array")
    arr_riwayat=csvparser.tocsv(arr_riwayat,5,"array")
    arr_kepemilikan=csvparser.tocsv(arr_kepemilikan,2,"array")
    
    # cek apakah folder ada atau tidak
    for (root,directory,files) in os.walk("./", topdown=True):
        for i in directory:
            if dir == i :   # Direktori sudah ada
                dir_tiada = False

    if dir_tiada :          # Direktori belum ada
        # buat folder baru
        os.mkdir("./" + dir)
    
    buat_file("game.csv", arr_game, dir)
    buat_file("user.csv", arr_user, dir)
    buat_file("riwayat.csv", arr_riwayat, dir)
    buat_file("kepemilikan.csv", arr_kepemilikan, dir)

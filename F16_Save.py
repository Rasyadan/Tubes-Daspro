import os
import lensplit

def buat_file(filenya, array_pengganti, dir):
    # Menyimpan data yang awalnya berupa array ke file csv

    path = "./" + dir + "/" + str(filenya)
    file_diganti = open(path, "w")

    for i in lensplit.arrayLength(array_pengganti) :
        file_diganti.write(array_pengganti[i])

    file_diganti.close()


def save(dir, arr_game, arr_riwayat, arr_user, arr_kepemilikan) :
    # Menyimpan data yang awalnya berupa array ke file csv dan menaruhnya di folder tujuan

    dir_tiada = True    

    # cek apakah folder ada atau tidak
    for (root,directory,files) in os.walk("./", topdown=True):
        for i in directory:
            if dir == i :   # Direktori sudah ada
                dir_tiada = False

    if dir_tiada :          # Direktori belum ada
        # buat folder baru
        os.mkdir("./", dir)
    
    buat_file("game.csv", arr_game, dir)
    buat_file("user.csv", arr_user, dir)
    buat_file("riwayat.csv", arr_riwayat, dir)
    buat_file("kepemilikan.csv", arr_kepemilikan, dir)
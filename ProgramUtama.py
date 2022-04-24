# Import Modul-Modul yang telah dibuat
import os
import sys
import csvparser
toArray = csvparser.toArray
tocsv = csvparser.tocsv
from F02_Register import register
from F02_Register import isAdmin
from F03_Login import login
from F04_TambahGame import tambahgame
from F05_UbahGame import ubah_game
from F06_UbahStok import ubah_stok
from F07_ListingGame import listGame
from F08_MembeliGame import buy_game
from F09_LihatGameSendiri import game_pengguna
from F10_CariGameSendiri import CariGameSendiri
from F11_CariGameDiToko import CariGameDiToko
from F12_TopUpSaldo import topup
from F13_MelihatRiwayatPembelian import riwayatPembelian
from F14_Help import Help
from F16_Save import save
from F17_Exit import exitBNMO
from B03_TicTacToe import tictactoe

import lensplit
splittext = lensplit.splittext
arrayLength = lensplit.arrayLength


# Load
try : 
    dir_name = sys.argv[1]

    is_dir_tiada = True

    for (root,directory,files) in os.walk("./"):
        for folder in direcotry:
            if dir_name == folder :
                print("Loading...")
                print('Selamat datang di antarmuka "Binomo"\n')
                is_dir_tiada = False

    if is_dir_tiada :   # Folder penyimpanan tidak ditemukan
        print('Folder ' + '"' + str(dir_name) + '"' + ' tidak ditemukan')
        # Program langsung berakhir

    else :              # Folder penyimpanan ditemukan

        # Membaca dan memasukkan data pada csv ke dalam variabel dan mengubahnya ke bentuk array (dengan fungsi toArray)
        game = toArray((open("game.csv", "r").readlines()), 6, "array") # Bentuk Array
        user = toArray((open("user.csv", "r",).readlines()), 6, "array") # Bentuk Array
        kepemilikan = toArray((open("kepemilikan.csv", "r",).readlines()), 2, "array") # Bentuk Array
        riwayat = toArray((open("riwayat.csv", "r",).readlines()), 5, "array") # Bentuk Array


        # Program
        logged_in=False
        isExit=False
        while isExit==False:
            print("Silahkan memilih opsi di bawah untuk memulai binomo")
            print("1. LOGIN")
            print("2. REGISTER")
            print("3. TAMBAH GAME")
            print("4. UBAH GAME")
            print("5. UBAH STOK GAME")
            print("6. LIST GAME")
            print("7. BELI GAME")
            print("8. LIHAT GAME USER")
            print("9. CARI GAME USER")
            print("10. CARI GAME DI TOKO")
            print("11. TOP UP")
            print("12. LIHAT RIWAYAT PEMBELIAN")
            print("13. HELP")
            print("14. SAVE")
            print("15. EXIT")
            print("16. Game Tic-Tac-Toe")

            pil=input("Ketik di sini: ")
            if (pil == "1"):
                logged_in = login(user)
                if logged_in==True:
                    data_pengguna=logged_in
            else:
                if logged_in==False:
                    print("Maaf, anda harus login terlebih dahulu")
                    print("=="*24)
                else:
                    print("Oke tunggu sebentar...")
                    print("=="*24)
                    if (pil == "2"):
                        if (isAdmin(data_pengguna)):
                            user = register(user,data_pengguna)
                    elif (pil == "3"):
                        if (isAdmin(data_pengguna)):
                            game = tambahgame(game,data_pengguna)
                    elif (pil == "4"):
                        if (isAdmin(data_pengguna)):
                            game = ubah_game("admin", game)
                        else :
                            game = ubah_game("user", game)
                    elif (pil == "5"):
                        if (isAdmin(data_pengguna)):
                            game = ubah_stok("admin", game)
                        else :
                            game = ubah_stok("user", game)
                    elif (pil == "6"):
                        listGame(game)
                    elif (pil == "7"):
                        if (isAdmin(data_pengguna[4] == "user")):
                            buy_game(game, user, kepemilikan, data_pengguna)
                    elif (pil == "8"):
                        game_pengguna(kepemilikan, game, data_pengguna)
                    elif (pil == "9"):
                        CariGameSendiri(game)
                    elif (pil == "10"):
                        CariGameDiToko(game)
                    elif (pil == "11"):
                        topup(game, user)
                    elif (pil == "12"):
                        riwayatPembelian(riwayat)
                    elif (pil == "13"):
                        Help(data_pengguna[4],logged_in)

                    elif pil=="14":
                        folder = str(input("Masukkan nama folder penyimpanan: "))
                        save(folder,arr_game=game,arr_riwayat=riwayat,arr_kepemilikan=kepemilikan,arr_user=user)

                    elif pil=="15":
                        if(exitBNMO(folder, game, riwayat, user, kepemilikan)): # Folder nya belum
                            exit()

                    elif (pil == "16"):
                        tictactoe()
                    else:
                        print("Pilihan tidak tersedia")

except IndexError: # Nama folder tidak dimasukkan
    print("Tidak ada nama folder yang diberikan!")
    # Program langsung berakhir
    

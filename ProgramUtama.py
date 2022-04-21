# Import Modul-Modul yang telah dibuat
import csvparser
toArray = csvparser.toArray
tocsv = csvparser.tocsv
from F02_Register import register
from F03_Login import login
from F04_TambahGame import tambahgame
from F05_UbahGame import ubah_game
from F06_UbahStok import ubah_stok
from F07_ListingGame import listGame
from F09_LihatGameSendiri import game_pengguna
from F10_CariGameSendiri import CariGameSendiri
from F11_CariGameDiToko import CariGameDiToko

import lensplit
splittext = lensplit.splittext
arrayLength = lensplit.arrayLength


# Membaca dan memasukkan data pada csv ke dalam variabel dan mengubahnya ke bentuk array (dengan fungsi parse)
game = toArray((open("game.csv", "r").readlines()), 6, "array") # Bentuk Array
user = toArray((open("user.csv", "r",).readlines()), 6, "array") # Bentuk Array


# Program
logged_in=False
isExit=False
while exit==False:
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
    print("14. LOAD")
    print("15. SAVE")
    print("16. EXIT")

    pil=input("Ketik di sini: ")
    if pil=="1":
        logged_in = login(user)

    else:
        if logged_in==False:
            print("Maaf, anda harus login terlebih dahulu")
            print("=="*24)
        else:
            data_pengguna=login(user)
            print("Oke tunggu sebentar...")
            print("=="*24)
            if pil=="2":
                #IF ADMIN
                user = register(user,data_pengguna)
            elif pil=="3":
                #IF ADMIN
                game = tambahgame(game,data_pengguna)
            elif pil=="4":
                # IF ADMIN :
                game = ubah_game("Admin", game)
            elif pil=="5":
                # IF ADMIN
                game = ubah_stok("Admin", game)
            elif pil=="6":
                listGame(game)
            # elif pil=="7":
            # elif pil=="8":
            elif pil=="9":
                game_pengguna(kepemilikan, game, data_pengguna) #array kepemilikan belum ada
            elif pil=="10":
                CariGameSendiri(game)
            elif pil=="11":
                CariGameDiToko(game)
            # elif pil=="12":
            # elif pil=="13":
            # elif pil=="14":

            # elif pil=="15":

            elif pil=="16":
                isExit=exit()

            else:
                print("Pilihan tidak tersedia")

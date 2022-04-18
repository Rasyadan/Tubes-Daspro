# Import Modul-Modul yang telah dibuat
import csvparser
parse = csvparser.parse
tocsv = csvparser.tocsv
from ubahgameditoko import ubah_game
from ubahstokgameditoko import ubah_stok
from listinggame import listGame

# Membaca dan memasukkan data pada csv ke dalam variabel dan mengubahnya ke bentuk array
game = parse((open("game.csv", "r").readlines()), 6) # Bentuk Array
user = parse((open("user.csv", "r",).readlines()), 6) # Bentuk Array

# Program
logged_in=False
exit=False
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
                if data_pengguna[4]=="admin":
                    register(user)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
                    print("Mintalah ke administrator untuk melakukan hal tersebut.")


            elif pil=="3":
                if data_pengguna[4]=="admin":
                    tambahgame(game)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut.") 
                    print("Mintalah ke administrator untuk melakukan hal tersebut.")
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
            # elif pil=="9":
            # elif pil=="10":
            # elif pil=="11":
            # elif pil=="12":
            # elif pil=="13":
            # elif pil=="14":

            # elif pil=="15":

            # elif pil=="16":

            else:
                print("Pilihan tidak tersedia")

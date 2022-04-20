# Import Modul-Modul yang telah dibuat
import csvparser
parse = csvparser.parse
tocsv = csvparser.tocsv
from F05_UbahGame import ubah_game
from F06_UbahStok import ubah_stok
from F07_ListingGame import listGame
import lensplit
splittext = lensplit.splittext
arrayLength = lensplit.arrayLength


# Membaca dan memasukkan data pada csv ke dalam variabel dan mengubahnya ke bentuk array (dengan fungsi parse)
game = parse((open("game.csv", "r").readlines()), 6) # Bentuk Array
user = parse((open("user.csv", "r",).readlines()), 6) # Bentuk Array

# Fungsi-Fungsi Program
def login(user):
    username = (input("Masukkan username: "))
    password = (input("Masukkan password: "))
    logged_in=True
    found=False
    i=1 
    while i<=(arrayLength(user)-1) and not found:
        data=splittext(user[i],";")
        if data[1]==username:
                if data[3]==password:
                    data_pengguna = splittext(user[i],";")
                    print("Halo",data_pengguna[2]+"!","Selamat datang di Binomo")
                    logged_in=True
                    print("=="*24)
                    return data_pengguna
                else:
                    print("Password Anda salah")
                found=True            
        i+=1
    if not found:
        print("Username tidak ditemukan")
    return logged_in==False

def register(user):
    nama= input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password= input("Masukkan password: ")
    found=False
    i=1

    while i<=(arrayLength(user)-1) and not found:
            data=splittext(user[i],";")
            if data[1]==username:
                found=True
            else:
                i+=1
    if found==True :
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
    else:
        tambahan = f"{arrayLength(user)};{username};{nama};{password};user;0"
        user = ((open("C:/Users/ASUS/OneDrive/Dokumen/TUBES/user.csv", "a").write(f"{tambahan}/n")))
    
def tambahgame(game):
    game = ((open("C:/Users/ASUS/OneDrive/Dokumen/TUBES/game.csv", "r").readlines()))
    inputSelesai=False
    while not inputSelesai:
        nama= input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis= int(input("Masukkan tahun rilis: "))
        harga=int(input("Masukkan harga: "))
        stok_awal=int(input("Masukkan stok awal: "))
        if (nama!="" and kategori!="" and tahun_rilis!="" and harga!="" and stok_awal!="" ):
            tambahan=f"GAME00{arrayLength(game)};{nama};{kategori};{tahun_rilis};{harga};{stok_awal}"
            inputSelesai
            break
        else:
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            inputSelesai=False

    game = ((open("C:/Users/ASUS/OneDrive/Dokumen/TUBES/game.csv", "a").write(f"{tambahan}\n")))




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

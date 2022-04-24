from F09_LihatGameSendiri import findIn
from lensplit import length

def CariGameDiToko(game):
    #Program mencari game di toko berdasarkan masukan kategori yang diberikan user
    
    #Kamus Lokal
    #idgame, nama, harga, kategori, tahun : string
    #filtered : array of array

    #Algoritma
    #masukan berbagai kategori untuk mencari game yang ada di toko
    idgame = input('Masukkan ID Game: ')
    nama = input('Masukkan Nama Game: ')
    kategori = input('Masukkan Kategori Game: ')
    tahun = input('Masukkan Tahun Rilis Game: ')
    harga = input('Masukkan Harga Game: ')
    
    #memfilter kategori berdasarkan input user
    filtered = findIn(idgame, 0, game)
    filtered = findIn(nama, 1, filtered)
    filtered = findIn(kategori, 2, filtered)
    filtered = findIn(tahun, 3, filtered)
    filtered = findIn(harga, 4, filtered)

    if length(filtered) > 0:
        #ketika ditemukan hasil setelah input user
        #mencetak hasil dari filter yang dibutuhkan
        for j in range(length(filtered)):
            print(filtered[j][0], end = ' | ')
            print('{:21.20}|'.format(filtered[j][1]), end=' ')
            print('{:13.12}|'.format(filtered[j][2]), end=' ')
            print('{:5.4}|'.format(filtered[j][3]), end=' ')
            print('{:7.6}|'.format(filtered[j][4]), end=' ')
            print(filtered[j][5])
    else:
        #ketika tidak ada hasil yang memenuhi input kategori
        print('Tidak ada game di toko yang memenuhi kriteria')


from F09_LihatGameSendiri import findIn
from lensplit import length

def CariGameDiToko(game):
    #Program mencari game di toko berdasarkan masukan kategori yang diberikan user
    
    #Kamus Lokal
    #idgame, nama, harga, kategori, tahun : string
    #filtered : array of array

    #Algoritma
    #masukan berbagai kategori untuk mencari game yang ada di toko
    idgame = input('Masukkan ID Game: ')
    nama = input('Masukkan Nama Game: ')
    kategori = input('Masukkan Kategori Game: ')
    tahun = input('Masukkan Tahun Rilis Game: ')
    harga = input('Masukkan Harga Game: ')
    
    #memfilter kategori berdasarkan input user
    filtered = findIn(idgame, 0, game)
    filtered = findIn(nama, 1, filtered)
    filtered = findIn(kategori, 2, filtered)
    filtered = findIn(tahun, 3, filtered)
    filtered = findIn(harga, 4, filtered)

    if length(filtered) > 0:
        #ketika ditemukan hasil setelah input user
        #mencetak hasil dari filter yang dibutuhkan
        for j in range(length(filtered)):
            print(filtered[j][0], end = ' | ')
            print('{:21.20}|'.format(filtered[j][1]), end=' ')
            print('{:13.12}|'.format(filtered[j][2]), end=' ')
            print('{:5.4}|'.format(filtered[j][3]), end=' ')
            print('{:7.6}|'.format(filtered[j][4]), end=' ')
            print(filtered[j][5])
    else:
        #ketika tidak ada hasil yang memenuhi input kategori
        print('Tidak ada game di toko yang memenuhi kriteria')


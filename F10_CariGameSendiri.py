from F09_LihatGameSendiri import findIn
from lensplit import length

def CariGameSendiri(game):
    #Program yang mencari game pada inventory sendiri

    #Kamus Lokal
    #idgame, tahun : string
    #filtered : array of array

    #Algoritma
    #masukan kategori berdasarkan game ID dan tahun rilis
    idgame = input('Masukkan ID Game: ')
    tahun  = input('Masukkan Tahun Rilis Game: ')

    #memfilter game yang ada di inventory berdasarkan masukan user
    filtered = findIn(idgame, 0, game)
    filtered = findIn(tahun, 3, filtered)

    if length(filtered) > 0:
        #ketika ditemukan hasil
        #mencetak tabel sesuai dengan hasil
        for j in range(length(filtered)):
            print(filtered[j][0], end = ' | ')
            print('{:21.20}|'.format(filtered[j][1]), end=' ')
            print('{:13.12}|'.format(filtered[j][2]), end=' ')
            print('{:5.4}|'.format(filtered[j][3]), end=' ')
            print('{:7.6}'.format(filtered[j][4]))
    else:
        #ketika tidak ada hasil yang sesuai dengan input user
        print('Tidak ada game di inventory-mu yang memenuhi kriteria')

#untuk ngetes aja
#game = [["GAME001", "Azril Multazam Pambudi", "Kategori", "2022", "10000", "0"], ["GAME003", "Tes", "Kategori", "2022", "10000", "2"]]
#CariGameSendiri(game)
from F09_LihatGameSendiri import findIn
from lensplit import length
from csvparser import tocsv
from csvparser import toArray

def CariGameSendiri(kepemilikan, games, userlogged):
    #Program yang mencari game pada inventory sendiri

    #Kamus Lokal
    #idgame, tahun : string
    #filtered : array of array
    #file_kepemilikan; file_games : array

    #Algoritma
    file_games = tocsv(games, 6, "array")
    file_games = toArray(file_games, 6, "matriks")
    file_kepemilikan = tocsv(kepemilikan, 2, "array")
    file_kepemilikan = toArray(file_kepemilikan, 2, "matriks")
    
    game_pengguna = findIn(userlogged[0], 1, file_kepemilikan)
    
    result = []
    for game in game_pengguna:
        result += [findIn(game[0], 0, file_games)[0]]

    #masukan kategori berdasarkan game ID dan tahun rilis
    idgame = input('Masukkan ID Game: ')
    tahun  = input('Masukkan Tahun Rilis Game: ')

    #memfilter game yang ada di inventory berdasarkan masukan user
    filtered = findIn(idgame, 0, result)
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
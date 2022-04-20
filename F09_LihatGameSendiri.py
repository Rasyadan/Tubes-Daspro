from lensplit import length

def findIn(toFind, column, array):
    #Fungsi untuk mencari salah satu komponen pada suatu array

    #Kamus Lokal
    #res : array

    #Algoritma
    res = []
    #memeriksa komponen apakah ada atau tidak
    if toFind != "":
        #ketika komponen terdapat pada salah satu kategori/kolom, maka array akan ditambahkan ke toFind
        for i in range(length(array)):
            if toFind == array[i][column]:
                res += [array[i]]
    else:
        #ketika tidak ditemukan, maka array akan sama (tanpa ubahan)
        res = array

    return res
    

def game_pengguna(kepemilikan, games, userlogged):
    #Prosedur yang mereturn game milik pengguna

    #Kamus Lokal
    #find_game, game_found : array of array
    #temp : array

    # ALGORITMA
    game_pengguna = findIn(str(userlogged[0]+1), 1, kepemilikan)

    result = []
    for game in game_pengguna:
        result += findIn(game[0], 0, games)[0]

    if length(result) == 0:
        print("Gaada gan")
    else:
        for j in range(length(result)):
            print(result[j][0], end = " | ")
            print("{:21.20}|".format(result[j][1]), end=" ")
            print("{:13.12}|".format(result[j][2]), end=" ")
            print("{:5.4}|".format(result[j][3]), end=" ")
            print("{:7.6}|".format(result[j][4]), end=" ")
            print(result[j][5])

#user = [1, "azril", "Azril Multazam", "cepirit", "user", 10]
#kepemilikan = [["GAME001", 2], ["GAME002", 2]]
#game = [["GAME001", "Azril Multazam Pambudi", "Kategori", "2022", "10000", "0"], ["GAME003", "Tes", "Kategori", "2022", "10000", "2"]]
#game_pengguna(kepemilikan, game, user)
def tictactoe():
    game_board = [["" for i in range(3)] for j in range(3)]

    # Isi board dengan #
    for i in range(3):
        for j in range(3):
            game_board[i][j] = "#"

    print("Legenda")
    print("# = kosong")
    print("X = Pemain 1")
    print("O = Pemain 2")
    printPapanGame(game_board)

    menang = False
    giliran = "X"

    while (menang != True):
        if (CekKemenangan(game_board)):
            menang = True
        else :
            if (giliran == "X"):
                print("Giliran Pemain X")
                posX = int(input("Posisi X (1-3) :"))
                posY = int(input("Posisi Y (1-3) :"))
                if(ValidasiInputPosisi(posX, posY)):
                    if(CekIsiPapan(game_board, posX, posY)):
                        game_board[posY-1][posX-1] = "X"
                        printPapanGame(game_board)
                        giliran = "O"
                    else :
                        print("Kotak sudah terisi. Silakan memilih kotak lain.")
                else :
                    print("Posisi Kotak Tidak Valid")

            else :
                print("Giliran Pemain O")
                posX = int(input("Posisi X (1-3) :"))
                posY = int(input("Posisi Y (1-3) :"))
                if(ValidasiInputPosisi(posX, posY)):
                    if(CekIsiPapan(game_board, posX, posY)):
                        game_board[posY-1][posX-1] = "O"
                        printPapanGame(game_board)
                        giliran = "X"
                    else :
                        print("Kotak sudah terisi. Silakan memilih kotak lain.")
                        print("")
                else :
                    print("Posisi Kotak Tidak Valid")

def printPapanGame(papan):
    print("")
    print("Status Papan : ")
    for i in range(3):
        for j in range(3):
            if (j != 2):
                print(papan[i][j], end="")
            else :
                print(papan[i][j])

def ValidasiInputPosisi(posisiX,posisiY):
    if (posisiX >= 1 and posisiX <= 3):
        if (posisiY >= 1 and posisiY <= 3):
            return True
        else :
            return False
    else :
        return False

def CekIsiPapan(papan, posX, posY):
    if (papan[posY-1][posX-1] == "#"):
        return True
    else :
        return False
            
def CekKemenangan(papan):
    countX = 0
    countO = 0
    # Cek Horizontal
    for i in range(3):
        for j in range(3):
            if (papan[i][j] == "X"):
                countX += 1
            elif (papan[i][j] == "O"):
                countO += 1
            
            if (countX == 3):
                print("Pemain X menang")
                return True
            elif (countO == 3):
                print("Pemain O menang")
                return True
        countX = 0
        countO = 0    
    
    # Cek Vertikal
    for i in range(3):
        for j in range(3):
            if (papan[j][i] == "X"):
                countX += 1
            elif (papan[j][i] == "O"):
                countO += 1
            
            if (countX == 3):
                print("Pemain X menang")
                return True
            elif (countO == 3):
                print("Pemain O menang")
                return True
        countX = 0
        countO = 0     

    # Cek Diagonal
    for i in range(3):
        if (papan[i][i] == "X"):
            countX += 1
        elif (papan[i][i] == "O"):
            countO += 1
            
        if (countX == 3):
            print("Pemain X menang")
            return True
        elif (countO == 3):
            print("Pemain O menang")
            return True
    countX = 0
    countO = 0
    
    for i in range(3):
        j = 2 - i
        if (papan[i][j] == "X"):
            countX += 1
        elif (papan[i][j] == "O"):
            countO += 1
            
        if (countX == 3):
            print("Pemain X menang")
            return True
        elif (countO == 3):
            print("Pemain O menang")
            return True
    countX = 0
    countO = 0 

    # Cek Seri
    empty = 9
    for i in range(3):
        for j in range(3):
            if (papan[i][j] != "#"):
                empty -= 1
    if (empty == 0):
        print("Seri. Tidak ada yang menang.")
        return True
    
tictactoe()
            
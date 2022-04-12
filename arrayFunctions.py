import lensplit
arrayLen = lensplit.length

def ArrayLoc(array,search): # Menghasilkan indeks dari data yang dicari(parameter search)
    found = False
    for i in range(arrayLen(array)):
        if (search == array[i]):
            found = True
            return i
    if (found == False):
        return -1
        
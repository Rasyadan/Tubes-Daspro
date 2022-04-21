import lensplit
split = lensplit.splittext
arrayLen = lensplit.arrayLength

def removen(array): # Menghapus "\n dari data yang diperoleh dari csv"
    for j in range(arrayLen(array)): 
        array[j] = (split(array[j], "\n"))
    result = ["" for i in range(arrayLen(array))]
    
    for i in range(arrayLen(array)):
        result[i] = (array[i])[0]
    return(result)       


def toArray(array,jumlah_kategori,pilihan): 
    # Mengubah bentuk file csv menjadi array sehingga bisa diubah dalam memori/variabel
    # jumlah_kategori adalah jumlah kategori dalam sebuah file csv
    no_N_array = removen(array)
    if (pilihan == "array"):
        result_array = ["" for i in range(jumlah_kategori*(arrayLen(no_N_array)))]
        temp_array = ["" for i in range(jumlah_kategori)]

        for i in range(0, arrayLen(no_N_array)):
            temp_array = split(no_N_array[i], ";") # Memisahkan tiap data dengan separator ";" dan memasukkan ke dalam temporary array
            for j in range(1,jumlah_kategori+1):
                result_array[(j-1) + (jumlah_kategori*(i))] = temp_array[j-1] # Memindahkan hasil dari temporary array ke array result
    
    else : #pilihan == "matriks"
        result_array = [["" for i in range(jumlah_kategori)] for j in range(arrayLen(array))]
        temp_array = ["" for i in range(jumlah_kategori)]

        for i in range(arrayLen(array)):
            temp_array = split(no_N_array[i], ";")
            for j in range(jumlah_kategori):
                result_array[i][j] = temp_array[j]
    
    return(result_array)

def tocsv(array, jumlah_kategori): 
    #Mengubah bentuk array data menjadi bentuk csv
    csv_array = ["" for i in range(arrayLen(array)//jumlah_kategori)]
    temp_string = ""
    for i in range(arrayLen(array)//jumlah_kategori):
        temp_string = ""
        for j in range(jumlah_kategori):
            if (j != 5) :
                temp_string += (array[j + (jumlah_kategori*i)] + ";") # Menambahkan separator ";"
            else :
                temp_string += array[j + (jumlah_kategori*i)] + "\n" # Menambahkan endline \n untuk akhir data csv
        csv_array[i] = temp_string
    return(csv_array)

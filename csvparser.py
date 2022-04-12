import lensplit
length = lensplit.length
split = lensplit.splittext
arrayLen = lensplit.arrayLength
game = ((open("game.csv", "r").readlines()))
#Import parsenya aja buat parse csv

def removen(array):
    for j in range(arrayLen(array)):
        array[j] = (split(array[j], "\n"))
    result = ["" for i in range(arrayLen(array))]
    for i in range(arrayLen(array)):
        result[i] = (array[i])[0]
    return(result)       


def parse(array):
    raw_csv_array = removen(array)
    result_array = ["" for i in range(6*(arrayLen(raw_csv_array)))]
    temp_array = ["" for i in range(6)]

    for i in range(0, arrayLen(raw_csv_array)):
        temp_array = split(raw_csv_array[i], ";")
        for j in range(1,7):
            result_array[(j-1) + (6*(i))] = temp_array[j-1]
    
    return(result_array)

def tocsv(array): #Mengubah bentuk array data menjadi bentuk csv
    csv_array = ["" for i in range(arrayLen(array)//6)]
    temp_string = ""
    for i in range(arrayLen(array)//6):
        temp_string = ""
        for j in range(6):
            if (j != 5) :
                temp_string += (array[j + (6*i)] + ";") 
            else :
                temp_string += array[j + (6*i)] + "\n"
        csv_array[i] = temp_string
    return(csv_array)

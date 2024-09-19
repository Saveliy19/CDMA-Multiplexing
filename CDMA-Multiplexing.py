import numpy as np

def make_walsh_matrix(order: int) -> np.ndarray:
    if order == 0:
        return np.array([[1]])
    else:
        BASE = make_walsh_matrix(order - 1)
        TOP = np.hstack((BASE, BASE))
        BOTTOM = np.hstack((BASE, -1 * BASE))
        RES = np.vstack((TOP, BOTTOM))
        return RES

def binary_array_to_string(binary_array):
    # разделяем массив на группы по 8 бит
    byte_values = [binary_array[i:i+8] for i in range(0, len(binary_array), 8)]
    
    # каждый бит - символ
    characters = [chr(int(''.join(map(str, byte)), 2)) for byte in byte_values]
    return ''.join(characters)


if __name__ == '__main__':
    # задаем словарь кодов станций
    station_codes = {
    }
    station_words = {

    }
    decoded_words = {
        
    }
    print("Введите через пробел название станции \nи слово, которое она передает.\nДля завершения ввода введите пустую строку.")
    while True:
        try:
            station, word = map(str, input().split(' '))
        except ValueError:
            break
        else:
            station_codes[station] = []
            decoded_words[station] = []
            st_str = ''.join(format(ord(char), '08b') for char in word)
            station_words[station] = [int(bit) for bit in st_str]

    # длина самого большого слова
    max_length = 0

    # определяем самое длинное слово
    for key, value in station_words.items():
        current_length = len(value)
        if current_length > max_length:
            max_length = current_length

    # генерируем матрицу Уолша
    walsh_codes_matrix = make_walsh_matrix(2**(len(station_codes) - 1) - 1)
    print(walsh_codes_matrix)

    # указываем длину кодов станций
    size = len(walsh_codes_matrix[0])

    i = 0
    # каждой станции присваиваем строку из матрицы Уолша
    for key in station_codes:
        station_codes[key] = walsh_codes_matrix[i]
        i+=1

    # считаем сумму сигналов    
    signal_summ = np.zeros(size)

    # чтобы все слова могли быть разной длины, берем  длину наибольшего слова
    for i in range(max_length):
        signal_summ.fill(0)

        for key, value in station_words.items():
            # проверка, чтоб не выйти за границы массива
            if i < len(value):
                if value[i] == 1:
                    signal_summ += station_codes[key]
                elif value[i] == 0:
                    signal_summ -= station_codes[key]
        
        # расшифровка, что передала каждая из станций за такт
        for key in decoded_words:
            value = np.dot(signal_summ, station_codes[key]) / size
            if value == -1:
                decoded_words[key].append(0)
            elif value == 1:
                decoded_words[key].append(1)
            else:
                continue
    
    for key, value in decoded_words.items():
        print(f'{key} says {binary_array_to_string(value)}')
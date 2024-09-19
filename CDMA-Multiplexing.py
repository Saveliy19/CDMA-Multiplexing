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



if __name__ == '__main__':
    # задаем словарь кодов станций
    stantion_codes = {
    }
    stantion_words = {

    }
    print("Введите через пробел название станции \nи слово, которое она передает.\nДля завершения ввода введите пустую строку.")
    while True:
        try:
            stantion, word = map(str, input().split(' '))
        except ValueError:
            break
        else:
            stantion_codes[stantion] = []
            stantion_words[stantion] = ''.join(format(ord(char), '08b') for char in word)

    # генерируем матрицу Уолша
    walsh_codes_matrix = make_walsh_matrix(len(stantion_codes) - 1)

    i = 0
    # каждой станции присваиваем строку из матрицы Уолша
    for key in stantion_codes:
        stantion_codes[key] = walsh_codes_matrix[i]
        i+=1

    print(stantion_codes)
    print(stantion_words)

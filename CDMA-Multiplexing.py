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
    print("Введите название матрицы или пустую строку для завершения.")
    while True:
        stantion = str(input())
        if stantion == '':
            break
        else:
            stantion_codes[stantion] = []

    walsh_codes_matrix = make_walsh_matrix(len(stantion_codes) - 1)

    i = 0
    for key in stantion_codes:
        stantion_codes[key] = walsh_codes_matrix[i]
        i+=1

    print(stantion_codes)

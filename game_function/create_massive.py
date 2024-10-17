import random as r

import numpy as np


def create_massive(n: int = 12) -> np.array:
    massive = np.array([[0 for i in range(10)] for j in range(10)])
    for mine in range(n):
        while True:
            i = r.randint(0, 9)
            j = r.randint(0, 9)
            if massive[i][j] == 0:
                massive[i][j] = 1
                break

    return massive


def mines_around(i, j, massive: np.array) -> int:
    if i == 0 and j == 0:
        return massive[i + 1][j] + massive[i][j + 1] + massive[i + 1][j + 1]
    elif i == 0 and j == 9:
        return massive[i + 1][j] + massive[i][j - 1] + massive[i + 1][j - 1]
    elif i == 9 and j == 0:
        return massive[i - 1][j] + massive[i][j + 1] + massive[i - 1][j + 1]
    elif i == 9 and j == 9:
        return massive[i - 1][j] + massive[i][j - 1] + massive[i - 1][j - 1]
    elif i == 0:
        return massive[i + 1][j] + massive[i][j + 1] + massive[i][j - 1] + massive[i + 1][j + 1] + massive[i + 1][j - 1]
    elif i == 9:
        return massive[i - 1][j] + massive[i][j + 1] + massive[i][j - 1] + massive[i - 1][j + 1] + massive[i - 1][j - 1]
    elif j == 0:
        return massive[i + 1][j] + massive[i - 1][j] + massive[i][j + 1] + massive[i + 1][j + 1] + massive[i - 1][j + 1]
    elif j == 9:
        return massive[i + 1][j] + massive[i - 1][j] + massive[i][j - 1] + massive[i + 1][j - 1] + massive[i - 1][j - 1]
    else:
        return massive[i + 1][j] + massive[i - 1][j] + massive[i][j + 1] + massive[i][j - 1] + massive[i + 1][j + 1] + \
            massive[i + 1][j - 1] + massive[i - 1][j + 1] + massive[i - 1][j - 1]




if __name__ == '__main__':
    k = create_massive()
    print(k)
    print(mines_around(5, 5, k))

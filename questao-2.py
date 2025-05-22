import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main(argv):

    imageName = argv[0] if len(argv) > 0 else 'lena_ruido.bmp'

    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)

    kernel_1 = (1/5) * np.array([[0, 1, 0],
                             [1, 1, 1],
                             [0, 1, 0]], dtype=np.float32)

    kernel_2 = (1/9) * np.ones((3, 3), dtype=np.float32)

    kernel_3 = (1/32) * np.array([[1, 3, 1],
                              [3, 16, 3],
                              [1, 3, 1]], dtype=np.float32)

    kernel_4 = (1/8) * np.array([[0, 1, 0],
                             [1, 4, 1],
                             [0, 1, 0]], dtype=np.float32)


    filtro_1 = cv.filter2D(src, -1, kernel_1)
    filtro_2 = cv.filter2D(src, -1, kernel_2)
    filtro_3 = cv.filter2D(src, -1, kernel_3)
    filtro_4 = cv.filter2D(src, -1, kernel_4)

    filtro_mediana = cv.medianBlur(src, 3)


    titulos = ["Original", "Filtro 1 (1/5)", "Filtro 2 (1/9)",
           "Filtro 3 (1/32)", "Filtro 4 (1/8)", "Filtro da Mediana"]
    imagens = [src, filtro_1, filtro_2, filtro_3, filtro_4, filtro_mediana]

    plt.figure(figsize=(15, 10))
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(imagens[i], cmap='gray')
        plt.title(titulos[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])

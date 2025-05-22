import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
    window_name = "Edge detection"
    imageName = argv[0] if len(argv) > 0 else 'lena_gray.bmp'

    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)

    if src is None:
        print ('Erro ao abrir imagem' )
        print ('Argumentos do programa: [nome_da_imagem -- default lena_gray.bmp]')
        return -1

    # filtro Prewitt
    kernelx = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]], dtype=np.float32)

    kernely = np.array([[ 1,  1,  1],
                        [ 0,  0,  0],
                        [-1, -1, -1]], dtype=np.float32)

    prewitt_x = cv.filter2D(src, -1, kernelx)
    prewitt_y = cv.filter2D(src, -1, kernely)

    prewitt_combined = cv.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

    # filtro Sobel
    sobel_x = cv.Sobel(src, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(src, cv.CV_64F, 0, 1, ksize=3)

    sobel_combined = cv.addWeighted(cv.convertScaleAbs(sobel_x), 0.5,cv.convertScaleAbs(sobel_y), 0.5, 0)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.imshow(prewitt_x, cmap='gray')
    plt.title('Prewitt X')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(prewitt_y, cmap='gray')
    plt.title('Prewitt Y')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.imshow(prewitt_combined, cmap='gray')
    plt.title('Prewitt - Combinação')
    plt.axis('off')

    plt.subplot(2, 3, 4)
    plt.imshow(cv.convertScaleAbs(sobel_x), cmap='gray')
    plt.title('Sobel X')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.imshow(cv.convertScaleAbs(sobel_y), cmap='gray')
    plt.title('Sobel Y')
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plt.imshow(sobel_combined, cmap='gray')
    plt.title('Sobel - Combinação')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])

    
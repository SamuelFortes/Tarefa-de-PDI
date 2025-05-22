import sys
import cv2 as cv

def main(argv):
    window_name = "Highboost Filter"
    imageName = argv[0] if len(argv) > 0 else 'lena_gray.bmp'

    # Lê a imagem em BGR
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    if src is None:
        print('Erro ao abrir imagem')
        print('Argumentos do programa: [nome_da_imagem -- default lena_gray.bmp]')
        return -1

    # filtragem Highboost - fórmula:
    # Highboost=Imagem original+(A−1)⋅(Imagem original−Imagem suavizada)

    A = 2.0
    # 'A' controla o quanto a imagem original será realçada em relação à versão suavizada (borrada)

    # Aplica desfoque gaussiano
    blurred = cv.GaussianBlur(src, (3, 3), 0)

    # Converte para float32 para evitar saturação ao subtrair/somar
    src_f = src.astype('float32')
    blurred_f = blurred.astype('float32')

    # Calcula a máscara de nitidez
    mask = cv.subtract(src_f, blurred_f)
    highboost_f = src_f + (A - 1) * mask

    highboost = cv.convertScaleAbs(highboost_f)

    # Mostra o resultado
    cv.imshow(window_name, highboost)
    k = cv.waitKey(0)

    if k == ord("s"): # imagem após a aplicação da máscara é salva se a tecla 's' for pressionada
        cv.imwrite("lena_gray copy.bmp", highboost)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
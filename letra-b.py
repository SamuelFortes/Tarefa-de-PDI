import sys
import cv2 as cv

def main(argv):
    window_name = "Unsharp Masking"
    imageName = argv[0] if len(argv) > 0 else 'lena_gray.bmp'

    # Lê a imagem em BGR
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR)
    if src is None:
        print('Erro ao abrir imagem')
        print('Argumentos do programa: [nome_da_imagem -- default lena_gray.bmp]')
        return -1

    # Aplica desfoque gaussiano
    blurred = cv.GaussianBlur(src, (3, 3), 0)

    # Converte para float32 para evitar saturação ao subtrair/somar
    src_f = src.astype('float32')
    blurred_f = blurred.astype('float32')

    # Calcula a máscara de nitidez
    mask = cv.subtract(src_f, blurred_f)

    unsharp = cv.add(src_f, mask)

    # Converte de volta para uint8
    unsharp = cv.convertScaleAbs(unsharp)

    # Mostra o resultado
    cv.imshow(window_name, unsharp)
    k = cv.waitKey(0)

    if k == ord("s"): # imagem após a aplicação da máscara é salva se a tecla 's' for pressionada
        cv.imwrite("lena_gray copy.bmp", unsharp)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
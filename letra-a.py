import sys
import cv2 as cv

def main(argv):
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplacino"

    imageName = argv[0] if len(argv) > 0 else 'lena_gray.bmp'

    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR) # Carrega uma imagem

     # Verificando se a imagem foi carregada corretamente
    if src is None:
        print ('Erro ao abrir imagem' )
        print ('Argumentos do programa: [nome_da_imagem -- default lena_gray.bmp]')
        return -1

    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # aplicando a função laplaciano
    laplaciano  = cv.Laplacian(src, ddepth, ksize=kernel_size)

    laplaciano  = cv.convertScaleAbs(laplaciano)
  
    cv.imshow(window_name, laplaciano)
    k = cv.waitKey(0)

    if k == ord("s"): # imagem após a aplicação do filtro é salva se a tecla 's' for pressionada
        cv.imwrite("lena_gray.bmp", laplaciano )

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
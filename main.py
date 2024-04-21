import pyautogui
from PIL import Image, ImageGrab
import numpy as np
from time import sleep
import keyboard 



def tirar_print(x1,y1,x2,y2):
    """
    Recebe as coordedanas
    Retorna uma matriz RGB
    """
    screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # Converter em tons de cinza
    screen = screen.convert('L')
    #threshold é o divisor, a partir de qual cor será preto ou branco
    threshold = 140
    screen_matriz = np.array(screen)
    # Aplica o limiar para binarizar a image
    binario_matriz = np.where(screen_matriz < threshold, 0, 255)
    # Converte a matriz numpy de volta para uma image PIL
    binary_image = Image.fromarray(binario_matriz.astype(np.uint8))
    binary_image.save("salvar_imagem.png")
    return binario_matriz


def pegar_coordenadas(screen_matriz):
    """
    Recebe uma matriz binarizada, o pixel  ou ẽ 0 ou é 255
    Retorna a primeira coordenada que tem cor preta
    """
    altura, largura = screen_matriz.shape
    for y_image_reverse, linha in enumerate(reversed(screen_matriz)):
        for x_image, pixel in enumerate(linha):
            if pixel == 0:
                y_image = altura+1 - y_image_reverse
                return (x_image, y_image)



def converter_coordenadas(x_base, y_base, x_imagem, y_imagem):
    """
    Recebe coordenadas da base da imagem e as coordenadas da imagem
    Retorn as coordenadas da tela para o click
    """
    x_tela = x_base + x_imagem
    y_tela = y_base + y_imagem
    return (x_tela, y_tela)


def monitorar_jogo(x1, y1, x2, y2):
    x_anterior = 0
    y_anterior = 0
    while True:
        if keyboard.is_pressed('q'):
            break
        else:
            try:
                # Captura a tela e a converte em uma matriz
                screen_matriz = tirar_print(x1, y1, x2, y2)
                # Função que pega a primeira coordenadas na imagem
                coord_imagem_x, coord_imagem_y = pegar_coordenadas(screen_matriz=screen_matriz)
                # Converter coord_imagem para coord_screen
                coord_tela_x, coord_tela_y = converter_coordenadas(x1,y1,coord_imagem_x, coord_imagem_y)
                # Desconto
                coord_tela_x += 5
                #coord_tela_y += 5
                # clicar no pixel
                if coord_tela_x != x_anterior:
                    pyautogui.click(coord_tela_x, coord_tela_y)
                    x_anterior, y_anterior = coord_tela_x, coord_tela_y
                    print(coord_tela_x, coord_tela_y)
            except:
                pass

# ==========Código Estruturado===========
#Tamanho da Tela Size(width=1280, height=800)
#top-left: Point(x=310, y=197)
#top-right: Point(x=642, y=197)
#bottom-left: Point(x=310, y=751)
#bottom-right: Point(x=642, y=751)

# Posições da tela a serem monitoradas
x1 = 310
x2 = 642
y1 = 297
#y2 = 751
y2 = 601
# inicial serve para pular o start
#y2_inicial = 501

# esperar 5 segundos pra dar tempo de colocar na tela do jogo
sleep(5)
# monitorar
monitorar_jogo(x1,y1, x2, y2)





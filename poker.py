import pyautogui
import psutil
import cv2  
import numpy as np
import matplotlib.pyplot as plt

#Check PokerStars is open
name = "PokerStars" 
found = any(name in p.name() for p in psutil.process_iter())

'''
screenshot = pyautogui.screenshot(region=(x, y, width, height))  # Ajusta la región a tus cartas
screenshot.save('board.png')

board = cv2.imread('board.png', cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(board, 120, 255, cv2.THRESH_BINARY)  # Umbral adaptativo

# Cortar area del board para sacar las cartas
'''

# Leer la imagen desde la ruta especificada
board = cv2.imread('poker_screenshots/pf1.png')

# Coordenadas fijas de la región de las cartas (x, y, width, height)
x, y, w, h = 867, 638, 187, 78

# Dibuja un rectángulo en la imagen original para mostrar la región seleccionada
cv2.rectangle(board, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Color azul (BGR) y grosor 2

# Mostrar la imagen con el rectángulo dibujado
cv2.imshow('Región seleccionada', board)

# Cortar la región seleccionada de la imagen original
carta = board[y:y + h, x:x + w]

# Convertir la región de la carta a escala de grises
carta_gris = cv2.cvtColor(carta, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para destacar los números y palos
_, carta_thresh = cv2.threshold(carta_gris, 127, 255, cv2.THRESH_BINARY)

# Mostrar la carta umbralizada para verificar el resultado
cv2.imshow('Carta Umbralizada', carta_thresh)

# Esperar a que el usuario presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

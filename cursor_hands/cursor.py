import pyautogui
import math

# Controlador de Cursor com Suavização
class ControladorCursor:
    def __init__(self, suavizacao=5):
        self.prev_x = 0 
        self.prev_y = 0
        self.smooth_factor = suavizacao #
        self.screen_w, self.screen_h = pyautogui.size() 
        # Obtém a resolução da tela
        self.clicando = False

    # Método para mover o cursor suavemente
    def mover_cursor(self, dedo_x, dedo_y):
        target_x = self.screen_w * dedo_x
        target_y = self.screen_h * dedo_y

        curr_x = self.prev_x + (target_x - self.prev_x) / self.smooth_factor
        curr_y = self.prev_y + (target_y - self.prev_y) / self.smooth_factor

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x = curr_x
        self.prev_y = curr_y

    # Método para clicar 
    def detectar_clique(self, dedo1_x, dedo1_y, dedo2_x, dedo2_y, limiar=40):
        
        x1, y1 = self.screen_w * dedo1_x, self.screen_h * dedo1_y
        x2, y2 = self.screen_w * dedo2_x, self.screen_h * dedo2_y

        dist = math.hypot(x2 - x1, y2 - y1) # Calcula a distância entre os dedos

        if dist < limiar: # se a distância for menor que o limiar
            if not self.clicando:
                self.clicando = True
                pyautogui.click()
        else:
            self.clicando = False
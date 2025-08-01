import cv2
import mediapipe as mp

# Inicializa o MediaPipe para detecção de mãos
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

class DetectorDeMaos:
    def __init__(self, max_maos=1):
        # Inicializa o MediaPipe Hands com o número máximo de mãos
        self.hands = mp_hands.Hands (max_num_hands=max_maos) 
        self.desenhador = mp_draw

    def detectar_maos(self, img):
        # Converte a imagem de BGR para RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        return results

    def desenhar_maos(self, img, landmarks):
        # Desenha as landmarks das mãos na imagem
        for hand_landmarks in landmarks:
            self.desenhador.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

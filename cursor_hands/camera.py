import cv2

# Inicializa a câmera com resolução
def inicializar_camera(w=640, h=480):
    cap = cv2.VideoCapture(0) # Captura da câmera padrão
    if not cap.isOpened():
        raise Exception("Não foi possível abrir a câmera.")
    cap.set(3, w) # Define a largura da câmera
    cap.set(4, h) # Define a altura da câmera
    return cap

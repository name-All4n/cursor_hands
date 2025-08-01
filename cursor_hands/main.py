import cv2
from camera import inicializar_camera
from mao import DetectorDeMaos
from cursor import ControladorCursor

#
wCam, hCam = 640, 480 
cap = inicializar_camera(wCam, hCam) 

detector = DetectorDeMaos()
cursor = ControladorCursor(suavizacao=5)

# Loop principal para capturar vídeo e detectar mãos
while True:
    success, img = cap.read() # Captura a imagem da câmera
    img = cv2.flip(img, 1) # Inverte horizontalmente a imagem
    if not success:
        break

    results = detector.detectar_maos(img) # Detecta as mãos na imagem

    # Se mãos forem detectadas, move o cursor com base na ponta do dedo indicador
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[8] # Ponto da ponta do dedo indicador
            cursor.mover_cursor(index_finger_tip.x, index_finger_tip.y) 
            detector.desenhar_maos(img, [hand_landmarks]) # Desenha as mãos detectadas na imagem

    
    if results.multi_hand_landmarks: # Itera sobre as mãos detectadas
        for hand_landmarks in results.multi_hand_landmarks: 
                dedo_indicador = hand_landmarks.landmark[8]
                dedo_polegar = hand_landmarks.landmark[4]

                # Move o cursor com o indicador
                cursor.mover_cursor(dedo_indicador.x, dedo_indicador.y)

                # Detecta o gesto de clique (pinça entre polegar e indicador)
                cursor.detectar_clique(
                    dedo_indicador.x, dedo_indicador.y,
                    dedo_polegar.x, dedo_polegar.y
                )

                detector.desenhar_maos(img, [hand_landmarks])

    cv2.imshow("Controle com a Mão", img) # Exibe a imagem com as mãos detectadas
    if cv2.waitKey(1) & 0xFF == ord('q'): # Pressiona 'q' para sair do loop
        break

cap.release() 
cv2.destroyAllWindows() 

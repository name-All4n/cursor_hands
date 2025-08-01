# 🖐️ Mouse Controlado por Gestos com a Mão (OpenCV + MediaPipe)

Este projeto utiliza **OpenCV**, **MediaPipe** e **PyAutoGUI** para controlar o cursor do mouse com gestos da mão captados pela webcam. Com o movimento do dedo indicador você move o cursor, e com o gesto de "pinça" entre o indicador e o polegar, você realiza cliques!

---

## 🎥 Demonstração

> Ao mover o dedo indicador, o cursor do mouse acompanha.  
> Ao aproximar o polegar do indicador, é feito um clique automático.

---

## 🧠 Como Funciona

- A câmera captura a imagem em tempo real
- O `MediaPipe Hands` detecta pontos da mão
- O ponto do **dedo indicador** controla a posição do mouse
- A distância entre o **polegar** e o **indicador** determina se haverá um **clique**

---

## 🗂️ Estrutura do Projeto

├── main.py # Código principal (loop e integração)
├── camera.py # Inicialização da câmera
├── cursor.py # Controle do cursor e clique com suavização
├── mao.py # Detecção da mão e desenho com MediaPipe

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- OpenCV
- MediaPipe (Google)
- PyAutoGUI
- Math

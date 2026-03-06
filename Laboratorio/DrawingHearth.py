import turtle  # Importamos la librería para gráficos vectoriales

# Vamos a Dibujar un corazon

# 1. Configuración inicial del "pincel" (turtle) y el lienzo (screen)
t = turtle.Turtle()  # Creamos el objeto 't', que es nuestra flecha/pincel
s = turtle.Screen()  # Creamos la ventana de dibujo

s.bgcolor("black")   # Definimos el color de fondo de la ventana a negro
t.color("red")       # Definimos el color de la línea a rojo
t.fillcolor("red")   # Definimos que el color de relleno sea rojo
t.speed(3)           # (Opcional) Ajusta la velocidad del dibujo

# 2. Inicio del dibujo
t.begin_fill()       # Le decimos a Python: "empieza a recordar el trayecto para rellenarlo"

# Dibujamos el lado izquierdo del corazón
t.left(50)           # Gira el pincel 50 grados a la izquierda
t.forward(133)       # Avanza 133 píxeles (crea la base recta izquierda)

# Dibujamos la curva superior izquierda
# circle(radio, extensión): Dibuja un arco de 45 de radio y 200 grados de giro
t.circle(50, 200)    

# Ajustamos la dirección para la siguiente curva
t.right(140)         # Gira a la derecha para apuntar hacia la otra curva

# Dibujamos la curva superior derecha
t.circle(50, 200)    

# Dibujamos el lado derecho (cerramos la punta de abajo)
t.forward(133)       # Avanza para completar el contorno

t.end_fill()         # "Cierra el área y rellénala de rojo"

# 3. Finalización
t.hideturtle()       # Esconde la flechita para que solo se vea el corazón
turtle.done()        # Mantiene la ventana abierta al terminar
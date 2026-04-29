import stepic 
from PIL import Image 


#Abrir imagen 
img= Image.open ("C:/Users/paola/OneDrive/Desktop/Fondo de Pantalla Septiembre Bohemio Beige.png")

#mensaje a ocultar
mensaje= "Este es un mensaje secreto"

#insertar imagen 
img_oculta=stepic.encode(img, mensaje.encode())
img_oculta.save("C:/Users/paola/OneDrive/Desktop/nueva_imagen.png")

print ("Mensaje oculto en la imagen oculta.png")



img_oculta= Image.open ("C:/Users/paola/OneDrive/Desktop/nueva_imagen.png")
mensaje_recuperado= stepic.decode(img_oculta)
print ("Mensaje recuperado:", mensaje_recuperado)




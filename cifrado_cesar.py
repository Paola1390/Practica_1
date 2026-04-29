def cifrado_cesar(texto, deszplazamiento):
    resultado= ""
    for char in texto.upper(): 
        if char.isalpha(): 
            resultado+= chr ((ord(char)-65+ deszplazamiento)% 26 +65)
        else :
            resultado += char 
    return resultado 
        
mensaje="SEGURIDAD"
cifrado= cifrado_cesar(mensaje, 3)
print ("cifrado:",cifrado)
print ("Descifrado:", cifrado_cesar (cifrado, -3))


# EXPLICACION CODIGO
#5: ord(char)    -convierte la letra a su codigo ASI 
#6: ord(char) -65     -convierten A= 0 B=1  
# + dezplazamiento    -aplica a las posiciones
# %26 significa modulo, residuo de una division los valores esten siempre en en rango de 25



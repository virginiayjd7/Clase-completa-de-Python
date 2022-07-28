#archivo=open('texto.txt','a')
#archivo.white('prueba de guardado en el archivo')
#archivo.close()

#archivo=open('texto.t#xt','r')
#print(archivo.read())#

def encriptar(texto):
    print('el texto a encriptar es:'+texto)
    textoFinal=''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal
def desencriptar(texto):
    print('El texto a desencriptar es:'+texto) 
    textoFinal =''
    
    for letra in texto:
            ascii = ord(letra)
            ascii -= 1
            textoFinal += chr(ascii)
    return textoFinal
    
#desencriptar('Pxrxuxexbxax xdxex xtxexxxtxox')

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo,'r')
    texto = archivo.read()
    archivo.close()

    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo,'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('el archivo se encripto correctamente')
#encriptarArchivo()

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo,'r')
    texto = archivo.read()
    archivo.close()

    textodeEncriptado = desencriptar(texto)

    archivo = open(rutaArchivo,'w')
    archivo.write(textodeEncriptado)
    archivo.close()
    print('el archivo se desencripto correctamente')
#esencriptarArchivo()
resultadoEoD = input('presione "E" para encriptar, o "D" para desencriptar: ')
rutaArchivo = input('ingrese la ruta del archivo: ')

if resultadoEoD =='E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)


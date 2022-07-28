# nombre=input('¿como llamas ?')
# print('hola'+nombre)
# edad  =int (input('¿cuantos años tienes?'))
# masdedoce= edad >= 12
# resphijodedueño= input('¿eres el hijo de dueño?')
# eshijodedueño = resphijodedueño =='si'
# puedepasar =masdedoce or eshijodedueño
# if puedepasar:
#      print('pasa a la montaña rusa')
# else:
##      print('no puede pasar')

#numero =int (input('¿ingrse numero?'))
#if numero % 2 == 0:
#   print('es par')
#else:
#   print('impar')
#calcular el indice de masa corporal

def calcularIMC(peso,alturaENMETROS):
    imc=peso /(alturaENMETROS* alturaENMETROS)
    return imc

def pedirELIMC():

    peso = float(input('ingrese el peso en kg:'))
    alturaenCENTI = int (input('ingrse su altura en cm:'))
    alturaENMETROS= alturaenCENTI / 100
    imc=calcularIMC(peso, alturaENMETROS)

    print('su IMC es de '+ str(imc))
    
    if imc < 20:
        print ('Estado de delgadez')
    if imc >= 20 and imc < 26:
        print('peso normal')
    if imc >= 26 and imc < 30:
        print('estado de sobrepeso')
    if imc >= 30:
        print('Estado de obecidad')
print("primera")
pedirELIMC()
#print("egunda")
#pedirELIMC()
#print("tercera")
#pedirELIMC()


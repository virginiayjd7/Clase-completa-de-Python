
from Empleado import Empleado
from Cliente import Cliente
from Persona import Persona
#emp= Empleado('yaneth','may','122333','97595746','2000')
#cli= Cliente('yaneth','may','122333','97595746','vip')
#print(emp.salario)
Personas = []
def cargar():
    respuesta = input('¿va a agregar un empleado? ')
    nombre = input('ingrese el nombre')
    apellido = input('ingrese el apellido')
    dni = input('ingrese el dni')
    telefono = input('ingrese el telefono')

    if(respuesta == 'si'):
        salario = input('ingrese el salario')
        emp = Empleado(nombre,apellido,dni,telefono, int(salario))
        Personas.append(emp)
    else:
        tipo = input('ingrese el tipo de cliente:')
        cli = Cliente(nombre,apellido,dni,telefono,tipo)
        Personas.append(cli)

cargar()
cargar()

for persona in Personas:
    print(persona)
    
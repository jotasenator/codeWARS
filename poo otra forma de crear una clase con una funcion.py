
#crear clase de otra manera

def creando_clase(*args):

	class Animal:

		def __init__(self,*brgs):

			self.__dict__ = {i:j for i,j in zip(args,brgs)}

	return Animal

Animal = creando_clase('nombre', 'hambre', 'cabeza')

perro = Animal('Juan','siempre','no tiene')

print(perro.nombre)
print(perro.hambre)
print(perro.cabeza)



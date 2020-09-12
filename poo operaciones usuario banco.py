
class Usuario:

	def __init__(self,name,amount):

		self.name=name
		self.amount=amount

	def __str__(self):

		return f'{self.name} tiene ${self.amount}'

	def deposito(self,cantidad):
		self.amount += cantidad

		return f'{self.name} ha depositado ${cantidad}'

	def retiro(self,cantidad):

		if self.amount>=cantidad:
			self.amount -= cantidad
			return f'{self.name} ha retirado ${cantidad}'
		else:
			return f'{self.name} no puede extraer ${cantidad},\nsolo tiene ${self.amount} ...'

	def donacion(self,other,cantidad):
		if self.amount >= cantidad:

			other.deposito(cantidad)
			self.retiro(cantidad)
			return f'{self.name} ha donado a {other.name} unos ${cantidad}'

		else:	return f'No hay fondos para que {self.name} extraiga ${cantidad},\nsolo tiene ${self.amount} ...'



persona1 = Usuario('Maykel',790)
persona2 = Usuario('Yausmara',20)

print(persona1.name,persona1.amount)
print(persona2.name,persona2.amount)
print(persona1.__str__())
print(persona2.__str__())
print(persona1.deposito(100))
print(persona2.deposito(1200))
print(persona1.__str__())
print(persona2.__str__())
print(persona1.retiro(15*25))
print(persona2.retiro(3000))
print(persona1.__str__())
print(persona2.__str__())
print(persona1.donacion(persona2,200)) 
print(persona2.donacion(persona1,500))
print(persona1.__str__())
print(persona2.__str__())
print(persona2.donacion(persona1,200))
print(persona1.__str__())
print(persona2.__str__())
print(persona2.donacion(persona1,200))
print(persona2.donacion(persona1,2200))
print(persona1.__str__())
print(persona2.__str__())
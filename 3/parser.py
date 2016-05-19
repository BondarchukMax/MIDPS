def resuelve(cadena):
	try:
		while '(' in cadena and ')' in cadena:
			contInicio = cadena.count('(')

			inicio = cadena.find('(')	
			fin = cadena.find(')')+1

			while contInicio > 1:
				inicio = cadena.find('(', inicio+1) 
				contInicio -= 1

			viejo = cadena[inicio:fin]
			nuevo = calcula(viejo.replace('(', '').replace(')', ''))
			cadena = cadena.replace(viejo, nuevo)

		resultado = float(calcula(cadena))
	except:
		resultado = "Error"

	return resultado

def calcula(cadena):
	elementos = cadena.split()

	while len(elementos) != 1:
		# Capa multiplicacion y divicion
		for index in range(len(elementos)):
			if elementos[index] == '*':
				elementos[index] = str(float(elementos[index-1]) * float(elementos[index+1]))

				elementos.pop(index+1)
				elementos.pop(index-1)
				break

			elif elementos[index] == '/':
				elementos[index] = str(float(elementos[index-1]) / float(elementos[index+1]))

				elementos.pop(index+1)
				elementos.pop(index-1)
				break

		# Capa suma y resta
		if not '/' in elementos and not '*' in elementos:
			while len(elementos) != 1:
				for index in range(len(elementos)):
					elementos[index] = str(float(elementos[index]) + float(elementos[index+1]))

					elementos.pop(index+1)
					break
				
	return elementos[0]

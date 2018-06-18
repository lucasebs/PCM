import matplotlib.pyplot as plt

def nrz(bits):	
	result = ''
	for bit in bits:
		result += bit
	return result

def nrz_m(bits):
	result = ''
	bit_vez = '0'
	for bit in bits:
		if bit == '1':
			if bit_vez == '1':
				result += '0'
				bit_vez = '0'
			elif bit_vez == '0':
				result += '1'
				bit_vez = '1'
		if bit == '0':
			result += bit_vez

	return result

def write(bits):
	signal = '+v '

	for bit in bits:
		if bit == '1':
			signal += '_'
		else:
			signal += ' '

	signal += '\n-v '

	for bit in bits:
		if bit == '0':
			signal += '_'
		else:
			signal += ' '
	print(signal)


def get_points(nrzm, bits):
	aux = []
	ant = 0

	for bit in nrzm:
		for i in range(0,55):
			aux.append(int(bit))		

	plt.plot(range(len(aux)), aux, linestyle='-', color='r', linewidth=2.0)
	plt.axis([-1,len(aux),-1,2])
	plt.suptitle("nrzM - " + bits, fontsize=16)
	plt.title("Result - " + nrzm)
	plt.show()


def main():
	print("\nnrz-M\n")
	while True:
		bits = input("Informe 16 Bits: ")
		if len(bits) == 16:
			break
		else:
			print("\nPor favor, informe 16 bits!!!\n +\n + Qtd de bits informados: " + 
				str(len(bits)) + "\n +\n" )


	
	print('\nnrz')
	print(nrz(bits))
	write(nrz(bits))
	print('\nnrz-M')
	print(nrz_m(bits)) 
	write(nrz_m(bits))

	get_points(nrz_m(bits), bits)


if __name__ == "__main__":
    main()

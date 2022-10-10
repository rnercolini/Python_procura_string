# Procura uma string dentro de outra e retorna False ou True
nome = str(input('Digite um nome completo: ')).strip().upper()
print('O seu nome tem Silva? {}'.format('SILVA' in nome))

import funções_forca
print('#'*30)
print('#        JOGO DA FORCA.      #'.center(30))
print('#'*30)
print()
while True:
	r1=funções_forca.tipo('Sua opção: ')
	o=funções_forca.animal(r1)
	if o=='N':
		break
print('\033[32mFIM DE JOGO.\033[m')

cores={'VERMELHO':'\033[31m',
'AZUL':'\033[34m','AMARELO':'\033[33m','VERDE':'\033[32m','LILAS':'\033[36m'}

animais=('VACA','GATO','COBRA','GOLFINHO','PATO','CARANGUEIJO','TUCANO','ELEFANTE','HIPOPOTAMO','LAGARTO','POMBO','GIRAFA','ABELHA','VESPA','PAPAGAIO','FORMIGA','VAGALUME','MACACO','CACHORRO','ARANHA')

alimentos=('FEIJOADA','BOLO','PAMONHA','CUSCUZ','ARROZ','PIZZA','PASTEL','COXINHA','SORVETE','BISCOITO','LARANJA','MORANGO','CARANBOLA','ACELORA','BANANA','TOMATE','GOIABA','CHOCOLATE','ERVILHA','BAICON','PUDIM')


import random


def linha(txt):
	print('-'*22)
	print(f'{cores["AZUL"]}{txt}\033[m'.center(22))
	print('-'*22)
	

def opção(n):
	linha('MODO DE JOGO')
	print(f'''{cores['AMARELO']}1- Sozinho
2- Acompanhado\033[m''')
	print('-'*22)
	while True:
		try:
			opção=int(input(f'{n}'))
			if opção==1 or opção==2:
				return opção
			else:
				print('\033[31mDigite 1 ou 2\033[m')
		except:
			print('\033[31mErro: digite um número inteiro entre [1 e 2] \033[m')
			
			
			
def tipo(o):
	linha('GÊNERO')
	print(f'''{cores['AMARELO']}1- Animais
2- Alimentos\033[m''')
	print('-'*22)
	while True:
		try:
			opção=int(input(f'{o}'))
			if opção==1 or opção==2:
				return opção
			else:
				print('\033[31mDigite 1 ou 2\033[m')
		except:
			print('\033[31mErro: digite um número inteiro entre [1 e 2] \033[m')
	

def animal(a):
	lista=[]
	if a==1:
		s=random.choice(animais)
		for c in range(0,len(s)):
			lista.append(s[c])
	else:
		s=random.choice(alimentos)
		for c in range(0,len(s)):
			lista.append(s[c])
	cont=len(lista)
	c=0
	y=[]
	k=[]
	for cv in range(0,len(lista)):
		k.append('_')
	print('''
 	  	+ ---+
 	  	|    |
   		|    
  	 	|    
 	  	|''')
	for d in range(0,len(k)):
		if d==0:
			print(f'			{k[d]}',end=' ')
		else:
			print(f'{k[d]}',end=' ')
	print()
	while True:
		try:
			letra=input('\nDigite uma letra: ').strip().upper()[0]
			while letra.isnumeric()==True:
				print('\033[31mPor favor digite uma letra válida\033[m')
				letra=input('\nDigite uma letra: ').strip().upper()[0]
		except:
			print('\033[31mErro: Digite uma letra\033[m')
		else:
			y.append(letra)
			print()
			print('  \033[33mPALAVRAS FALADAS.\033[m')
			for faladas in y:
				print(f'  {faladas}',end='')
			for v in range(0,len(lista)):
				if letra in lista[v]:
					k[v]=letra
			if letra not in lista:
				c+=1
			if c==0:
				print('''
 	  	+ ---+
 	  	|    |
   		|    
  	 	|    
 	  	|''')
			if c==1:
				print('''
  		+ ---+
		|    |
		|    0
		|    
		|''') 
			elif c==2:
				print('''
              	+ ---+
	  	|    |
	  	|    0
	  	|    |
	  	|''')
			elif c==3:
				print('''
              	+ ---+
	  	|    |
	  	|    0
	  	|    |
	  	|   / \	''')
			if c!=4:
				for d in range(0,len(k)):
					if d==0:
						print(f'			{k[d]}',end=' ')
					else:
						print(f'{k[d]}',end=' ')
				print()
		if '_' not in k:
			print()
			print()
			print('\033[32mParabéns! Você, venceu.\033[m')
			c=4
		if c==4 and '_' in k:
				print(f'''
       	 	+ ---+
  	        |    |
	  	|    0        \033[31mVocê Perdeu!\033[m
	  	|  --|--
	  	|   / \	''')
				print()
				print(f'\033[35mA palavra era\033[m\033[36m"{s}"\033[m ')
				print()
		if c==4:
			while True:
				print()
				try:
					continuar=str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
					if continuar=='S' or continuar=='N':
						return continuar
					else:
						print('\033[31mOpção inválida\033[m')
				except:
					print('\033[31mERRO: Digite [S/N] \033[m')
					

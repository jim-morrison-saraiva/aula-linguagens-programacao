nome = input("Digite seu nome: ")
posicao = int(input("Digite a posição que deseja adicionar a letra: "))
print(nome[i])

if nome[posicao] == "s" or "S":
    print(nome[:posicao]+"r"+nome[posicao+1:])
elif nome[posicao] == "m" or "M": 
    print(nome[:posicao]+"n"+nome[posicao+1:])
else:
    print(nome[:posicao]+nome[posicao+1:])
    
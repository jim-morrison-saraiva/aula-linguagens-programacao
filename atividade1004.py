notas = []
soma = 0
i = int(input("digite sua nota: "))
while i != -1:
    notas.append(i)
    i = input("digite sua nota: ")
   
soma = sum(notas)
media = soma / len(notas)
print ("\n\n")
print ("sua média é: ",media)
if media < 7:
    print ("você foi reprovado")
else:
    print ("você foi aprovado")
print ("\n")

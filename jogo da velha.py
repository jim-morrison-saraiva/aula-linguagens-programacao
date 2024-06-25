import os
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
def tela():
    global tabuleiro
    os.system("cls")
    print (tabuleiro[0][0] + '|' + tabuleiro[0][1] + '|' + tabuleiro[0][2])
    print ('-----')
    print (tabuleiro[1][0] + '|' + tabuleiro[1][1] + '|' + tabuleiro[1][2])
    print ('-----')
    print (tabuleiro[2][0] + '|' + tabuleiro[2][1] + '|' + tabuleiro[2][2])

print (tela())

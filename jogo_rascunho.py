def criar_tabuleiro():
  """
  Cria e retorna um tabuleiro vazio (3x3) para o jogo da velha.
  """
  tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
  ]
  return tabuleiro

def exibir_tabuleiro(tabuleiro):
  """
  Exibe o tabuleiro do jogo da velha na tela.
  """
  for linha in tabuleiro:
    print("| " + " | ".join(linha) + " |")

def marcar_jogada(tabuleiro, jogador, linha, coluna):
  """
  Marca a jogada do jogador especificado no tabuleiro.
  """
  if not is_posicao_valida(tabuleiro, linha, coluna):
    return False
  
  tabuleiro[linha][coluna] = jogador
  return True

def is_posicao_valida(tabuleiro, linha, coluna):
  """
  Verifica se a posição informada é válida no tabuleiro.
  """
  if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
    return True
  else:
    return False

def verificar_vitoria(tabuleiro, jogador):
  """
  Verifica se o jogador especificado venceu a partida.
  """
  # Verificar linhas e colunas
  for i in range(3):
    if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
      return True
    if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
      return True
  
  # Verificar diagonais
  if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
    return True
  if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
    return True
  
  return False

def verificar_empate(tabuleiro):
  """
  Verifica se a partida resultou em empate.
  """
  for linha in tabuleiro:
    for celula in linha:
      if celula == ' ':
        return False
  return True

def iniciar_jogo():
  """
  Função principal para iniciar e controlar o jogo da velha.
  """
  tabuleiro = criar_tabuleiro()
  jogador_atual = 'X'

  while True:
    exibir_tabuleiro(tabuleiro)

    # Obter jogada do jogador atual
    linha = int(input(f"Jogador {jogador_atual}, digite a linha (0, 1 ou 2): "))
    coluna = int(input(f"Jogador {jogador_atual}, digite a coluna (0, 1 ou 2): "))

    # Validar e marcar jogada
    if not marcar_jogada(tabuleiro, jogador_atual, linha, coluna):
      print("Jogada inválida! Tente novamente.")
      continue

    # Verificar vitória e empate
    if verificar_vitoria(tabuleiro, jogador_atual):
      exibir_tabuleiro(tabuleiro)
      print(f"Parabéns, Jogador {jogador_atual}! Você venceu!")
      break
    elif verificar_empate(tabuleiro):
      exibir_tabuleiro(tabuleiro)
      print("Empate!")
      break

    # Alternar jogador
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if _name_ == "_main_":
  iniciar_jogo()
MOV_CAVALO = [(-2, -1), (-1, -2), (1, -2), (2, -1),
              (2, 1), (1, 2), (-1, 2), (-2, 1)]

def gerar_tabuleiro(n, posicoes_rainhas):
    """vai desenhar uma matriz com as rainhas posicionadas."""
    tabuleiro = [['.' for _ in range(n)] for _ in range(n)]
    for linha in range(n):
        col = posicoes_rainhas[linha]
        tabuleiro[linha][col] = 'R'  
    return tabuleiro

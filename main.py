import sys


MOV_CAVALO = [(-2, -1), (-1, -2), (1, -2), (2, -1),
              (2, 1), (1, 2), (-1, 2), (-2, 1)]

def eh_seguro(tabuleiro, linha, coluna, n):
    """verifica se é seguro posicionar uma rainha na posição (linha, coluna)."""
    for i in range(linha):
        if tabuleiro[i] == coluna or \
           tabuleiro[i] - i == coluna - linha or \
           tabuleiro[i] + i == coluna + linha:
            return False
    return True

def resolver_n_rainhas(tabuleiro, linha, n):
    """usa backtracking para resolver o problema das N-Rainhas."""
    if linha == n:
        return True
    for coluna in range(n):
        if eh_seguro(tabuleiro, linha, coluna, n):
            tabuleiro[linha] = coluna
            if resolver_n_rainhas(tabuleiro, linha + 1, n):
                return True
    return False

def gerar_tabuleiro(n, posicoes_rainhas):
    """vai desenhar uma matriz com as rainhas posicionadas."""
    tabuleiro = [['.' for _ in range(n)] for _ in range(n)]
    for linha in range(n):
        col = posicoes_rainhas[linha]
        tabuleiro[linha][col] = 'R'  
    return tabuleiro

def posicao_valida(tabuleiro, x, y):
    """analsia se uma posição está dentro dos limites e não tem rainha."""
    n = len(tabuleiro)
    return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == '.'

def passeio_do_cavalo(tabuleiro, x, y, visitado, total_livres, contador):
    """utiliza backtracking para verificar se o cavalo pode visitar todas as casas livres."""
    n = len(tabuleiro)
    if contador == total_livres:
        return True
    
    for dx, dy in MOV_CAVALO:
        nx, ny = x + dx, y + dy
        if posicao_valida(tabuleiro, nx, ny) and not visitado[nx][ny]:
            visitado[nx][ny] = True
            if passeio_do_cavalo(tabuleiro, nx, ny, visitado, total_livres, contador + 1):
                return True
            visitado[nx][ny] = False
    return False

def encontrar_inicio(tabuleiro):
    """procura a primeira posição livre (sem rainha) para iniciar o passeio."""
    n = len(tabuleiro)
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] == '.':
                return i, j
    return None

def contar_livres(tabuleiro):
    """conta quantas casas estão livres (sem rainha)."""
    return sum(row.count('.') for row in tabuleiro)

def principal(n):
    posicoes_rainhas = [-1] * n
    if not resolver_n_rainhas(posicoes_rainhas, 0, n):
        print("Não foi possível encontrar uma solução para as N-Rainhas.")
        return

    tabuleiro = gerar_tabuleiro(n, posicoes_rainhas)
    print("Tabuleiro com as rainhas posicionadas:")
    for linha in tabuleiro:
        print(" ".join(linha))

    total_livres = contar_livres(tabuleiro)
    inicio = encontrar_inicio(tabuleiro)
    if not inicio:
        print("Não há posição inicial válida para o cavalo.")
        return

    visitado = [[False for _ in range(n)] for _ in range(n)]
    x0, y0 = inicio
    visitado[x0][y0] = True

    print(f"\nIniciando passeio do cavalo a partir de ({x0}, {y0})")
    if passeio_do_cavalo(tabuleiro, x0, y0, visitado, total_livres, 1):
        print("O cavalo conseguiu visitar todas as casas livres sem interferir com as rainhas.")
    else:
        print("O cavalo NÃO conseguiu visitar todas as casas livres.")

if __name__ == "__main__":
    N = int(input("Digite o valor de N (tamanho do tabuleiro): "))
    if N < 1 or N > 10:
        print("Escolha um valor de N entre 1 e 10 para evitar alta complexidade.")
        sys.exit()
    principal(N)

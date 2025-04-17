# 🧠 N-Rainhas + Passeio do Cavalo 🐴♛

Este projeto combina dois clássicos problemas de backtracking: o **Problema das N-Rainhas** e o **Problema do Passeio do Cavalo** em um tabuleiro de xadrez.

---

## 📌 Enunciado da Atividade

Desenvolver um programa que:

1. Posicione `N` rainhas em um tabuleiro `N×N` de forma que **nenhuma ataque a outra**.
2. Após isso, posicione um **cavalo** em uma posição **não ocupada por rainha** e verifique se ele é capaz de visitar **todas as casas livres do tabuleiro**, utilizando apenas movimentos válidos do cavalo, **sem passar por casas com rainhas**.

---

## ⚙️ Como funciona

### ✔ Parte 1 – N-Rainhas
- O algoritmo usa **backtracking** para encontrar uma configuração válida de N rainhas que não se ataquem entre si.
- É garantido que, se houver solução para o N fornecido, ela será exibida.

### ✔ Parte 2 – Passeio do Cavalo
- O cavalo começa em uma posição **livre** do tabuleiro.
- Um segundo algoritmo de backtracking verifica se é possível visitar **todas as casas vazias** com os movimentos válidos do cavalo, **sem interferir com as rainhas**.

## ⚠️ Limitações conhecidas

- **N = 2** e **N = 3** não possuem solução para o problema das N-Rainhas. O programa detecta e informa isso.
- Para evitar complexidade excessiva, o programa recomenda usar valores de `N >= 4` e `N <= 10`.

---

## ▶️ Como Executar

### Requisitos
- Python 3 instalado

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/gabruurr/algoritmoRainha
   cd algoritmoRainha
   ```

2. Execute
   ```bash
   python main.py
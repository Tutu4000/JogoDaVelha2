import copy
from tkinter import *
from tkinter import messagebox
import tkinter

class Jogo:
    def __init__(self, matriz, peca=None, numPecas=0, modLinha=None, modColuna=None):
        self.matriz = matriz
        self.peca = peca
        self.numPecas = numPecas
        self.modLinha = modLinha
        self.modColuna = modColuna

    def addPeca(self, l, c, valor):
        self.matriz[l][c] = valor
        self.numPecas += 1
        self.modLinha = l
        self.modColuna = c
        self.peca = self.definirPeca()
    def retornaPeca(self, l, c):
        return self.matriz[l][c]

    def jogadorVenceu(self):
        for i in range(len(self.matriz)):
            if sum(self.matriz[i]) == 3:  # verifica as linhas do tabuleiro
                return True
            # verificando as colunas
            coluna = []
            for j in range(len(self.matriz)):
                coluna += [self.matriz[j][i]]
                if sum(coluna) == 3:
                    return True

            # verificando as diagonais
        diagonalprincipal = [self.matriz[0][0], self.matriz[1][1], self.matriz[2][2]]
        diagonalsecundaria = [self.matriz[0][2], self.matriz[1][1], self.matriz[2][0]]
        if sum(diagonalsecundaria) == 3 or sum(diagonalprincipal) == 3:
            return True
        return False

    def maquinaVenceu(self):
        for i in range(len(self.matriz)):
            if sum(self.matriz[i]) == -3:  # verifica as linhas do tabuleiro
                return True
            # verificando as colunas
            coluna = []
            for j in range(len(self.matriz)):
                coluna += [self.matriz[j][i]]
                if sum(coluna) == -3:
                    return True

            # verificando as diagonais
        diagonalprincipal = [self.matriz[0][0], self.matriz[1][1], self.matriz[2][2]]
        diagonalsecundaria = [self.matriz[0][2], self.matriz[1][1], self.matriz[2][0]]
        if sum(diagonalsecundaria) == -3 or sum(diagonalprincipal) == -3:
            return True
        return False

    def jogoCheio(self):
        if self.matriz[0][0] != 0 and self.matriz[0][1] != 0 and self.matriz[0][2] != 0 and self.matriz[1][0] != 0 and self.matriz[1][1] != 0 and self.matriz[1][2] != 0 and self.matriz[2][0] != 0 and self.matriz[2][1] != 0 and self.matriz[2][2] != 0:
            return True
        else:
            return False

    def definirPeca(self):
        if self.jogadorVenceu():
            return "X"
        elif self.maquinaVenceu():
            return "O"
        elif self.jogoCheio():
            return "Y"
        else:
            return None

    def chancesJogador(self):
        i = 0
        for l in range(3):
            if self.matriz[l][0] != -1 and self.matriz[l][1] != -1 and self.matriz[l][2] != -1:
                i += 1
        for c in range(3):
            if self.matriz[0][c] != -1 and self.matriz[1][c] != -1 and self.matriz[2][c] != -1:
                i += 1
        if self.matriz[0][0] != -1 and self.matriz[1][1] != -1 and self.matriz[2][2] != -1:
            i += 1
        if self.matriz[0][2] != -1 and self.matriz[1][1] != -1 and self.matriz[2][0] != -1:
            i += 1
        return i

    def chancesMaquina(self):
        i = 0
        for l in range(3):
            if self.matriz[l][0] != 1 and self.matriz[l][1] != 1 and self.matriz[l][2] != 1:
                i += 1
        for c in range(3):
            if self.matriz[0][c] != 1 and self.matriz[1][c] != 1 and self.matriz[2][c] != 1:
                i += 1
        if self.matriz[0][0] != 1 and self.matriz[1][1] != 1 and self.matriz[2][2] != 1:
            i += 1
        if self.matriz[0][2] != 1 and self.matriz[1][1] != 1 and self.matriz[2][0] != 1:
            i += 1
        return i

    def heuristica(self):
        if self.maquinaVenceu():
            return 100000
        elif self.jogadorVenceu():
            return -100000
        else:
            return self.chancesMaquina() - self.chancesJogador()

    def printJogo(self):
        for linha in self.matriz:
            print(linha)


class No:
    def __init__(self, valor, pai=None, peso=None):
        self.valor = valor
        self.filhos = []
        self.pai = pai
        self.peso = peso

    def adicionarFilho(self, filho):
        filho.pai = self
        self.filhos.append(filho)

def empate(jogo):
    for l in range(3):
        if jogo[l][0].peca == "Y" and jogo[l][1].peca == "Y" and jogo[l][2].peca == "Y":
            return True
    for c in range(3):
        if jogo[0][c].peca == "Y" and jogo[1][c].peca == "Y" and jogo[2][c].peca == "Y":
            return True
    if jogo[0][0].peca == "Y" and jogo[1][1].peca == "Y" and jogo[2][2].peca == "Y":
        return True
    if jogo[0][2].peca == "Y" and jogo[1][1].peca == "Y" and jogo[2][0].peca == "Y":
        return True
    return False
def jogadorVenceuJogo(jogo):
    for l in range(3):
        if (jogo[l][0].peca == "X" or jogo[l][0].peca == "Y") and (
                jogo[l][1].peca == "X" or jogo[l][1].peca == "Y") and (
                jogo[l][2].peca == "X" or jogo[l][2].peca == "Y"):
            return True
    for c in range(3):
        if (jogo[0][c].peca == "X" or jogo[0][c].peca == "Y") and (
                jogo[1][c].peca == "X" or jogo[1][c].peca == "Y") and (
                jogo[2][c].peca == "X" or jogo[2][c].peca == "Y"):
            return True
    if (jogo[0][0].peca == "X" or jogo[0][0].peca == "Y") and (
            jogo[1][1].peca == "X" or jogo[1][1].peca == "Y") and (
            jogo[2][2].peca == "X" or jogo[2][2].peca == "Y"):
        return True
    if (jogo[0][2].peca == "X" or jogo[0][2].peca == "Y") and (
            jogo[1][1].peca == "X" or jogo[1][1].peca == "Y") and (
            jogo[2][0].peca == "X" or jogo[2][0].peca == "Y"):
        return True
    return False
def maquinaVenceuJogo(jogo):
    for l in range(3):
        if (jogo[l][0].peca == "O" or jogo[l][0].peca == "Y") and (
                jogo[l][1].peca == "O" or jogo[l][1].peca == "Y") and (
                jogo[l][2].peca == "O" or jogo[l][2].peca == "Y"):
            return True
    for c in range(3):
        if (jogo[0][c].peca == "O" or jogo[0][c].peca == "Y") and (
                jogo[1][c].peca == "O" or jogo[1][c].peca == "Y") and (
                jogo[2][c].peca == "O" or jogo[2][c].peca == "Y"):
            return True
    if (jogo[0][0].peca == "O" or jogo[0][0].peca == "Y") and (
            jogo[1][1].peca == "O" or jogo[1][1].peca == "Y") and (
            jogo[2][2].peca == "O" or jogo[2][2].peca == "Y"):
        return True
    if (jogo[0][2].peca == "O" or jogo[0][2].peca == "Y") and (
            jogo[1][1].peca == "O" or jogo[1][1].peca == "Y") and (
            jogo[2][0].peca == "O" or jogo[2][0].peca == "Y"):
        return True
    return False

def jogoTotalmenteCheio(jogo):
    for l in range(3):
        for c in range(3):
            if not jogo[l][c].jogoCheio():
                return False
    return True

def fimDeJogo(jogo):
    if maquinaVenceuJogo(jogo) or jogadorVenceuJogo(jogo) or jogoTotalmenteCheio(jogo):
        return True
    else:
        return False

def acharJogo(jogo):
    pecas = 10
    linha, coluna = None, None
    for i in range(3):
        for j in range(3):
            if jogo.valor[i][j].peca is None and jogo.valor[i][j].numPecas < pecas:
                linha = i
                coluna = j
    return linha, coluna

def acharJogo2(jogo):
    pecas = 10
    linha, coluna = None, None
    for i in range(3):
        for j in range(3):
            if jogo[i][j].peca is None:
                if jogo[i][j].numPecas < pecas:
                    linha = i
                    coluna = j
    return linha, coluna

def chancesMaquina(jogo):
    i = 0
    for l in range(3):
        if jogo[l][0].peca != "X" and jogo[l][1].peca != "X" and jogo[l][2].peca != "X":
            i += 1
    for c in range(3):
        if jogo[0][c].peca != "X" and jogo[1][c].peca != "X" and jogo[2][c].peca != "X":
            i += 1
    if jogo[0][0].peca != "X" and jogo[1][1].peca != "X" and jogo[2][2].peca != "X":
        i += 1
    if jogo[0][2].peca != "X" and jogo[1][1].peca != "X" and jogo[2][0].peca != "X":
        i += 1
    return i


def chancesJogador(jogo):
    i = 0
    for l in range(3):
        if jogo[l][0].peca != "O" and jogo[l][1].peca != "O" and jogo[l][2].peca != "O":
            i += 1
    for c in range(3):
        if jogo[0][c].peca != "O" and jogo[1][c].peca != "O" and jogo[2][c].peca != "O":
            i += 1
    if jogo[0][0].peca != "O" and jogo[1][1].peca != "O" and jogo[2][2].peca != "O":
        i += 1
    if jogo[0][2].peca != "O" and jogo[1][1].peca != "O" and jogo[2][0].peca != "O":
        i += 1
    return i

def heuristica(jogo):
    if maquinaVenceuJogo(jogo):
        return 100000
    elif jogadorVenceuJogo(jogo):
        return -100000
    else:
        return chancesMaquina(jogo) - chancesJogador(jogo)
def MinMax(raiz, nivel, cont, l, c):
    if (nivel-cont) % 2 == 0:
        max = True
    else:
        max = False

    if raiz.valor[l][c].peca is not None:
        linha, coluna = acharJogo(raiz)
        l = linha
        c = coluna

    for i in range(3):
        for j in range(3):
            if raiz.valor[l][c].matriz[i][j] == 0:
                jogoG = copy.deepcopy(raiz.valor)
                jogo = copy.deepcopy(raiz.valor[l][c])
                if max:
                    ## jogo.valor[l][c].matriz[i][j] = -1
                    jogo.addPeca(i, j, -1)
                else:
                    ##jogo.valor[l][c].matriz[i][j] = 1
                    jogo.addPeca(i, j, 1)
                jogoG[l][c] = jogo
                filho = No(jogoG)
                raiz.adicionarFilho(filho)
                if cont-1 > 0 and not fimDeJogo(jogoG): ##and jogo.peca is None
                    MinMax(filho, nivel, cont - 1, i, j)
                    # if filho.valor[i][j].peca is None:
                    #     MinMax(filho, nivel, cont-1, i, j)
                    # else:
                    #     linha, coluna = acharJogo(filho)
                    #     MinMax(filho, nivel, cont-1, linha, coluna)
                else:
                    filho.peso = 2*heuristica(filho.valor) + filho.valor[i][j].heuristica()
    if max:
        raiz.peso = -500000
        for filho in raiz.filhos:
            if filho.peso > raiz.peso:
                raiz.peso = filho.peso
    else:
        raiz.peso = 500000
        for filho in raiz.filhos:
            if filho.peso < raiz.peso:
                raiz.peso = filho.peso


def maquinaJogaPadrao(raiz, nivel, l, c):
    MinMax(raiz, nivel, nivel, l, c)

    for filho in raiz.filhos:
        if filho.peso == raiz.peso:
            return filho.valor, filho.valor[l][c].modLinha, filho.valor[l][c].modColuna

def printJogoAtual(jogoAtual):
    for linha in jogoAtual:
        print(linha[0].matriz[0], "     |     ", linha[1].matriz[0], "     |     ", linha[2].matriz[0])
        print(linha[0].matriz[1], "     |     ", linha[1].matriz[1], "     |     ", linha[2].matriz[1])
        print(linha[0].matriz[2], "     |     ", linha[1].matriz[2], "     |     ", linha[2].matriz[2])
        print(linha[0].peca, linha[1].peca, linha[2].peca)
        print("------------------------------------------------------------------------------")


nivel = int(input("Qual é o nível de profundidade desejado para o MinMax? "))


print("\nInicio do Jogo \n")

matriz1 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz2 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz3 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz4 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz5 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz6 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz7 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz8 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

matriz9 = [[0,0,0],
           [0,0,0],
           [0,0,0]]

jogo1 = Jogo(matriz1)
jogo2 = Jogo(matriz2)
jogo3 = Jogo(matriz3)
jogo4 = Jogo(matriz4)
jogo5 = Jogo(matriz5)
jogo6 = Jogo(matriz6)
jogo7 = Jogo(matriz7)
jogo8 = Jogo(matriz8)
jogo9 = Jogo(matriz9)

jogoAtual = [[jogo1, jogo2, jogo3],
             [jogo4, jogo5, jogo6],
             [jogo7, jogo8, jogo9]]
jogol, jogoc = None, None
root = Tk()
root.title("Jogo da Velha")
raiz = No(jogoAtual)

#função para detectar que se jogol e jogoc atual for um jogo ja ganho por alguem, o jogol e jogoc viram linha e coluna do jogo com mais peças
def verificarJogoAtualLC():
    global jogol, jogoc
    if jogol is None or jogoc is None:
        return
    elif jogoAtual[jogol][jogoc].peca is not None:
        jogol, jogoc = acharJogo2(jogoAtual)



def atualizarBotao1(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[0][0].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i, column=j)

def atualizarBotao2(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[0][1].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i, column=j+3)
def atualizarBotao3(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[0][2].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i, column=j+6)
def atualizarBotao4(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[1][0].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i+3, column=j)
def atualizarBotao5(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[1][1].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i+3, column=j+3)
def atualizarBotao6(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[1][2].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i+3, column=j+6)
def atualizarBotao7(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[2][0].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i+6, column=j)
def atualizarBotao8(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[2][1].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i+6, column=j+3)
def atualizarBotao9(jogoAtual):
    for i in range(3):
        for j in range(3):
            if jogoAtual[2][2].retornaPeca(i, j) == -1:
                b = Button(root, text="O", width=10, height=5, bg="SystemButtonFace")
                b.grid(row=i+6, column=j+6)

def atualizarTodosBotoes(jogoAtual):
    atualizarBotao1(jogoAtual)
    atualizarBotao2(jogoAtual)
    atualizarBotao3(jogoAtual)
    atualizarBotao4(jogoAtual)
    atualizarBotao5(jogoAtual)
    atualizarBotao6(jogoAtual)
    atualizarBotao7(jogoAtual)
    atualizarBotao8(jogoAtual)
    atualizarBotao9(jogoAtual)

def apertarBotaoPrimeiroJogo(b):
    global jogoAtual, jogol, jogoc, raiz

    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 0 or jogoc != 0:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return


    if b["text"] == "":
        b["text"] = "X"
    if b == b11:
        jogoAtual[0][0].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b12:
        jogoAtual[0][0].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b13:
        jogoAtual[0][0].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b14:
        jogoAtual[0][0].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b15:
        jogoAtual[0][0].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b16:
        jogoAtual[0][0].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b17:
        jogoAtual[0][0].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b18:
        jogoAtual[0][0].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)

    elif b == b19:
        jogoAtual[0][0].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)


b11 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b11))
b12 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b12))
b13 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b13))
b14 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b14))
b15 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b15))
b16 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b16))
b17 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b17))
b18 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b18))
b19 = Button(root, text = jogoAtual[0][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoPrimeiroJogo(b19))

b11.grid(row = 0, column = 0)
b12.grid(row = 0, column = 1)
b13.grid(row = 0, column = 2)
b14.grid(row = 1, column = 0)
b15.grid(row = 1, column = 1)
b16.grid(row = 1, column = 2)
b17.grid(row = 2, column = 0)
b18.grid(row = 2, column = 1)
b19.grid(row = 2, column = 2)

def apertarBotaoSegundoJogo(b):
    global jogoAtual, jogol, jogoc, raiz
    verificarJogoAtualLC()

    if jogol is not None and jogoc is not None:
        if jogol != 0 or jogoc != 1:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return


    if b["text"] == "":
        b["text"] = "X"
    if b == b21:
        jogoAtual[0][1].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b22:
        jogoAtual[0][1].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b23:
        jogoAtual[0][1].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b24:
        jogoAtual[0][1].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b25:
        jogoAtual[0][1].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b26:
        jogoAtual[0][1].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b27:
        jogoAtual[0][1].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b28:
        jogoAtual[0][1].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)

    elif b == b29:
        jogoAtual[0][1].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)

b21 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b21))
b22 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b22))
b23 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b23))
b24 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b24))
b25 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b25))
b26 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b26))
b27 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b27))
b28 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b28))
b29 = Button(root, text = jogoAtual[0][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSegundoJogo(b29))

b21.grid(row = 0, column = 3)
b22.grid(row = 0, column = 4)
b23.grid(row = 0, column = 5)
b24.grid(row = 1, column = 3)
b25.grid(row = 1, column = 4)
b26.grid(row = 1, column = 5)
b27.grid(row = 2, column = 3)
b28.grid(row = 2, column = 4)
b29.grid(row = 2, column = 5)

def apertarBotaoTerceiroJogo(b):
    global jogoAtual, jogol, jogoc, raiz

    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 0 or jogoc != 2:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return

    if b["text"] == "":
        b["text"] = "X"
    if b == b31:
        jogoAtual[0][2].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b32:
        jogoAtual[0][2].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b33:
        jogoAtual[0][2].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b34:
        jogoAtual[0][2].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b35:
        jogoAtual[0][2].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b36:
        jogoAtual[0][2].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b37:
        jogoAtual[0][2].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b38:
        jogoAtual[0][2].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)

    elif b == b39:
        jogoAtual[0][2].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)

b31 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b31))
b32 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b32))
b33 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b33))
b34 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b34))
b35 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b35))
b36 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b36))
b37 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b37))
b38 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b38))
b39 = Button(root, text = jogoAtual[0][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoTerceiroJogo(b39))

b31.grid(row = 0, column = 6)
b32.grid(row = 0, column = 7)
b33.grid(row = 0, column = 8)
b34.grid(row = 1, column = 6)
b35.grid(row = 1, column = 7)
b36.grid(row = 1, column = 8)
b37.grid(row = 2, column = 6)
b38.grid(row = 2, column = 7)
b39.grid(row = 2, column = 8)


def apertarBotaoQuartoJogo(b):
    global jogoAtual, jogol, jogoc, raiz
    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 1 or jogoc != 0:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return

    if b["text"] == "":
        b["text"] = "X"
    if b == b41:
        jogoAtual[1][0].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)


    elif b == b42:
        jogoAtual[1][0].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b43:
        jogoAtual[1][0].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b44:
        jogoAtual[1][0].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b45:
        jogoAtual[1][0].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b46:
        jogoAtual[1][0].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b47:
        jogoAtual[1][0].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b48:
        jogoAtual[1][0].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)

    elif b == b49:
        jogoAtual[1][0].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)

b41 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b41))
b42 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b42))
b43 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b43))
b44 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b44))
b45 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b45))
b46 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b46))
b47 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b47))
b48 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b48))
b49 = Button(root, text = jogoAtual[1][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuartoJogo(b49))

b41.grid(row = 3, column = 0)
b42.grid(row = 3, column = 1)
b43.grid(row = 3, column = 2)
b44.grid(row = 4, column = 0)
b45.grid(row = 4, column = 1)
b46.grid(row = 4, column = 2)
b47.grid(row = 5, column = 0)
b48.grid(row = 5, column = 1)
b49.grid(row = 5, column = 2)


def apertarBotaoQuintoJogo(b):
    global jogoAtual, jogol, jogoc, raiz
    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 1 or jogoc != 1:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return

    if b["text"] == "":
        b["text"] = "X"
    if b == b51:
        jogoAtual[1][1].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b52:
        jogoAtual[1][1].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b53:
        jogoAtual[1][1].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b54:
        jogoAtual[1][1].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b55:
        jogoAtual[1][1].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b56:
        jogoAtual[1][1].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b57:
        jogoAtual[1][1].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b58:
        jogoAtual[1][1].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)

    elif b == b59:
        jogoAtual[1][1].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)


b51 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b51))
b52 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b52))
b53 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b53))
b54 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b54))
b55 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b55))
b56 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b56))
b57 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b57))
b58 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b58))
b59 = Button(root, text = jogoAtual[1][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoQuintoJogo(b59))

b51.grid(row = 3, column = 3)
b52.grid(row = 3, column = 4)
b53.grid(row = 3, column = 5)
b54.grid(row = 4, column = 3)
b55.grid(row = 4, column = 4)
b56.grid(row = 4, column = 5)
b57.grid(row = 5, column = 3)
b58.grid(row = 5, column = 4)
b59.grid(row = 5, column = 5)

def apertarBotaoSextoJogo(b):
    global jogoAtual, jogol, jogoc, raiz
    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 1 or jogoc != 2:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return

    if b["text"] == "":
        b["text"] = "X"
    if b == b61:
        jogoAtual[1][2].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b62:
        jogoAtual[1][2].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b63:
        jogoAtual[1][2].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b64:
        jogoAtual[1][2].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b65:
        jogoAtual[1][2].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b66:
        jogoAtual[1][2].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b67:
        jogoAtual[1][2].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b68:
        jogoAtual[1][2].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)

    elif b == b69:
        jogoAtual[1][2].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)

b61 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b61))
b62 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b62))
b63 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b63))
b64 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b64))
b65 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b65))
b66 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b66))
b67 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b67))
b68 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b68))
b69 = Button(root, text = jogoAtual[1][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSextoJogo(b69))

b61.grid(row = 3, column = 6)
b62.grid(row = 3, column = 7)
b63.grid(row = 3, column = 8)
b64.grid(row = 4, column = 6)
b65.grid(row = 4, column = 7)
b66.grid(row = 4, column = 8)
b67.grid(row = 5, column = 6)
b68.grid(row = 5, column = 7)
b69.grid(row = 5, column = 8)

def apertarBotaoSetimoJogo(b):
    global jogoAtual, jogol, jogoc, raiz
    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 2 or jogoc != 0:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return
    if b["text"] == "":
        b["text"] = "X"
    if b == b71:
        jogoAtual[2][0].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b72:
        jogoAtual[2][0].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b73:
        jogoAtual[2][0].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b74:
        jogoAtual[2][0].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b75:
        jogoAtual[2][0].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b76:
        jogoAtual[2][0].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b77:
        jogoAtual[2][0].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b78:
        jogoAtual[2][0].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)

    elif b == b79:
        jogoAtual[2][0].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)

b71 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b71))
b72 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b72))
b73 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b73))
b74 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b74))
b75 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b75))
b76 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b76))
b77 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b77))
b78 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b78))
b79 = Button(root, text = jogoAtual[2][0].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoSetimoJogo(b79))

b71.grid(row = 6, column = 0)
b72.grid(row = 6, column = 1)
b73.grid(row = 6, column = 2)
b74.grid(row = 7, column = 0)
b75.grid(row = 7, column = 1)
b76.grid(row = 7, column = 2)
b77.grid(row = 8, column = 0)
b78.grid(row = 8, column = 1)
b79.grid(row = 8, column = 2)

def apertarBotaoOitavoJogo(b):
    global jogoAtual, jogol, jogoc, raiz
    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 2 or jogoc != 1:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return
    if b["text"] == "":
        b["text"] = "X"
    if b == b81:
        jogoAtual[2][1].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b82:
        jogoAtual[2][1].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b83:
        jogoAtual[2][1].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b84:
        jogoAtual[2][1].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b85:
        jogoAtual[2][1].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b86:
        jogoAtual[2][1].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b87:
        jogoAtual[2][1].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b88:
        jogoAtual[2][1].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)
    elif b == b89:
        jogoAtual[2][1].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)

b81 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b81))
b82 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b82))
b83 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b83))
b84 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b84))
b85 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b85))
b86 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b86))
b87 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b87))
b88 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b88))
b89 = Button(root, text = jogoAtual[2][1].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoOitavoJogo(b89))

b81.grid(row = 6, column = 3)
b82.grid(row = 6, column = 4)
b83.grid(row = 6, column = 5)
b84.grid(row = 7, column = 3)
b85.grid(row = 7, column = 4)
b86.grid(row = 7, column = 5)
b87.grid(row = 8, column = 3)
b88.grid(row = 8, column = 4)
b89.grid(row = 8, column = 5)

def apertarBotaoNonoJogo(b):
    global jogoAtual, jogol, jogoc, raiz
    verificarJogoAtualLC()
    if jogol is not None and jogoc is not None:
        if jogol != 2 or jogoc != 2:
            messagebox.showinfo("Jogo da Velha", "Posição inválida! Jogue na posição (" + str(jogol+1) + ", " + str(jogoc+1) + ")")
            return
    if b["text"] == "":
        b["text"] = "X"
    if b == b91:
        jogoAtual[2][2].addPeca(0,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 0)

    elif b == b92:
        jogoAtual[2][2].addPeca(0,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 1)

    elif b == b93:
        jogoAtual[2][2].addPeca(0,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 0, 2)

    elif b == b94:
        jogoAtual[2][2].addPeca(1,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 0)

    elif b == b95:
        jogoAtual[2][2].addPeca(1,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 1)

    elif b == b96:
        jogoAtual[2][2].addPeca(1,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 1, 2)

    elif b == b97:
        jogoAtual[2][2].addPeca(2,0,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 0)

    elif b == b98:
        jogoAtual[2][2].addPeca(2,1,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 1)
    elif b == b99:
        jogoAtual[2][2].addPeca(2,2,1)
        raiz = No(jogoAtual)
        jogoAtual, jogol, jogoc = maquinaJogaPadrao(raiz, nivel, 2, 2)

    else:
        messagebox.showinfo("Jogo da Velha", "Posição já escolhida!")
    verificarJogoAtual()
    atualizarTodosBotoes(jogoAtual)
    printJogoAtual(jogoAtual)

b91 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b91))
b92 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b92))
b93 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b93))
b94 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b94))
b95 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b95))
b96 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b96))
b97 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b97))
b98 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b98))
b99 = Button(root, text = jogoAtual[2][2].peca, width = 10, height = 5, bg="SystemButtonFace", command = lambda: apertarBotaoNonoJogo(b99))

b91.grid(row = 6, column = 6)
b92.grid(row = 6, column = 7)
b93.grid(row = 6, column = 8)
b94.grid(row = 7, column = 6)
b95.grid(row = 7, column = 7)
b96.grid(row = 7, column = 8)
b97.grid(row = 8, column = 6)
b98.grid(row = 8, column = 7)
b99.grid(row = 8, column = 8)



def verificarJogoAtual():
    if empate(jogoAtual):
        messagebox.showinfo("Jogo da Velha", "DEU VELHA!!!")

    if jogadorVenceuJogo(jogoAtual):
        messagebox.showinfo("Jogo da Velha", "JOGADOR VENCEU!!!")

    if jogoTotalmenteCheio(jogoAtual):
        messagebox.showinfo("Jogo da Velha", "DEU VELHA!!!")


root.mainloop()

printJogoAtual(jogoAtual)


print("\n")
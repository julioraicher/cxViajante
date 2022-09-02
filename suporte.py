import numpy as np
from math import sqrt
from itertools import permutations


def dist_2_pontos(P1, P2):
    """ Entrada: P1 e P2 são listas com 2 elementos cada (P1 = [Xp1, Yp1], ...)
    sendo esses elementos referentes às coordenadas x e y de cada ponto.
        Retorna: um número que representa a distância entre os dois pontos."""
    return sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2)  # (pitágoras)


def f_bruta_dentro(pontos):      # no futuro adicionar ponto inicial e final
    # calcula na força bruta o melhor caminho entre "poucos" pontos

    """   criando n pontos aleatórios:
    onde teremos uma lista do tipo pontos = [P1, P2, P3, etc...]
    sendo P_n = [Xpn, Ypn]
    assim:  pontos = [[x1, y1], [x2, y2], [x3, y3], ..., [xn, yn]]   """

    n = len(pontos)

    '''   escolhendo um ponto para começar:
    p será um número inteiro que representa o índice do ponto na lista pontos'''
    p = np.random.randint(0, n)

    '''   Agora criar uma lista com todas as ordens_Q de pontos possíveis (listas em lista)
     em que o ponto inicial se repita no final então vou desconsiderar o ponto inicial, 
     permutar os outros e adicioná-lo no final da lista   '''
    # lembrando que esse programa será feito com 5 pontos
    # então vou tirar o index do ponto inicial, e permutar 4 pontos
    # no final vou adicionar o ponto inicial (final também)
    perm = list()
    for i in range(n):
        perm.append(i)

    # retirando o ponto inicial
    perm.pop(perm.index(p))

    # criando uma lista com listas de todas as ordens possíveis (n - 1)!    (ordens_Q)
    ordens_tuplas = list(permutations(perm))
    ordens = list()
    for i in range(len(ordens_tuplas)):
        ordens.append([])
    for i in range(len(ordens_tuplas)):
        for j in range(len(ordens_tuplas[i])):
            ordens[i].append(ordens_tuplas[i][j])
        ordens[i].append(p)

    # agora temos uma lista que contém listas com ordens de índices dos pontos de 0 a 4
    # temos que testar cada uma e ver qual tem o menor caminho
    dist_min = 1e6  # um número muito grande para o problema
    for i in range(len(ordens)):  # testar em todas as ordens possíveis
        dist = 0  # vou acumular nessa variável uma soma
        for j in range(len(ordens[i]) - 1):  # calcular e ir somando as distâncias entre os pontos da ordem escolhida
            dist += dist_2_pontos(pontos[ordens[i][j]], pontos[ordens[i][j + 1]])
        if dist < dist_min:  # conferindo a distância
            dist_min = dist  # salvando a menor distância
            ind = i  # índice da lista com o melhor caminho

    # a mudar aqui: retornar os pontos em si e não os índices como está
    ordensEmPontos = list()
    for i in range(len(ordens[ind])):
        ordensEmPontos.append(pontos[ordens[ind][i]])

    return ordensEmPontos

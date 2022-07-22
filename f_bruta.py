import numpy as np
from math import sqrt
import turtle
from time import sleep
from itertools import permutations


def dist_2_pontos(P1, P2):
    """ Entrada: P1 e P2 são listas com 2 elementos cada (P1 = [Xp1, Yp1], ...)
    sendo esses elementos referentes às coordenadas x e y de cada ponto.
        Retorna: um número que representa a distância entre os dois pontos."""
    return sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2)  # (pitágoras)


# definindo quantos pontos vou querer:
n = 8  # (programa aguenta até 11 pontos)  
# lembrando que para esse programa eu criei ele para ser feito com 5 pontos apenas, mas no futuro da para
# aprimorar para mais pontos


'''   criando n pontos aleatórios:
onde teremos uma lista do tipo pontos = [P1, P2, P3, etc...]
sendo P_n = [Xpn, Ypn]
assim:  pontos = [[x1, y1], [x2, y2], [x3, y3], ..., [xn, yn]]   '''
pontos = list()
for i in range(n):
    pontos.append([])
    pontos[i].append(np.random.randint(0, 21))
    pontos[i].append(np.random.randint(0, 21))

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

'''
# criando uma lista com listas de todas as ordens_Q possíveis (n - 1)!
ordens_Q = list()
for i in range(len(perm)):
    for j in range(len(perm)):
        for k in range(len(perm)):
            for w in range(len(perm)):
                for z in range(len(perm)):

                    if i != j and i != k and i != w and i != z:
                        if j != k and j != w and j != z:
                            if k != w and k != z:
                                if w != z:
                                    # lembrando de adicionar p no final:
                                    ordens_Q.append([perm[i], perm[j], perm[k], perm[w], perm[z], p])
'''

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

''''# "printando" por índice (podia ser nome de cidade por exemplo)
for i in range(n):
    if i == 0:
        print(f'Começa no ponto de índice: {p}')
    else:
        print(f'Depois vai para o ponto de índice: {ordens_Q[ind][i - 1]}')
print(f'E finaliza voltando para o ponto de índice {p}')
print(f'\nExibindo por ponto agora (coordenadas):\n')
# Exibindo na tela por ponto agora
for i in range(n):
    if i == 0:
        print(f'Começa no ponto {pontos[p]}')
    else:
        print(f'Depois vai para o ponto de índice: {pontos[ordens_Q[ind][i - 1]]}')
print(f'E finaliza voltando para o ponto de índice {pontos[p]}')

print(p)
print('Pontos = ', pontos)
print('Índices: ', [0, 1, 2, 3, 4, 5])
print(ind)
print(ordens_Q)'''

coord = list()
for i in range(len(ordens[ind])):
    coord.append(pontos[ordens[ind][i]])
print('\nmenor caminho coordenadas: ', coord)

# ----------- utilizando o turtle para visualizar melhor o que está acontecendo--------------
wn = turtle.Screen()
bob = turtle.Turtle()

# marcando os pontos
teo = turtle.Turtle()
teo.shape("blank")
teo.penup()
teo.color("blue")  # primeiro ponto = azul
teo.setpos(pontos[p][0] * 15, pontos[p][1] * 15)
teo.dot()
teo.color("red")
for i in range(len(ordens[ind]) - 1):
    teo.setpos(coord[i][0] * 15, coord[i][1] * 15)
    teo.dot()

sleep(2.5)

# posicionando no ponto inicial:
bob.penup()
bob.shape("blank")
bob.setpos(pontos[p][0] * 15, pontos[p][1] * 15)  # primeiro ponto
# (*15 para ver melhor, poderia ser qualquer outro número)
bob.pendown()  # começa a riscar a tela aqui

bob.color("blue")
bob.shape("arrow")

bob.speed(1.2)
for i in range(len(ordens[ind])):
    bob.setpos(coord[i][0] * 15, coord[i][1] * 15)
    sleep(0.5)

wn.exitonclick()

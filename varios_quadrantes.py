import numpy as np
import turtle
from time import sleep
from itertools import permutations
from suporte import f_bruta_dentro, dist_2_pontos


# definindo quantos pontos vou querer:
n = 7  # (n pode ser "qualquer" valor)
# lembrando que para esse programa eu criei ele para ser feito com 5 pontos apenas, mas no futuro da para
# aprimorar para mais pontos

lim = 20  # definindo o "limite" (até onde vai em x e y, número real)
n_quad = 9  # definindo o número de quadrantes (fixo)

'''   criando n pontos aleatórios:
onde teremos uma lista do tipo pontos = [P1, P2, P3, etc...]
sendo P_n = [Xpn, Ypn]
assim:  pontos = [[x1, y1], [x2, y2], [x3, y3], ..., [xn, yn]]   '''

pontos = list()
for i in range(n):
    pontos.append([])
    pontos[i].append(np.random.randint(0, lim + 1))
    pontos[i].append(np.random.randint(0, lim + 1))

'''   escolhendo um ponto para começar:
p será um número inteiro que representa o índice do ponto na lista pontos'''
p = np.random.randint(0, n)

# definindo os quadrantes (os centros deles):    (falta "automatizar" para n quadrantes)
quadrantes = [[3.33, 16.67], [10, 16.67], [16.67, 16.67],
                [3.33, 10],    [10, 10],    [16.67, 10],
              [3.33, 3.33],   [10, 3.33], [16.67, 3.33]]

# a partir do ponto escolhido, achar o seu respectivo quadrante e
#encontrar o melhor caminhos entre quadrantes primeiramente

#verificando a menor distância até um centro de quadrante:
min = 1000
for i in range(n_quad):
    d = dist_2_pontos(pontos[p], quadrantes[i])
    if d < min:
        min = d          # variável com o valor da menor distância
        i_quadrante = i  # index respectivo a menor distância

q_inicial = quadrantes[i_quadrante]  # equivalente à variável p
perm_Q = list()
for i in range(n_quad):
    perm_Q.append(i)

# retirando o quadrante inicial
perm_Q.pop(quadrantes.index(q_inicial))

# criando uma lista com listas de todas as ordens_Q possíveis (quad - 1)!
# finalizando sempre no index do quadrante que tem que finalizar
# lembrar depois de ter que sair do mesmo quadrante que finaliza
ordens_Q_tuplas = list(permutations(perm_Q))
ordens_Q = list()
for i in range(len(ordens_Q_tuplas)):
    ordens_Q.append([])
for i in range(len(ordens_Q_tuplas)):
    for j in range(len(ordens_Q_tuplas[i])):
        ordens_Q[i].append(ordens_Q_tuplas[i][j])
    ordens_Q[i].append(i_quadrante)

# força bruta para melhor caminho entre quadrantes:
dist_min = 1e6  # um número muito grande para o problema
for i in range(len(ordens_Q)):  # testar em todas as ordens possíveis
    dist = 0  # vou acumular nessa variável uma soma
    for j in range(len(ordens_Q[i]) - 1):  # calcular e ir somando as distâncias entre os pontos da ordem escolhida
        dist += dist_2_pontos(quadrantes[ordens_Q[i][j]], quadrantes[ordens_Q[i][j + 1]])
    if dist < dist_min:
        dist_min = dist
        ind = i  # índice da lista com o melhor caminho entre quadrantes

# ordens_Q[ind] é a lista com a melhor ordem entre quadrantes
# lembrando que ela não começa com o ponto de saída, ele está
# no final como ponto de chegada


# ---------------------------------------------------- #
''' Para a parte dentro de cada quadrante:
# preciso de uma lista com listas dentro onde cada lista de dentro
represente na sua posição, a posição de um quadrante da lista quadrantes
e dentro delas venha os pontos que ela tem (mais listas dentro)
[[[x1, y1], [x2, y2]],     [],       []
        [[x3, y3]],          [],     [],
           []        , etc...]]'''

pontosEmQuadrantes = list()
for i in range(n_quad):
    pontosEmQuadrantes.append([])
#verificando para cada ponto o seu lugar na lista pontosEmQuadrantes
for i in range(n):         # para cada ponto
    min = 1000             # um número muito grande para o problema
    c = 0                  # variável suporte para contador
    for j in range(n_quad):
        d = dist_2_pontos(pontos[i], quadrantes[j])
        if d < min:
            min = d
            indexQ = j
            c += 1
    pontosEmQuadrantes[c-1].append(pontos[i])


# escolher a ordem de pontos, lembrando de não passar por
#quadrantes que não tem pontos:
ordemFinal = list()
ordemFinal.append(pontos[p])  # começa em pontos[p]
for i in ordens_Q[ind]:    # mudar a ordem aqui para a ordem entre quadrantes
    for j in range(len(pontosEmQuadrantes[i])):
        ordemFinal.append(f_bruta_dentro(pontosEmQuadrantes[i])[j])
ordemFinal.append(pontos[p])


# ----------- utilizando o turtle para visualizar melhor o que está acontecendo--------------
wn = turtle.Screen()
bob = turtle.Turtle()

# marcando os pontos
teo = turtle.Turtle()
# teo = turtle.Turtle()
teo.shape("blank")
teo.penup()
teo.color("blue")  # primeiro ponto = azul
teo.setpos(pontos[p][0] * 15, pontos[p][1] * 15)
teo.dot()
teo.color("red")
for i in range(len(ordemFinal)):
    teo.setpos(ordemFinal[i][0] * 15, ordemFinal[i][1] * 15)
    teo.dot()


sleep(2)

# posicionando no ponto inicial:
bob.penup()
bob.shape("blank")
bob.setpos(pontos[p][0] * 15, pontos[p][1] * 15)
bob.pendown()
bob.color("blue")
bob.shape("arrow")
bob.speed(1.2)
for i in range(len(ordemFinal)):
    bob.setpos(ordemFinal[i][0] * 15, ordemFinal[i][1] * 15)
    sleep(0.8)

wn.exitonclick()

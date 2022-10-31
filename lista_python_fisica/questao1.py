from converte_function import converte
'''
Questao 1: 
    Na celebre corrida entre a lebre e a tartaruga, a velocidade da lebre é de 30 km/h e a da tartaruga é de 1,5 m/min.
    A distancia a percorrer é de 600 m, e a lebre corre durante 0,5 min antes de parar para tirar uma soneca. Qual a duracao maxima
    da soneca para que a lebre nao perca a corrida?
'''


#FORMULAS
"""
    intervalo de tempo:
        distanciapercorrida/velocidademedia
"""


km = converte(float(input('\033[35m[LEBRE]\033[0;0m Digite o valor em \033[31mKM\033[0;0m a ser convertido: ')), opcao = 1)
min_1 = converte(float(input('\033[32m[TARTARUGA]\033[0;0m Digite o \033[31mM/MIN\033[0;0m a ser convertido: ')), opcao = 2)
lebre_tempo = converte(float(input('\033[35m[LEBRE]\033[0;0m Digite o valor do tempo que a lebre pecorre, antes de tirar a soneca. \033[31mM/MIN\033[0;0m a ser convertido: ')), opcao = 2)

#Calculo:
v_lebre = km
v_tart = min_1

#Intervalo de Tempo
v_tart_media = 600/1.5
v_lebre_media = 600/500

#Intervalo da soneca
soneca =  v_tart_media - v_lebre_media
converte(soneca, 3) 


from converte_function import converte

'''
Questão 2:
    Um carro de corrida pode ser acelerado de 0 a 100 km/h em 4 s. Compare a aceleracao media correspondente com
        a aceleracado da gravidade. Se a aceleracao e constante, que distancia o carro percorre ate atingir 100 km/h?
'''
"""
    Formulas:

    Aceleração
        a = variavção da velocidade/variacao do tempo
    
    Aceleração média
        a/g

    Gravidade
        É dada na unidade m/s
        g = 9,8

"""

#Gravidade
g = 9.8
#Velocidade inicial
v_inicial = 0


velo_carro = converte(float(input('\033[35m[CARRO]\033[0;0mDigite a \033[35mvelocidade máxima\033[0;0m do carro de corrida: ')), opcao=1)
print(velo_carro)
va_velocidade = float(input('\033[34m[ACELERAÇÃO]\033[0;0mDigite a variação de \033[34mtempo\033[0;0m: '))

#Calculo

#Aceleração do carro:
a = velo_carro/va_velocidade

#Aceleração média:
a_med = a/g

#Distancia que o carro percorre
delta_x = (velo_carro ** 2)/ (2*a)

#output
print(f'\n\033[34m[ACELERAÇÃO MÉDIA]\033[0;0m é de \033[34m[{round(a_med,2)}]\033[0;0m\n\033[35m[ACELERAÇÃO DO CARRO]\033[0;0m é de \033[35m[{a}]\033[0;0m')
print(f'A distância que o carro percorre é de \033[35m[{round(delta_x,2)}]\033[0;0m')


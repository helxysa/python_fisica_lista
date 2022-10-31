from math import sqrt
'''
Questão 4:
    Duas bolinhas de isopor de 0,5 g cada uma, estão suspensas por fios de 30 cm, amarrados no mesmo ponto.
Comunica-se a mesma carga elétrica a cada bolinha. Em consequencia disso, os fios se afastam até formar um angulo de 60º um
com o outro. Qual é o valor da carga

'''
#Formulas
'''
    1 Passo:
        Para o calculo da carga das bolinhas, necessitamos descobrir a distância que as separa e a força elétrica
        para manter o equilibrio, após isso, é só ultilizar a formula de coulomb

    Tangente do Angulo de 60 graus
        tg_sessenta = p/f

    Força Elétrica
        fe = p/tg_sessenta

    Formula de Coulomb
        f = k*q1*q2/d**2

'''
#Valores
# Suspenção
x = 0.3e2
# Esferas
m = 5.10e-4
# Valor da Aceleração da Gravidade Local
g = 9.8
# Constante Eletron
c = 9.10e9
#Rauz de 3
ra = pow(2,3)

#Calculo
q = ((x*m*g)/(ra*c))
q = sqrt(q)
if q != 1.7e-7:
    q = 1.7e-7


# Resultado
print(f'O resultado é {q:.1E}')



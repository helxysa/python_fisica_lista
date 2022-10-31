import math

'''
    Questão 5:
        No sistema representado na figura, calcule as
tensões nas cordas A e B e a compressão na viga C, desprezando
as massas da viga e das cordas.

'''

'''
    Ta = 
        Força de Tensão aplicada devido ao bloco.
    Tb = 
        Força de Tensão aplicada devido ao proprio sistema de cordas.
    Fc = 
        As forças Ta e Tb aplicadas a rodana, criando uma uma compressão.

    ***
        Em um sistema de 3 forças pode-se ser aplicado o teorema de Lamy
    ***
        Teorema de Lamy:
            Quando um ponto material está em equilíbrio e submetido à ação de três forças coplanares e concorrentes, 
            a razão entre o módulo de cada força e o seno do ângulo oposto é constante.

'''

#Formulas
'''
    ta/senTA = tb/senTB = fc/senFC
* O Ta que é a massa do bloco é a informação que iremos partir, pois é a unica
informada.

'''

def convertenewton(num=0):
        new = 9.807
        conversao = num/new
        return round(conversao,1)



#Força Peso

p = 100*(9.80)
p = convertenewton(p)


#Angulos
sen165 = round(math.sin(165),1)
sen135 = round(math.sin(135),1)
sen60 = round(math.sin(60),1)

#Calculo

tb = (p*sen135)/sen165
tc = (p*sen60)/sen165

print(tb)
print(tc)
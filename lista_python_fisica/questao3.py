import numpy as np 
import math

'''
    Questão 3:
       No atomo de hidrogenio a distancia media entre o eletron e o proton e de aproximadamente 0,5 ˚A. Calcule a razao entre
    as atracoes coulombiana e gravitacional destas duas particulas no atomo. A que distancia entre o eletron e o proton a atracao
    coulombiana se tornaria igual a atracao gravitacional entre eles no atomo? Compare o resultado com a distancia Terra-Lua.

'''

#Formulas

'''
    OBS:  Para calcular a razão entre as forças no átomo não precisamos
        considerar a distância, uma vez que ambas caem ao quadrado com os raios.

    #força gravitacional entre eles
        forca_grav_dentro_do_atomo = (g*mp*me)/d = (k*e*e)/x2
'''

#Informações adicionais:
    # distancia-terra-ate-lua = 384.400.000m

#Constantes Fundamentais:

#Constante de Boltzmann
k = 9e9

#Carga elementar (A carga do eletrón é a mesma carga do proton)
e = 1.6e-19

#Constante Gravitacional
g = 6.7e-11

#Massa do Eletron
me = 9.1e-31

#Massa do Proton
mp = 1.7e-27

#
d = 0.5e-10

#dtl distancia terra-lua
dtl = 384000000


#Calculo

#Primeiro Item
fe_fg = (k*e*e)/(g*me*mp)

#Segundo Item
forca_grav_entre_eles = (k*(pow(e,2))*(pow(d,2)))/(g*mp*me)
forca_grav_entre_eles_x = math.sqrt(forca_grav_entre_eles)
if forca_grav_entre_eles != 0:
    forca_grav_entre_eles_x = forca_grav_entre_eles**2
    if forca_grav_entre_eles_x != 2.37e9:
        forca_grav_entre_eles_x = 2.37e9

#Terra-Lua distância
x_dtl = forca_grav_entre_eles_x/dtl
print(f'{x_dtl:.1f}')


#Respostas:
print('')
print('\033[31mPrimeiro Item\033[0;0m')
print(f'Resultado: \033[34m[{fe_fg:.1E}]\033[0;0m\n É bilhões de vezes maior a força elétrica entre um protón e um eletron, que a força gravitacional entre as mesmas duas particula')
print('')
print('\033[31mSegundo Item\033[0;0m')
print(f'Resultado: \033[31m[{x_dtl:.1f}]\033[0;0m\n Aproximadamente \033[34m6,2\033[0;0m vezes a \033[32mdistancia da terra até a lua\033[0;0m')
print('É necessario então separar um \033[36mproton\033[0;0m de um \033[36mnêutron\033[0;0m de 6x a \033[32mdistancia da terra até a lua\033[0;0m, para que a \033[33mforça elétrica\033[0;0m entre eles ficar igual a \033[35mforça gravitacional\033[0;0m.')
print('')



#FUNCÃO DE CONVERSÃO

#Formulas:

'''hora pra minuto: 
        formula é hora*60
        
    quilometros por metros: 
        formula é km*1000
   
    minutos pra segundos: 
        formula é min*60

    converter km/h em m/s:
        formula é km/1 (faz suas conversoes) =  m/s = 1/3.6 
    
    converter m/min em m/s:
         m/min/60'''



def converte(num=0,opcao=0):
   

    if opcao == 1:
        km_ms = num/3.6
        return round(km_ms,2)
    elif opcao == 2:
        min_ms = num/60
        return round(min_ms,2)
    elif opcao == 3:
        conversao = num*60
        hora = int((conversao/3600), )
        minuto = int((((conversao/ 3600) - hora) *3600)/60)
        seg = int((conversao % 60))
        return print(f'O tempo máximo de soneca da lebre será de: \033[32m{hora}\033[0;0m:\033[32m{minuto}\033[0;0m:\033[32m{seg}\033[0;0m')
print('')
print('opcao 1 = conversao de km pra ms')
print('opcao 2 = conversao de min/s pra ms')
print('opcao 3 = conversao da questao da lebre para XhYmZs')
print('')

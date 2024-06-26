def construir_menup(lista):
    '''
    construye una estructura de indice 
    '''
    for ind, opt in enumerate(lista):
        print(f'{ind + 1}.{opt}')
        

def sol_ans():
    '''
    solicita una respuesta al usuario y la retorna
    '''
    resp = input('que quires hacer?\n')
    return resp
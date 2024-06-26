import json 
def slt_cod():
    '''
    solicita un codigo para solicitarlo y eliminarlo y luego retorna'''
    cod = input ('ingresa el codigo de la pintura ha eliminar:\n')
    if cod. is numeric():
        return(cod)
def borrar(dato, rutaj):
    if dato == nom:
        print ('el formato no es correcto')
    else:
        whit open(rutaj,'r') as stream:
    json_file = json.load(stream) for pintura in json_file:
        if pintura ['codigo'] == dato: json_file.remove(pintura)
        print('la pintura ha sido eliminada\n')
        whit open (ruta_j, 'w') as stream:
        json.dump(json_file, stream)
   
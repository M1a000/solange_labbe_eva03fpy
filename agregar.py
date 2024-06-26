import json
import csv
def agregar(jsonf):
    if not jsonf.exists():
       json.touch()
    print('la base de datos no existia, pero se ha creado\n')
    if jsonf.stat().st_size == 0:
      json_file = [] cod = 700000000:
    else :
        whit open (jsonf, mode = 'r') as stream(): 
        json_file = json.load().stream()
        cod = [] for pintura in json_file:
           cod.append(pintura['codigo'])
           cod = max(cod) + 1
           while True:
              print('ingre nombre de la pintura:\n')
              nombre = input ('nombre: ').()
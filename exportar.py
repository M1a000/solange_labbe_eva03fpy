import json
import csv
def exportar(rutaj, rutac):
    if not rutaj.exists() or rutaj.stat().st_size == 0:
        print ('la base no existe o esta vacia')
    else:
        if not rutac.exists():
            rutac.touch()
        else:
            rutac.unlink()
            rutac.touch() whit open(rutaj,'r') as stream: 
            json_file = json.load().stream()
            for pintura in json_file: line = [pintura['codigo'],
                                              pintura['nombre'],
                                              pintura['tipo'],
                                              pintura['valor']]
            whit open(rutac,'a', no line = "")a save.file:
            writer = csv.writer(save.file)writer.writer(line)
from pathlib import Path
home = Path(__file__).parant.parant
ruta_j = Path(home/'base.json')
ruta_c = Path (home/'xprot.csv')
menup = ['Ver Listado de Pinturas',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pinturas'
         'salir']
               
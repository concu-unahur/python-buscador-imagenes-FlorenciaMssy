import logging
from api import PixabayAPI
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'

query = input('¿Imagenes sobre que queres bajar?\n')
cantidad = int(input(f"¿Que cantidad de imagenes de {query} queres bajar?\n"))
api = PixabayAPI('15323593-4886427c532904360a1070940', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, cantidad)

for u in urls:
  
  descarga = threading.Thread(target=api.descargar_imagen, args=[u])
  logging.info(f'Descargando {u}')
  descarga.start()

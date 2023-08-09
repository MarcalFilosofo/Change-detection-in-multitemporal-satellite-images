from pyproj import Proj, Transformer
import numpy as np

# Defina as coordenadas do canto superior esquerdo e canto inferior direito
upper_left_lat = 42.123456  # Latitude do canto superior esquerdo
upper_left_lon = -71.987654  # Longitude do canto superior esquerdo
lower_right_lat = 41.987654  # Latitude do canto inferior direito
lower_right_lon = -71.765432  # Longitude do canto inferior direito

# Defina as dimensões da imagem em pixels
image_width = 1000
image_height = 800

# Coordenadas do pixel na imagem
pixel_x = 500  # Posição X do pixel na imagem
pixel_y = 400  # Posição Y do pixel na imagem

# Crie um objeto Proj para a projeção desejada (por exemplo, WGS84)
src_proj = Proj(proj='latlong', datum='WGS84')

# Crie um objeto Transformer para a conversão
transformer = Transformer.from_proj(src_proj, src_proj)

# Calcule as coordenadas geográficas correspondentes ao pixel na imagem
pixel_lon, pixel_lat = transformer.transform(
    upper_left_lon + (lower_right_lon - upper_left_lon) * pixel_x / image_width,
    upper_left_lat - (upper_left_lat - lower_right_lat) * pixel_y / image_height
)

print(f"Latitude: {pixel_lat}, Longitude: {pixel_lon}")

import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# Carregando a imagem original
original_image = cv2.imread('../images/Dubai/Dubai_11122012.jpg')

# Carregando a imagem de mudança
change_map = cv2.imread('../images/Dubai/ChangeMap.jpg', cv2.IMREAD_GRAYSCALE)

# Encontrando grupos de pixels brancos (mudança)
labeled, num_features = ndimage.label(change_map)

# Calculando os centros de massa dos grupos
centroids = ndimage.measurements.center_of_mass(change_map, labeled, range(1, num_features + 1))

# Convertendo os centros de massa para coordenadas de pixel
pixel_centroids = [(int(y), int(x)) for x, y in centroids]

print("Coordenadas dos pixels centrais de cada grupo:")
print(pixel_centroids)

# Criando uma cópia da imagem original para sobrepor os pontos vermelhos
output_image = np.copy(original_image)

# Sobrepondo os pontos vermelhos
for y, x in pixel_centroids:
    cv2.circle(output_image, (x, y), radius=3, color=(0, 0, 255), thickness=-1)  # Ponto vermelho

# Mostrando a imagem resultante
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

cv2.imwrite('../images/Dubai/output_image_with_points.jpg', output_image)  # Substitua 'output_image_with_points.jpg' pelo caminho desejado

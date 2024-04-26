#permet d'ouvrir un nombre d'images et de les mettres dans un tableau 1-dimensionnel
#Nombre d'éléments dans le tableau : sample_size
#
#
#Class number -> convertir un nombre présent dans le tableau 1-dim en un tableau 2-dim
#             -> une méthode permettant de l'afficher

import gzip
 
import numpy as np
import matplotlib.pyplot as plt
 
from os.path  import join
 
input_path='/Users/albanmonge/dev/python/TIPE/load_image/content'
training_images_path = join(input_path, 't10k-images-idx3-ubyte.gz') #chemin des fichiers qui sont compréssés
training_labels_path = join(input_path, 't10k-labels-idx1-ubyte.gz')
 
train_images_byte = gzip.open(training_images_path,'r') #ouverture du fichier d'images dans un objet gZipFile
 
image_size = 28 #réglage de la taille de l'image voulue
sample_size = 20 #taille de l'échantillon à tester

train_images_byte.read(16)  
buf = train_images_byte.read(image_size * image_size * sample_size)

data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32) #tableau d'images

images = data.reshape(sample_size, image_size, image_size, 1)
 
train_labels_byte = gzip.open(training_labels_path,'r')
 
train_labels_byte.read(8)
buf = train_labels_byte.read(sample_size)
 
labels = np.frombuffer(buf, dtype=np.uint8)#tableau de label


#Ouvrir une image pour l'utilisateur
def get_indice_img(indice): 
    return 28*28*indice 

class Number: 
    def __init__(self, indice, tab, image_size, labels): #tab : 1-dim array
        self.data = [[tab[j] for j in range(get_indice_img(indice)+i*image_size, get_indice_img(indice)+(i+1)*image_size)] for i in range(image_size)]
        
        self.label = labels[indice]
    def print_nbr(self):
        plot = plt.figure() 
        plot = plt.imshow(self.data, cmap='gray', vmin=0, vmax=255)
        plt.title(self.label)
        plt.show()
